from injector import inject, Module

from entity import user
from interfaces import repository, console, db


DEFAULT_SYS_NAME = 'Restaurant System'


class DIMoudule(Module):
    def configure(self, binder):
        binder.bind(repository.ConsoleRepository, to=console.Console)
        binder.bind(repository.RestaurantRepository, to=db.Restaurant)


class RestaurantUseCase:
    @inject
    def __init__(self, c: repository.ConsoleRepository,
                 r: repository.RestaurantRepository):
        self.console = c
        self.restaurant = r

    def bind_message(self):
        user_name = self.console.find_user_name()
        return user.User(DEFAULT_SYS_NAME, user_name).bind()

    def run(self):
        self.console.start(self.bind_message())
        self.console.which_like_restaurant(self.bind_message())
        self.console.end(self.bind_message())
