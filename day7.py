
'''
Практическое задание
+ Создайте класс User и и его наследника класс SuperUser, которые описывают пользователя и супер-пользователя.
В классе User необходимо описать:
+ ● Конструктор, который принимает в качестве параметров значения для атрибутов name, login и password;
+ ● Методы для изменения и получения значений атрибутов;
+ ● Метод show_info, который печатает в произвольном формате значения атрибутов name и login;
+ ● Атрибут класса count для хранения количества созданных экземпляров класса User.
Необходимые условия, которые надо учесть после создания объекта:
+ ● Атрибут name доступен и для чтения, и для изменения;
+ ● Атрибут login доступен только для чтения;
+ ● Атрибут password доступен только для изменения.
В классе SuperUser необходимо описать:
+ ● Конструктор, который принимает в качестве параметров значения для атрибутов name, login, password и role;
+ ● Метод для изменения и получения значения атрибута role;
+ ● Метод show_info, который печатает в произвольном формате значения атрибутов name, login и role;
● Атрибут класса count для хранения количества созданных экземпляров класса SuperUser.
'''


class User:
    __name = 'user'
    __login = 'user'
    __password = ''
    __count = 0

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        User.__count += 1
        # self.__count += 1

    @property
    def count(self):
        return self.__count

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def login(self):
        return self.__login

    # @login.setter
    # def login(self, value):
    #     self.__login = value

    @property
    def password(self):
        #return self.__password
        pass

    @password.setter
    def password(self, value):
        self.__password = value

    def show_info(self):
        print(f'name: {self.name}, login: {self.login}')

    # @classmethod
    # def update_count(cls):
    #     cls.__count += 1


class SuperUser(User):
    __role = ''
    __scount = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.role = role
        SuperUser.__scount += 1

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):
        super().show_info()
        print(f'role: {self.__role}')


if __name__ == "__main__":
    usr1 = User('name1', 'login1', 'pass1')
    super_usr1 = SuperUser('sname1', 'login1', 'pass1', 'role1')

    n = 10
    users = []

    usr_str = 'user'
    login_str = 'login'
    pass_str = 'pass'

    super_usr_str = 'super_user'
    super_login_str = 'super_login'
    super_pass_str = 'super_pass'
    super_role_str = 'super_role'

    for i in range(10):
        users.append(User(usr_str+str(i), login_str+str(i), pass_str+str(i)))
        users.append(SuperUser(super_usr_str+str(i), super_login_str+str(i),
                               super_pass_str+str(i), super_role_str+str(i)))

    print()