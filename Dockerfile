# Используйте официальный образ Python как родительский образ
FROM python:3.11-slim

# Установите рабочий каталог в /app
WORKDIR /app

# Добавьте текущий каталог в контейнер в /app
ADD . /app

# Установите необходимые зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Сделайте порт 80 доступным для мира за пределами этого контейнера
EXPOSE 8080

# Запустите приложение, когда контейнер запускается
CMD ["python", "app.py"]
