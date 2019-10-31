from injector import inject, Module

from domain import message
from interfaces import console
from usecase import repository

DEFAULT_SYS_NAME = 'Restaurant System'


class DIMoudule(Module):
    def configure(self, binder):
        binder.bind(repository.IORepository, to=console.Console)


class RestaurantUseCase:
    @inject
    def __init__(self, c: repository.IORepository):
        self.console = c

    def run(self):
        self.console.start(message.Message(DEFAULT_SYS_NAME, '').bind())

        binded_message = message.Message(
            DEFAULT_SYS_NAME,
            self.console.get_user_name()).bind()
        self.console.which_like_restaurant(binded_message)

        self.console.end(binded_message)
