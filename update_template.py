#!/usr/bin/env python
"""
Скрипт для обновления Django шаблона из собранного Vite index.html
"""
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIST = BASE_DIR / 'frontend' / 'dist'
TEMPLATE_PATH = BASE_DIR / 'cars' / 'templates' / 'index.html'

def update_template():
    """Обновляет Django шаблон из собранного Vite index.html"""
    index_html_path = FRONTEND_DIST / 'index.html'
    
    if not index_html_path.exists():
        print(f"Ошибка: {index_html_path} не найден. Сначала выполните сборку фронтенда.")
        return False
    
    with open(index_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Извлекаем CSS файлы
    css_pattern = r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"[^>]*>'
    css_matches = re.findall(css_pattern, content)
    
    # Извлекаем JS файлы
    js_pattern = r'<script[^>]*src="([^"]+)"[^>]*>'
    js_matches = re.findall(js_pattern, content)
    
    # Извлекаем preload ссылки для шрифтов
    preload_pattern = r'<link[^>]*rel="preload"[^>]*href="([^"]+)"[^>]*>'
    preload_matches = re.findall(preload_pattern, content)
    
    # Извлекаем title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    title = title_match.group(1) if title_match else 'Лучший форум по машинам'
    
    # Извлекаем favicon
    favicon_match = re.search(r'<link[^>]*rel="icon"[^>]*href="([^"]+)"[^>]*>', content)
    favicon = favicon_match.group(1) if favicon_match else '/favicon.ico'
    
    # Создаем новый шаблон
    template_content = f"""{{% load static %}}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="icon" href="{{% static '{favicon.lstrip('/')}' %}}">
"""
    
    # Добавляем preload ссылки
    for preload in preload_matches:
        href = preload.lstrip('/')
        template_content += f'    <link rel="preload" as="font" href="{{% static \'{href}\' %}}" crossorigin="anonymous">\n'
    
    # Добавляем CSS
    for css in css_matches:
        href = css.lstrip('/')
        template_content += f'    <link rel="stylesheet" href="{{% static \'{href}\' %}}">\n'
    
    template_content += """</head>
<body>
    <div id="app"></div>
"""
    
    # Добавляем JS
    for js in js_matches:
        href = js.lstrip('/')
        template_content += f'    <script type="module" src="{{% static \'{href}\' %}}"></script>\n'
    
    template_content += """</body>
</html>
"""
    
    # Сохраняем шаблон
    with open(TEMPLATE_PATH, 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print(f"Шаблон обновлен: {TEMPLATE_PATH}")
    return True

if __name__ == '__main__':
    update_template()

