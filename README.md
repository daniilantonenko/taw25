## Структура проекта
```
|--- Task_1 - папка 1 задания
|--- Task_2 - папка 2 задания
|--- requirements.txt - зависимости
|--- README.md - описание проекта и инструкция
```


## Инструкция

1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
```
git clone https://github.com/daniilantonenko/taw25.git
```
Или скачайте zip архив по [ссылке](https://github.com/daniilantonenko/taw25/archive/refs/heads/main.zip) и распакуйте его


2. Убедитесь, что на Вашем компьютере установлен Python. В командной строке/терминале выполните команду
```
python -v
```  
Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала.  В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python

3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду
```
cd /здесь укажите путь до директории с проектом
```

4. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду  
```
pip install -r requirements.txt
```
если она не выполняется, то попробуйте
```
pip3 install -r requirements.txt
```
5. Наконец, запустите тесты, выполнив команду  
```
pytest -v
```