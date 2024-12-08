# Обрезка ссылок с помощью ВК #

Данный код позволит вам получить при вводе обычной ссылки сокращенную ссылку, либо при вводе уже скоращенной ссылки получить количестно переходов по этой ссылке

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

'''

pip install -r requirements.txt

'''
### Переменные оркужения

Часть настроек проекта берется из переменных окружения. Переменные окружения - это переменные, значения котторых присваиваются программе python извне. Чтобы их определить, создайте файл .env рядом с main.py, и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение

пример содержания файла .env при использовании VK:

VK_TOKEN="ваш_токен"

получить VK_TOKEN можно на сайте VK.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).   