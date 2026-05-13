# Hismes Agent - Project Context

## Overview
Hismes — форк [Hermes Agent](https://github.com/NousResearch/hermes-agent) с персистентной памятью через Git-репозиторий.

## Репозитории
| Репо | URL | Назначение |
|------|-----|------------|
| hismes-agent | https://github.com/igor-kurenkov/hismes-agent | Основной код агента |
| hismes-memory | https://github.com/igor-kurenkov/hismes-memory (приватный) | Персистентная память (config.yaml, sessions, memories) |

## Деплой
- **Платформа:** Render.com (free tier)
- **URL:** https://hismes-agent.onrender.com
- **Webhook:** Telegram бот

## Конфигурация Render
```
HERMES_MODEL=meta-llama/llama-3.3-70b-instruct:free
OPENROUTER_API_KEY=<ключ>
HERMES_PROVIDER=openrouter
```

**ВАЖНО:** Render автоматически устанавливает `HERMES_HOME=/opt/render/project/data` — это их preset для persistent storage. НЕ задавай HERMES_HOME в render.yaml!

## Архитектура памяти
1. `run_hismes.py` — точка входа
2. При старте: клонирует `hismes-memory` в `$HERMES_HOME/memory-repo/`
3. Периодически (каждые 5 мин): пушит изменения обратно
4. При сигнале SIGTERM: сохраняет память перед выходом

## Структура HERMES_HOME на Render
```
/opt/render/project/data/
├── config.yaml      # Конфигурация (модель, MCP серверы, web search)
├── .env             # API ключи
├── skills/          # Скиллы (bundled + user)
├── memories/        # Память агента
├── sessions/        # Сессии
├── cache/
│   └── documents/   # Документы для отправки
└── memory-repo/     # Клон hismes-memory (для git sync)
```

## Веб-поиск
| Провайдер | Требует ключ | Статус |
|-----------|--------------|--------|
| DuckDuckGo | Нет | ✅ По умолчанию |
| Tavily | Да (1000/мес бесплатно) | Опционально |
| SearXNG | Нет (URL) | ❌ Блокирует облачные IP (403) |

## MCP (Model Context Protocol)
- Конфигурация MCP серверов хранится в `config.yaml` под ключом `mcp_servers`
- Пример: `hermes mcp add myserver --url https://mcp.example.com/mcp`
- После настройки MCP серверы доступны как инструменты в сессиях

## Скиллы
- Загружаются из `$HERMES_HOME/skills/` при старте
- Bundled skills копируются автоматически из репозитория
- User skills синхронизируются через hismes-memory

## Ключевые файлы
- `run_hismes.py` — main entry point, управление памятью и конфигурацией
- `tools/web_tools.py` — веб-поиск и извлечение контента
- `tools/web_providers/duckduckgo.py` — DuckDuckGo провайдер
- `hermes_cli/config.py` — загрузка конфигурации
- `hermes_cli/mcp_config.py` — управление MCP серверами
- `tools/mcp_tool.py` — MCP клиент

## Ограничения пользователя
- Россия, нет международной карты
- MacBook с проблемным SSD (ограниченное дисковое пространство)

## Переменные окружения
- `HERMES_HOME` — директория для конфигурации (устанавливается Render)
- `HISMES_DATA_DIR` — явное переопределение data directory (опционально)
- `HERMES_MODEL` — модель по умолчанию
- `TAVILY_API_KEY` — опционально для Tavily поиска

## Правила для ассистента
- **WORKLOG.md** обновлять автоматически после каждого значимого изменения (без напоминания)
- Записывать проблемы и решения, чтобы не наступать на грабли дважды
- При старте сессии читать `PROJECT_CONTEXT.md` и `WORKLOG.md`
- Руководствоваться `CLAUDE.md` при работе с кодом
