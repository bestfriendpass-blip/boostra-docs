#!/usr/bin/env python3
"""Проверка свежести документации.

Смотрит поле `last_reviewed: YYYY-MM-DD` во frontmatter каждой страницы и
подсвечивает те, что не пересматривались дольше порога или вовсе без даты.

Это предупреждение ("пора перечитать"), а не ошибка сборки: скрипт всегда
завершается успешно (exit 0). Чтобы сделать его блокирующим, замените
последнюю строку на `sys.exit(1 if (stale or missing) else 0)`.
"""
import datetime
import pathlib
import re
import sys

MAX_AGE_DAYS = 180
DOCS = pathlib.Path("docs")

today = datetime.date.today()
missing: list[str] = []
stale: list[tuple[str, int]] = []

for path in sorted(DOCS.rglob("*.md")):
    # служебные включения не проверяем
    if "includes" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^last_reviewed:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    if not match:
        missing.append(str(path).replace("\\", "/"))
        continue
    reviewed = datetime.date.fromisoformat(match.group(1))
    age = (today - reviewed).days
    if age > MAX_AGE_DAYS:
        stale.append((str(path).replace("\\", "/"), age))

print(f"Проверка свежести (порог {MAX_AGE_DAYS} дней), сегодня {today}\n")

if stale:
    print("Просрочен пересмотр:")
    for name, age in stale:
        print(f"  - {name} — {age} дней назад")
    print()

if missing:
    print("Без даты last_reviewed:")
    for name in missing:
        print(f"  - {name}")
    print()

if not stale and not missing:
    print("Все страницы с актуальной датой пересмотра.")

# Предупреждение, а не ошибка — не блокируем merge.
sys.exit(0)

# демо: правка кода без обновления документации (для проверки бота)
