'''
                            Логгер

Разработайте класс Logger, который:
1. Создаёт файл лога при инициализации объекта (по указанному пути или по умолчанию в корневой
папке).
*Обеспечить существование только одного объекта этого класса (паттерн Singleton) !!!todo don't understand
+ 2. Название файла должно иметь формат log_dd.mm.yy.
+ 3. Внутри должен быть приватный метод, который возвращает текущую дату.
+ 4. Все события одного дня должны писаться в один файл. Если день меняется, должен создаваться новый
файл при записи в лог по шаблону из п.2
+ 5. Поддерживает метод write_log(), записывающий событие в правильный файл дня в формате:
[06:23:15] Произошедшее событие
+ 6. Поддерживает метод clear_log(), который удаляет записи в файле текущего дня.
+ 7. Поддерживает метод get_logs(), возвращающий записи из файла текущего дня в виде списка (один
элемент списка — запись одного события).
+ 8. Поддерживает метод get_last_event(), который возвращает запись о последнем событии.
+ 9. Поддерживает метод get_all_logs(), который возвращает список всех файлов лога.
Предусмотреть крайние ситуации при которых возможен вылет. Исключить возможные ошибки
конструкциями try-except и raise exception.
'''
import datetime
import os


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Logger(metaclass=Singleton):
    __last_event = None
    __LOG_FOLDER = "./logs"

    def __init__(self):
        if not os.path.exists(self.__LOG_FOLDER):
            os.makedirs(self.__LOG_FOLDER)

        filename = self.__get_filename()

        event = "object initialization"
        self.__write_log(filename, event)

    def __get_filename(self):
        return str(self.__LOG_FOLDER+"/log_" + self.__get_current_date())+".txt"

    @staticmethod
    def __get_current_date():
        return str(datetime.datetime.now().strftime("%d.%m.%y"))

    def __write_log(self, filename, event):
        log_message = "[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + event + "\n"
        with open(filename, 'a', encoding="UTF-8") as file:
            file.write(log_message)
            self.__last_event = log_message

    def clear_log(self):
        filename = self.__get_filename()
        with open(filename, 'w', encoding="UTF-8") as file:
            file.write('')

    def get_logs(self):
        filename = self.__get_filename()
        with open(filename, 'r', encoding="UTF-8") as file:
            events = {}
            for s in file:
                r = s.split(" ", 1)
                events[r[0]] = r[1]

        return events

    def get_last_event(self):
        return self.__last_event

    def get_all_logs(self):
        try:
            dirlist = os.listdir(self.__LOG_FOLDER)
            print(dirlist)
        except Exception as e:
            print(e)
        # pass


if __name__ == "__main__":
    print('start')

    l1 = Logger()
    l2 = Logger()

    date = datetime.datetime.now() + datetime.timedelta(days=1)
    print(date.strftime("%d.%m.%y"))#.date())

    print('end')



