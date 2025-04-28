#!/bin/bash

set -e

echo "📊 Налаштовуємо базовий моніторинг у Kubernetes..."

# Встановлення Prometheus + Grafana через Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Встановлюємо Prometheus
helm install prometheus prometheus-community/kube-prometheus-stack

echo "✅ Моніторинг через Prometheus та Grafana встановлено."

# Виводимо доступні сервіси
kubectl get svc -n default
