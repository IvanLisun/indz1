# Вказуємо базовий образ для Python
FROM python:3.10-slim

# Встановлюємо необхідні бібліотеки для роботи з додатком
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо бібліотеки для роботи з Docker
RUN pip install --upgrade pip

# Вказуємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо всі файли з локальної системи в контейнер
COPY requirements.txt /app/

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект у контейнер
COPY . /app/

# Вказуємо команду для запуску додатку
CMD ["python", "app.py"]

# Вказуємо порти, які буде використовувати додаток
EXPOSE 5000
