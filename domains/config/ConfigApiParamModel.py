# Facade Pattern
"""
doc: Model class with the decorator
"""
class ConfigApiParamModel(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass


    @property
    def param_name(self):
        return self.__param_name
    @param_name.setter
    def param_name(self, val):
        self.__param_name = val


    @property
    def default_value(self):
        return self.__default_value
    @default_value.setter
    def default_value(self, val):
        self.__default_value = val

    @property
    def current_value(self):
        return self.__current_value
    @current_value.setter
    def current_value(self, val):
        self.__current_value = val

