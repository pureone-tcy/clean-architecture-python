from interfaces.repository import RestaurantRepository


class Restaurant(RestaurantRepository):
    def find(self):
        return 'find'

    def save(self, name):
        return '{}'.format(name)
