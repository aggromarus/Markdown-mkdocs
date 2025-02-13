# Wiki-сайт на Mkdocs

## Порядок установки

>1. Установка Python 3 (если не установлен)

<details>
<summary>Windows</summary>

> Cкачать с [официального сайта](https://www.python.org/downloads/) и установить, обязательно поставив галочку Add Python to PATH.

</details>
<details>
<summary>Linux</summary>

```
sudo apt update && sudo apt install python3 python3-pip -y
```

</details>
<details>
<summary>MacOS</summary>

```
brew install python
```
</details>

>2. Клонирование репозитория

>3. Установка зависимостей проекта
```
pip install -r requirements.txt
```
>4. Запуск локального сервера документации
```
mkdocs serve
```
>5. Запуск сборки
```
mkdocs build
```
