#!/bin/bash

set -e

echo "🧹 Встановлюємо flake8 для перевірки якості коду..."
pip install flake8

echo "🔍 Перевіряємо якість коду у src/ та tests/ ..."
flake8 src/ tests/

echo "✅ Лінтинг пройдено успішно."
