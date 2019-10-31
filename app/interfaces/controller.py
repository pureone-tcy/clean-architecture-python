from injector import Injector

from usecase import restaurant


class RestaurantController:

    def __init__(self):
        """
        Usecase dispatcher:
           dependency injection of usecase
        """
        self.usecase = Injector([restaurant.DIMoudule()]).get(
            restaurant.RestaurantUseCase)

    def run(self):
        self.usecase.run()
