from abc import ABCMeta, abstractmethod


class ConsoleRepository(metaclass=ABCMeta):
    @abstractmethod
    def view(self, file_name, color=None, isEnd=False):
        pass

    @abstractmethod
    def find_user_name(self):
        pass

    def start(self, message):
        self.view('hello.txt', 'green', message)

    def which_like_restaurant(self, message):
        self.view('which_restaurant.txt', 'green', message)

    def end(self, message):
        self.view('good_by.txt', 'green', message, True)


class RestaurantRepository(metaclass=ABCMeta):
    @abstractmethod
    def find(self):
        pass

    def save(self, name):
        pass
