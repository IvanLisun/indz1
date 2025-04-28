#!/bin/bash

set -e

# Змінні
IMAGE_NAME="ghcr.io/${GITHUB_REPOSITORY}:latest"

echo " Збираємо Docker образ: $IMAGE_NAME ..."
docker build -t $IMAGE_NAME .

echo "✅ Docker образ успішно зібраний."
