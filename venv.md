# Virtual Environment

virtualenv — это инструмент, позволяющий создавать виртуальные окружения с пакетами. 
Разные «песочницы» имеют разный набор пакетов разных версий. 
Работая над конкретным проектом, вы просто переключаетесь на подходящую песочницу, и проблема уходит. 

Устанавливаем пакеты:
- virtualenv (pip install virtualenv)
- virtualenvwrapper (Linux: pip install virtualenvwrapper, Win: pip install virtualenvwrapper-win)
Выбираем версию интерпретатора, указываем директорию хранения окружений, указываем директорию для создания проектов: 
```sh
$ export VIRTUALENVWRAPPER_PYTHON=~/anaconda3/bin/python3.7
$ export WORK_ON=~/ENVS
$ export PROJECT_HOME=~/Documents/projects
$ source ~/anaconda3/bin/virtualenvwrapper.sh
```
Теперь можем создавать проект:

```sh
$ mkproject kazpost
```
Создается папка проекта в ```PROJECT_HOME ``` и окружение в ```WORK_ON``` и автоматически активируется окружение проекта. 
При этом окружение не содержит глобальных зависимостей и необходимо устанавливать пакеты непосредственно в него

Деактивировать окружение:
```sh
$ deactivate
```
Удаляем окружение:
```sh
$ rmvirtualenv kazpost
```
Список окружений:
```sh
$ lsvirtualenv
```
Получить список зависимостей можно непосредственно от ```pip```:
```sh
$ pip freeze > requirenments.txt
```
Ну и установить:
```sh
$ pip install -r requirenments.txt
```
