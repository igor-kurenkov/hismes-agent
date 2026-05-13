# Hismes Agent - Worklog

## 2026-05-08

### Добавление DuckDuckGo провайдера
**Проблема:** Веб-поиск не работал. SearXNG возвращал 403 на облачных IP Render.

**Решение:**
1. Создан `tools/web_providers/duckduckgo.py` — провайдер с ddgs библиотекой и HTTP fallback
2. Обновлён `tools/web_tools.py` — добавлена поддержка DuckDuckGo
3. Обновлён `run_hismes.py` — DuckDuckGo как бэкенд по умолчанию

**Коммиты:**
- `84d49a07` — feat: Add DuckDuckGo web search provider
- `2fb2e145` — fix: DuckDuckGo provider with HTTP fallback

### Диагностика веб-поиска
**Проблема:** После добавления DuckDuckGo поиск всё равно не работал. В логах только `SyntaxWarning`.

**Анализ:**
- Логи Hermes идут в файлы (`~/.hermes/logs/`), а не в stdout
- Render показывает только stdout
- Нет видимости вызывается ли инструмент вообще

**Решение:**
- Добавлены `print(..., flush=True)` в ключевых местах для видимости в логах Render:
  - `run_hismes.py` — при создании config.yaml
  - `web_tools.py` — в `check_web_api_key()`
  - `duckduckgo.py` — при каждом поиске

**Коммит:** `f69babc6` — debug: add stdout logging for Render diagnostics

### Создание документации
- `PROJECT_CONTEXT.md` — контекст проекта
- `WORKLOG.md` — история изменений
- `CLAUDE.md` — guidelines для coding
- Добавлено правило: автоматически обновлять WORKLOG.md после значимых изменений

**Коммит:** `f4783018` — docs: add PROJECT_CONTEXT.md, WORKLOG.md, CLAUDE.md

### Web backend не обновлялся из существующего конфига
**Проблема:** В логах `configured backend='searxng'` вместо `duckduckgo`.

**Причина:** `hismes-memory` репозиторий содержал старый `config.yaml` с `searxng`. Код добавлял web конфиг только если его нет — существующий не перезаписывался.

**Решение:** В `run_hismes.py` изменена логика — всегда обновлять `web.backend` и `web.search_backend` на актуальное значение.

**Коммит:** `85efbd8e` — fix: always update web backend in config.yaml

### Включён auto-deploy на Render
**Изменение:** Добавлен `autoDeploy: true` в `render.yaml`.

**Коммит:** `fb0e5180` — feat: enable autoDeploy on Render

### HERMES_HOME не использовался из переменной окружения
**Проблема:** Hermes не находил конфиг — `~/.hermes/config.yaml` отсутствует.

**Причина:** 
- В render.yaml была переменная `HISMES_HOME`, а не `HERMES_HOME`
- Код использовал `Path.cwd() / ".hismes"` вместо значения из env
- На Render `cwd()` = `/opt/render/project/src/`, а не `/app`

**Решение:**
1. В `run_hismes.py` — читать `HERMES_HOME` из окружения
2. В `render.yaml` — установить `HERMES_HOME=/app/.hismes`
3. Добавлено логирование `HISMES_HOME` при старте

**Коммит:** `a4a7acfd` — fix: use HERMES_HOME from env, set correct path in render.yaml

### Веб-поиск заработал!
**Результат:** После фикса HERMES_HOME, веб-поиск работает через Tavily.

**Нюанс:** Render переопределяет `HERMES_HOME` на `/opt/render/project/data` (их стандартный persistent путь). Это нормально — главное что конфиг создаётся в правильном месте.

**Коммит:** `9fe54810` — debug: add config file verification logging

---

## 2026-05-11

### Bundled skills не копировались при старте
**Проблема:** Скиллы не загружались на Render, т.к. `HERMES_HOME/skills/` был пуст.

**Причина:** Bundled skills (из `./skills/` репозитория) не копировались автоматически в `HERMES_HOME/skills/`. Hermes ожидает скиллы именно в `HERMES_HOME/skills/`, а не в директории с исходным кодом.

**Решение:**
1. Добавлена функция `copy_bundled_skills()` в `run_hismes.py`
2. Функция копирует все скиллы из `./skills/` в `$HERMES_HOME/skills/` при старте
3. Копирование происходит только если целевая директория пуста (не перезаписывает существующие)
4. Копирование идёт после клонирования memory, чтобы скиллы из памяти имели приоритет

### MCP конфигурация не сохранялась
**Проблема:** MCP серверы не работали после перезапуска.

**Причина:** MCP конфигурация должна храниться в `config.yaml` под ключом `mcp_servers`, но этот ключ не добавлялся при создании конфига.

**Решение:**
1. Добавлен ключ `mcp_servers: {}` в базовую конфигурацию
2. При объединении с существующим конфигом MCP сохраняется

### Архитектура скиллов
**Важное понимание:**
- Hermes загружает скиллы из `$HERMES_HOME/skills/` при старте
- Bundled skills (в репозитории) — это "seed" для установки
- User skills хранятся в hismes-memory репозитории
- MCP конфигурация хранится в `config.yaml` под ключом `mcp_servers`

### Конфликт путей HERMES_HOME на Render
**Проблема:** Конфиг, скиллы и MCP настройки терялись между перезапусками.

**Причина:** 
- Render автоматически устанавливает `HERMES_HOME=/opt/render/project/data` (их preset для persistent storage)
- В `render.yaml` было указано `HERMES_HOME=/app/.hismes` — конфликт!
- Memory repo клонировался в `cwd()/hismes-memory-repo` вместо `HERMES_HOME`
- Hermes использовал свой `HERMES_HOME`, а `run_hismes.py` — другой путь

**Решение:**
1. Убрано явное задание `HERMES_HOME` в `render.yaml` — пусть Render управляет
2. Добавлена переменная `HISMES_DATA_DIR` для явного переопределения если нужно
3. Memory repo теперь клонируется ВНУТЬ `HERMES_HOME/memory-repo` для персистентности
4. Добавлены комментарии в код и `render.yaml` с объяснением архитектуры путей

**Ключевые изменения в `run_hismes.py`:**
```python
# Приоритет путей:
# 1. HISMES_DATA_DIR - явная переменная для data directory
# 2. HERMES_HOME - стандартная переменная Hermes (Render preset)
# 3. cwd()/.hismes - fallback для локальной разработки

# Memory repo - ВНУТЬ HERMES_HOME для персистентности
HISMES_MEMORY_REPO = HISMES_HOME / "memory-repo"
```

**Результат:** Все данные (config.yaml, skills, MCP, memories, sessions) теперь в одном месте — `/opt/render/project/data/`

---

## TODO / Известные проблемы

1. ~~**Веб-поиск:**~~ ✅ Заработал через Tavily
2. ~~**Скиллы не загружались:**~~ ✅ Исправлено копированием bundled skills
3. ~~**MCP конфигурация терялась:**~~ ✅ Исправлено сохранением mcp_servers в config.yaml
4. ~~**Пути на Render:**~~ ✅ Исправлено использование HERMES_HOME от Render
5. **Telegram polling conflict:** Предупреждение о конфликтующих инстансах (возможно старый инстанс не остановился)

---

## 2026-05-11 (продолжение)

### Hardcoded пути ~/.hermes
**Проблема:** Некоторые файлы использовали hardcoded путь `~/.hermes` вместо `HERMES_HOME` из переменной окружения.

**Исправлено:**
1. `auto_model.py:254` - теперь использует `get_hermes_home()` с fallback на `~/.hermes`
2. `mcp_serve.py` - уже использует `get_hermes_home()` через try/except
3. `mcp_tool.py` - уже использует `HERMES_HOME` из env с fallback

**Коммит:** `fix: use HERMES_HOME in auto_model.py`

---

## 2026-05-14

### ⭐ Fresh Start от Upstream
**Проблема:** Форк отставал от upstream на 749 коммитов и не имел общей точки слияния (diverged history).

**Решение:**
1. Создана backup ветка `backup-before-fresh-start`
2. Сохранены наши файлы во временную директорию
3. Hard reset на `upstream/main`
4. Возвращены наши файлы с адаптацией под новый upstream:
   - `run_hismes.py` — адаптирован под upstream naming (ddgs вместо duckduckgo)
   - `render.yaml` — добавлен `pip install ddgs` в buildCommand
   - `PROJECT_CONTEXT.md`, `WORKLOG.md`, `CLAUDE.md` — возвращены без изменений
   - `tools/web_providers/duckduckgo.py` — удалён (upstream уже имеет ddgs.py)

**Новые фичи из upstream:**
- Session search с LLM modes (fast/guided/summary)
- Desktop GUI улучшения
- Video generation tool
- Security fixes (shell=True removal)
- Zsh completion fixes
- И многое другое...

**Важно:** Удалён наш дубликат duckduckgo.py — upstream уже имеет ddgs.py провайдер с тем же функционалом.
