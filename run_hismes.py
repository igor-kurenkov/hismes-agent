#!/usr/bin/env python3
"""
Hismes Agent - Форк Hermes с персистентной памятью
"""

import subprocess
import time
import os
import sys
import threading
import signal
import json
import shutil
import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional

# Конфигурация - определяем правильный путь для данных
# Приоритет:
# 1. HISMES_DATA_DIR - явная переменная для data directory (рекомендуется для Render)
# 2. HERMES_HOME - стандартная переменная Hermes (Render может переопределить!)
# 3. cwd()/.hismes - fallback для локальной разработки
#
# ВАЖНО: Render автоматически устанавливает HERMES_HOME=/opt/render/project/data
# Это их preset для persistent storage. Мы должны использовать этот путь!

HISMES_DATA_DIR = os.environ.get("HISMES_DATA_DIR", "").strip()
HERMES_HOME_FROM_ENV = os.environ.get("HERMES_HOME", "").strip()

if HISMES_DATA_DIR:
    # Явный путь - используем его
    HISMES_HOME = Path(HISMES_DATA_DIR)
elif HERMES_HOME_FROM_ENV:
    # HERMES_HOME установлен (Render или пользователь)
    HISMES_HOME = Path(HERMES_HOME_FROM_ENV)
else:
    # Fallback для локальной разработки
    WORK_DIR = Path.cwd()
    HISMES_HOME = WORK_DIR / ".hismes"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_USER = os.environ.get("GITHUB_USER", "")
MEMORY_REPO = os.environ.get("MEMORY_REPO", f"https://github.com/{GITHUB_USER}/hismes-memory.git")
PORT = int(os.environ.get('PORT', 10000))
SAVE_INTERVAL = int(os.environ.get("SAVE_INTERVAL", 300))

# Модель из переменной окружения (приоритет) или по умолчанию
HERMES_MODEL = os.environ.get("HERMES_MODEL", "meta-llama/llama-3.3-70b-instruct:free")
HERMES_PROVIDER = os.environ.get("HERMES_PROVIDER", "openrouter")

# Веб-поиск: DuckDuckGo по умолчанию (бесплатно, без ключа, надёжно для облаков)
# Публичные SearXNG часто блокируют облачные IP с 403 ошибкой
# Tavily API ключ: https://tavily.com (бесплатный tier 1000 запросов/месяц)
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")

def get_web_search_backend():
    """Определяет лучший бэкенд для веб-поиска."""
    if TAVILY_API_KEY:
        return "tavily", "Tavily API"
    return "ddgs", "DuckDuckGo via ddgs (free, no API key)"

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

def run_cmd(cmd, cwd=None, timeout=60):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, r.stdout, r.stderr
    except: return False, "", "Error"

# HTTP сервер для Render health check
def run_http_server():
    import http.server, socketserver
    class H(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hismes OK')
        def log_message(self, *a): pass
    with socketserver.TCPServer(('0.0.0.0', PORT), H) as s:
        log(f"HTTP on port {PORT}")
        s.serve_forever()

def copy_bundled_skills():
    """Копирует bundled skills из репозитория в HERMES_HOME/skills/."""
    skills_target = HISMES_HOME / "skills"
    skills_source = Path.cwd() / "skills"
    
    # Если исходной директории нет - пробуем найти относительно скрипта
    if not skills_source.exists():
        skills_source = Path(__file__).parent / "skills"
    
    if not skills_source.exists():
        log(f"WARNING: Bundled skills not found at {skills_source}")
        return
    
    # Создаём целевую директорию
    skills_target.mkdir(parents=True, exist_ok=True)
    
    # Копируем только если целевая директория пуста или не содержит SKILL.md файлов
    existing_skills = list(skills_target.rglob("SKILL.md"))
    if len(existing_skills) > 50:  # Уже есть много скиллов
        log(f"Skills directory already populated ({len(existing_skills)} skills)")
        return
    
    log(f"Copying bundled skills from {skills_source}...")
    copied = 0
    for skill_dir in skills_source.iterdir():
        if skill_dir.is_dir() and skill_dir.name not in [".git", ".github", "index-cache"]:
            target_dir = skills_target / skill_dir.name
            if not target_dir.exists():
                try:
                    shutil.copytree(skill_dir, target_dir)
                    copied += 1
                except Exception as e:
                    log(f"Warning: could not copy skill {skill_dir.name}: {e}")
    
    # Подсчитываем итоговое количество
    total_skills = list(skills_target.rglob("SKILL.md"))
    log(f"Skills ready: {len(total_skills)} total ({copied} copied this run)")


def create_config_yaml():
    """Создаёт config.yaml с моделью и настройками веб-поиска."""
    config_path = HISMES_HOME / "config.yaml"
    
    # Print to stdout for Render logs visibility
    print(f"[Hismes] create_config_yaml: path={config_path}", flush=True)
    
    # Определяем бэкенд для веб-поиска
    web_backend, web_backend_info = get_web_search_backend()
    
    # Базовая конфигурация
    config = {
        "model": {
            "default": HERMES_MODEL,
            "provider": HERMES_PROVIDER,
        },
        "providers": {},
        "toolsets": ["hermes-cli"],
        "web": {
            "backend": web_backend,
            "search_backend": web_backend,
        },
        "terminal": {
            "backend": "local",
            "cwd": str(Path.home()),
        },
        "agent": {
            "max_turns": 90,
            "gateway_timeout": 1800,
        },
        "display": {
            "language": "en",
        },
        # MCP servers - пустой словарь, можно добавить через hismes-memory
        "mcp_servers": {},
        # Auxiliary models - vision и другие задачи
        "auxiliary": {
            "vision": {
                "provider": "openrouter",
                "model": "google/gemini-2.0-flash-001",  # стабильная vision модель
            },
        },
    }
    
    # Print to stdout for Render logs visibility
    print(f"[Hismes] Creating config.yaml with web backend: {web_backend}", flush=True)
    
    # Если есть существующий конфиг - объединяем
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                existing = yaml.safe_load(f) or {}
            # Сохраняем существующие настройки, но обновляем модель
            if "model" not in existing:
                existing["model"] = config["model"]
            elif isinstance(existing.get("model"), dict):
                if not existing["model"].get("default"):
                    existing["model"]["default"] = HERMES_MODEL
                if not existing["model"].get("provider"):
                    existing["model"]["provider"] = HERMES_PROVIDER
            elif isinstance(existing.get("model"), str):
                # Модель указана как строка - сохраняем
                pass
            # Добавляем веб-конфиг если нет, или обновляем backend
            if "web" not in existing:
                existing["web"] = config["web"]
            else:
                # Всегда обновляем backend на актуальный (searxng не работает на Render)
                print(f"[Hismes] Existing web config: {existing.get('web')}", flush=True)
                existing["web"]["backend"] = web_backend
                existing["web"]["search_backend"] = web_backend
                print(f"[Hismes] Updated web backend to: {web_backend}", flush=True)
            # MCP servers - сохраняем существующие или добавляем пустой словарь
            if "mcp_servers" not in existing:
                existing["mcp_servers"] = {}
            else:
                print(f"[Hismes] Preserving mcp_servers: {list(existing['mcp_servers'].keys())}", flush=True)
            # Skills - сохраняем существующие настройки
            if "skills" in existing:
                print(f"[Hismes] Preserving skills config", flush=True)
            # Auxiliary models - ВСЕГДА обновляем vision чтобы работал
            if "auxiliary" not in existing:
                existing["auxiliary"] = {}
            # Принудительно устанавливаем vision модель
            existing["auxiliary"]["vision"] = {
                "provider": "openrouter",
                "model": "google/gemini-2.0-flash-001",
            }
            print(f"[Hismes] Set auxiliary.vision to openrouter/google/gemini-2.0-flash-001", flush=True)
            config = existing
        except Exception as e:
            log(f"Warning: could not read existing config: {e}")
    
    # Записываем конфиг
    HISMES_HOME.mkdir(parents=True, exist_ok=True)
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
    log(f"Config written: model={HERMES_MODEL}")
    print(f"[Hismes] Final web config: {config.get('web')}", flush=True)
    print(f"[Hismes] Final auxiliary config: {config.get('auxiliary')}", flush=True)

def create_env_file():
    """Создаёт .env с ключами."""
    env_path = HISMES_HOME / ".env"
    
    env_vars = {}
    
    # Читаем существующий .env если есть
    if env_path.exists():
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line and not line.startswith('#'):
                        key, val = line.split('=', 1)
                        env_vars[key.strip()] = val.strip()
        except:
            pass
    
    # Добавляем переменные из окружения (если не пустые)
    env_mappings = {
        "OPENROUTER_API_KEY": "OPENROUTER_API_KEY",
        "OPENAI_API_KEY": "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY": "ANTHROPIC_API_KEY",
        "TAVILY_API_KEY": "TAVILY_API_KEY",
        "FIRECRAWL_API_KEY": "FIRECRAWL_API_KEY",
        "EXA_API_KEY": "EXA_API_KEY",
        "PARALLEL_API_KEY": "PARALLEL_API_KEY",
        "TELEGRAM_BOT_TOKEN": "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_ALLOWED_USERS": "TELEGRAM_ALLOWED_USERS",
    }
    
    for env_var, key in env_mappings.items():
        val = os.environ.get(env_var, "")
        if val and key not in env_vars:
            env_vars[key] = val
    
    # Записываем
    with open(env_path, 'w', encoding='utf-8') as f:
        for key, val in env_vars.items():
            f.write(f"{key}={val}\n")
    log(f".env written with {len(env_vars)} variables")

# Git память
class Memory:
    def __init__(self, repo_url, token):
        self.repo_url = repo_url
        self.token = token
        self.mem_dir = HISMES_HOME
    
    def setup_git(self):
        run_cmd(["git", "config", "--global", "user.email", "h@h.h"])
        run_cmd(["git", "config", "--global", "user.name", "Hismes"])
    
    def get_url(self):
        if self.token and "@" not in self.repo_url:
            return self.repo_url.replace("https://", f"https://x-access-token:{self.token}@")
        return self.repo_url
    
    def clone(self):
        log("Cloning memory repo...")
        # Клонируем во временную директорию, чтобы не удалить саму себя
        import tempfile
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_repo = Path(tmp_dir) / "memory-repo"
            ok, _, err = run_cmd(["git", "clone", "--depth", "1", self.get_url(), str(tmp_repo)], timeout=120)
            if ok:
                log("Memory cloned")
                src = tmp_repo / ".hismes"
                if src.exists():
                    # Копируем содержимое .hismes в HISMES_HOME
                    # НЕ удаляем HISMES_HOME целиком, т.к. там может быть важное
                    # Копируем поверх с dirs_exist_ok=True
                    self.mem_dir.mkdir(parents=True, exist_ok=True)
                    for item in src.iterdir():
                        tgt = self.mem_dir / item.name
                        if tgt.exists():
                            if tgt.is_dir():
                                shutil.rmtree(tgt)
                            else:
                                tgt.unlink()
                        if item.is_dir():
                            shutil.copytree(item, tgt)
                        else:
                            shutil.copy2(item, tgt)
                    log("Memory loaded")
                    return
            log(f"Clone failed or no .hismes, creating new memory")
        # Создаём базовую структуру если не было памяти
        self.mem_dir.mkdir(parents=True, exist_ok=True)
        (self.mem_dir / "memories").mkdir(exist_ok=True)
        (self.mem_dir / "sessions").mkdir(exist_ok=True)
    
    def push(self):
        """Сохраняет память в git репозиторий."""
        if not self.mem_dir.exists():
            log("No memory to save")
            return

        # Клонируем во временную директорию для push
        import tempfile
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_repo = Path(tmp_dir) / "memory-repo"
            ok, _, err = run_cmd(["git", "clone", "--depth", "1", self.get_url(), str(tmp_repo)], timeout=120)
            if not ok:
                log(f"Failed to clone for push: {err}")
                return

            # Копируем .hismes из HISMES_HOME в репозиторий
            tgt = tmp_repo / ".hismes"
            if tgt.exists():
                shutil.rmtree(tgt)
            if self.mem_dir.exists():
                shutil.copytree(self.mem_dir, tgt)

            # Проверяем есть ли изменения
            ok, out, _ = run_cmd(["git", "status", "--porcelain"], cwd=tmp_repo)
            if not out.strip():
                return  # Нет изменений

            # Commit и push
            run_cmd(["git", "add", "-A"], cwd=tmp_repo)
            run_cmd(["git", "commit", "-m", f"mem {datetime.now():%Y-%m-%d %H:%M}"], cwd=tmp_repo)
            ok, _, err = run_cmd(["git", "push"], cwd=tmp_repo, timeout=60)
            if ok:
                log("Memory saved")
            else:
                log(f"Push failed: {err}")

# Глобальная переменная для сигнала
shutting_down = False
mem = None

def on_signal(signum, frame):
    global shutting_down
    log(f"Signal {signum}, saving...")
    shutting_down = True
    if mem: mem.push()
    log("Exiting for restart...")
    sys.exit(1)  # Exit(1) = Render перезапустит

def main():
    global mem, shutting_down
    
    # Определяем бэкенд для веб-поиска
    web_backend, web_backend_info = get_web_search_backend()
    
    log("=" * 40)
    log("HISMES AGENT")
    log(f"HISMES_HOME: {HISMES_HOME}")
    log(f"HERMES_HOME from env: {HERMES_HOME_FROM_ENV or '(not set)'}")
    log(f"Model: {HERMES_MODEL}")
    log(f"Provider: {HERMES_PROVIDER}")
    log(f"Web search: {web_backend_info}")
    
    # Память
    mem = Memory(MEMORY_REPO, GITHUB_TOKEN)
    mem.setup_git()
    mem.clone()
    
    # Копируем bundled skills (делаем это после клонирования памяти,
    # чтобы skills из памяти имели приоритет)
    copy_bundled_skills()
    
    # Создаём конфигурацию с моделью
    create_config_yaml()
    create_env_file()
    
    # HERMES_HOME для Hermes (убедимся что установлен)
    os.environ["HERMES_HOME"] = str(HISMES_HOME)
    log(f"Set HERMES_HOME={HISMES_HOME}")
    
    # Проверим что конфиг существует
    config_file = HISMES_HOME / "config.yaml"
    if config_file.exists():
        log(f"Config file exists: {config_file}")
        # Выведем содержимое для проверки
        try:
            with open(config_file, 'r') as f:
                content = f.read()
            print(f"[Hismes] Config content preview:\n{content[:500]}...", flush=True)
        except Exception as e:
            log(f"Could not read config: {e}")
    else:
        log(f"WARNING: Config file NOT found: {config_file}")
    
    # Передаём Tavily API ключ если есть
    if TAVILY_API_KEY:
        os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
    # DuckDuckGo работает без API ключа - настраивается в config.yaml
    
    # HTTP сервер
    threading.Thread(target=run_http_server, daemon=True).start()
    
    # Периодическое сохранение
    def save_loop():
        while not shutting_down:
            time.sleep(SAVE_INTERVAL)
            if not shutting_down and mem:
                mem.push()
    threading.Thread(target=save_loop, daemon=True).start()
    
    # Сигналы
    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    
    # Главный цикл
    while not shutting_down:
        try:
            log("Starting Hermes Gateway...")
            p = subprocess.Popen(
                ['python', '-m', 'hermes_cli.main', 'gateway', 'run'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            for line in iter(p.stdout.readline, ''):
                if shutting_down: break
                print(line, end='', flush=True)
            
            code = p.wait()
            log(f"Hermes exited (code {code})")
            
            if not shutting_down:
                mem.push()
                log("Restart in 5s...")
                time.sleep(5)
            
        except KeyboardInterrupt:
            shutting_down = True
            mem.push()
            break
        except Exception as e:
            log(f"Error: {e}")
            time.sleep(10)
    
    log("Shutdown complete")

if __name__ == "__main__":
    main()
