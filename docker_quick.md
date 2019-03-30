# Docker
Installation on Linux: https://bit.ly/2FJrm8G

Installation on Windows: https://dockr.ly/2FMrNQO

Отличное видео: https://bit.ly/2sIu45D

Создадим свой ```Hello World!``` на python

Первое, создаем файл который будет исполняться (```main.py```):
```sh
print('Hello World!)
```
Затем нужно создать сам файл контейнера (```Dockerfile```):
```sh
FROM python:3
ADD my_script.py /
CMD [ "python", "./my_script.py" ]
```
- ```FROM``` - указывает Doker какой образ использовать в качестве основы (можно найти на hub.docker.com)
- ```ADD``` - копирует файл из текущей директории в директорию контейнера
- ```CMD``` - исполняет команду 

Теперь уже собираем контейнер, указываем его имя и путь до ```Dockerfile```:
```sh
$ docker build -t phello .
```
Запускаем контейнер:
```sh
$ docker run phello
```
