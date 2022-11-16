from .util import Util

class Servo:
    def __init__(self, servo_id, initial=500, minimum=500, maximum=2500):
        self.servo_id = servo_id
        self.__value = initial

    def __get_value(self):
        return self.__value  # do we even care about casting?

    def __set_value(self, value):
        self.__value = value

    value = property(__get_value, __set_value)
