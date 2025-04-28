#!/bin/bash

set -e

echo "🧪 Встановлюємо тестові залежності..."
pip install pytest

echo "🔎 Запускаємо юніт-тести..."
pytest tests/unit

echo "🔎 Запускаємо інтеграційні тести..."
pytest tests/integration

echo "✅ Всі тести успішно пройдені."
