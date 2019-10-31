from injector import Injector, Module

from interfaces import console
from usecase import restaurant, repository


class DIMoudule(Module):
    def configure(self, binder):
        binder.bind(repository.IORepository, to=console.Console)


class RestaurantController:
    def __init__(self):
        self.usecase: RestaurantUseCase = Injector([DIMoudule()]).get(
            restaurant.RestaurantUseCase)

    def run(self):
        self.usecase.run()
