#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка Python зависимостей
pip install -r requirements.txt


# Очистка старых статических файлов
python manage.py collectstatic --no-input --clear

# Сборка фронтенда
cd frontend
npm install
npm install unplugin-vue-components --save-dev
npm run build
cd ..

# Обновление Django шаблона из собранного index.html
python update_template.py

# Сборка бэкенда
python manage.py collectstatic --no-input
python manage.py migrate

# Создание суперпользователя
python create_superuser.py 