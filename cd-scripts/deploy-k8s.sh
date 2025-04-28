#!/bin/bash

set -e

echo "🚀 Починаємо деплой у Kubernetes..."

# Змінна для імеджу
IMAGE_NAME="ghcr.io/${GITHUB_REPOSITORY}:latest"

# Оновлюємо контейнер у Deployment
kubectl set image deployment/my-deployment my-container=$IMAGE_NAME

# Чекаємо завершення оновлення
kubectl rollout status deployment/my-deployment

echo "✅ Деплой у Kubernetes завершено успішно."
