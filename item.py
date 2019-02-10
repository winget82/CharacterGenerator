# class for items

class Item:
    """Item Object Class"""
    def __init__(self, name, description, effect, value):
        self.name = name
        self.description = description
        self.effect = effect
        self.value = value