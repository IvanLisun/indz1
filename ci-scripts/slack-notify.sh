#!/bin/bash

set -e

if [ -z "$SLACK_WEBHOOK_URL" ]; then
  echo "❌ SLACK_WEBHOOK_URL не встановлено!"
  exit 1
fi

MESSAGE=${1:-"✅ Завдання виконано успішно."}

echo "📨 Надсилаємо повідомлення в Slack..."

curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$MESSAGE\"}" "$SLACK_WEBHOOK_URL"

echo "✅ Повідомлення успішно надіслано в Slack."
