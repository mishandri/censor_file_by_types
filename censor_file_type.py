import os
import time
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logname = "log308.log"#название для лога

#Класс для отслеживания события
path_file = open('source_path.txt','r') #Отслеживаемые пути. Желательно не пересекать пути
types_file = open('file_types.txt','r') #Разрешённые типы файлов

#SOURCE_PATH - список путей (используется пока только 1)
SOURCE_PATH = [line.strip() for line in path_file.readlines()]

#FILE_TYPES - множество типов файлов, могут повторяться
FILE_TYPES = {line.strip() for line in types_file.readlines()}

path_file.close()   #Закрыли файл
types_file.close()  #Закрыли файл

#Класс для слежки за файлами. Нужно только create и moved
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        #print("Создан файл:", event.src_path)
        #Проверяем расширение исходного файла и если совпадает с типами, то удаляем
        ext = event.src_path.split('.')[-1].lower()
        if ext not in FILE_TYPES:
            while True:
                try:
                    os.remove(event.src_path)
                    log_file = open(logname,'a')
                    string = str(datetime.datetime.today())[:19:] + "\tудалён\t" + event.src_path
                    print(string)
                    log_file.write(string + '\n')
                    log_file.close()
                    break
                except PermissionError:
                    log_file = open(logname,'a')
                    string = str(datetime.datetime.today())[:19:] + "\tзанят\t" + event.src_path
                    print(string)
                    log_file.write(string + '\n')
                    log_file.close()

    def on_moved(self, event):
        #print("Перемещён\переименован файл:", event.src_path, event.dest_path)
        #Проверяем расширение переименнованого файла и если совпадает с типами, то удаляем
        ext = event.dest_path.split('.')[-1].lower()
        if ext not in FILE_TYPES:
            while True:
                try:
                    os.remove(event.dest_path)
                    log_file = open(logname,'a')
                    string = str(datetime.datetime.today())[:19:] + "\tудалён\t" + event.dest_path
                    print(string)
                    log_file.write(string + '\n')
                    log_file.close()
                    break
                except PermissionError:
                    log_file = open(logname,'a')
                    string = str(datetime.datetime.today())[:19:] + "\tзанят\t" + event.dest_path
                    print(string)
                    log_file.write(string + '\n')
                    log_file.close()

print('Из путей:\n',SOURCE_PATH, '\nНе будут удаляться файлы типа:\n', FILE_TYPES)

                
#Запускаем My_handler
event_handler = MyHandler()
observer = Observer()
for index in range(len(SOURCE_PATH)):
    observer.schedule(event_handler, path=SOURCE_PATH[index], recursive=True)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
