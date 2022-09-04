class Restaurant:
    __table__ = "restaurants"
    columns = ["name", "address", "city", "category", "rating", "url"]

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
