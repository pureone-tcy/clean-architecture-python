from injector import Injector

from usecase import rank


class Robot:
    def __init__(self):
        self.usecase = Injector([rank.DIMoudule()]).get(rank.RestaurantUseCase)

    def run(self):
        self.usecase.run()
