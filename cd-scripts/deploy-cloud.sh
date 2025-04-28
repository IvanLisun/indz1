#!/bin/bash

set -e

echo "☁️ Починаємо деплой у хмару (AWS/GCP)..."

# Приклад для AWS ECS CLI деплою
# (Ти можеш змінити під конкретну хмару і сервіс)

# Логін до AWS ECR або інше сховище контейнерів
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Пуш Docker образу
docker tag $LOCAL_IMAGE_NAME $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPOSITORY_NAME:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPOSITORY_NAME:latest

# Оновлення сервісу (ECS)
aws ecs update-service --cluster $CLUSTER_NAME --service $SERVICE_NAME --force-new-deployment

echo "✅ Деплой у хмару завершено успішно."
