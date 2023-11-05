class Program:
    def __init__(self, commands, parent=None):
        self.parent = parent
        self.commands = commands

    def __str__(self):
        return "BEGIN\n" + "\n".join(map(str, self.commands)) + "\nEND"
    

    def to_python(self, indent=0):
        return """
import time
import random
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color


toy = scanner.find_toy()

with SpheroEduAPI(toy) as droid:
""" + "\n".join(map(lambda x: x.to_python(indent + 1), self.commands))


class RollStatement:
    def __init__(self, degrees, speed, seconds, parent=None):
        self.parent = parent
        self.degrees = degrees
        self.speed = speed
        self.seconds = seconds

    def __str__(self):
        return "ROLL " + str(self.degrees) + " DEGREES AT " + str(self.speed) + " SPEED FOR " + str(self.seconds) + " SECONDS"
    
    def to_python(self, indent=0):
        return "    " * indent + "droid.roll(" + str(self.degrees) + ", " + str(self.speed) + ", " + str(self.seconds) + ")"


class LEDStatement:
    def __init__(self, red, green, blue, parent=None):
        self.parent = parent
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return "LED " + str(self.red) + " " + str(self.green) + " " + str(self.blue)
    
    def to_python(self, indent=0):
        return "    " * indent + "droid.set_main_led(Color(r=" + str(self.red) + ", g=" + str(self.green) + ", b=" + str(self.blue) + "))"


class SoundStatement:
    def __init__(self, sound, parent=None):
        self.parent = parent
        self.sound = sound

    def __str__(self):
        return "SOUND " + str(self.sound)
    
    def to_python(self, indent=0):
        return "    " * indent + "droid.play_sound(" + str(self.sound) + ")"


class DeclareStatement:
    def __init__(self, name, value, parent=None):
        self.parent = parent
        self.name = name
        self.value = value

    def __str__(self):
        return "DECLARE " + str(self.name) + " " + str(self.value)
    
    def to_python(self, indent=0):
        return "    " * indent + str(self.name) + " = " + str(self.value)


class AssignStatement:
    def __init__(self, name, value, parent=None):
        self.parent = parent
        self.name = name
        self.value = value

    def __str__(self):
        return "ASSIGN " + str(self.name) + " " + str(self.value)
    
    def to_python(self, indent=0):
        return "    " * indent + str(self.name) + " = " + str(self.value)


class IfStatement:
    def __init__(self, condition, body, parent=None):
        self.parent = parent
        self.condition = condition
        self.body = body

    def __str__(self):
        return "IF " + str(self.condition) + " THEN\n" + "\n".join(map(str, self.body)) + "\nEND"
    
    def to_python(self, indent=0):
        return "    " * indent + "if " + str(self.condition) + ":\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))


class ElseStatement:
    def __init__(self, body, parent=None):
        self.parent = parent
        self.body = body

    def __str__(self):
        return "ELSE\n" + "\n".join(map(str, self.body)) + "\nEND"
    
    def to_python(self, indent=0):
        return "    " * indent + "else:\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))


class CompareExpression:
    def __init__(self, left, op, right, parent=None):
        self.parent = parent
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return str(self.left) + " " + str(self.op) + " " + str(self.right)
    
    def to_python(self, indent=0):
        return str(self.left) + " " + str(self.op) + " " + str(self.right)


class Random:
    def __init__(self, min, max, parent=None):
        self.parent = parent
        self.min = min
        self.max = max

    def __str__(self):
        return "random(" + str(self.min) + ", " + str(self.max) + ")"
    
    def to_python(self, indent=0):
        return "random.randint(" + str(self.min) + ", " + str(self.max) + ")"


class Literal:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def to_python(self, indent=0):
        return str(self.value)


class LoopUntil:
    def __init__(self, condition, body, parent=None):
        self.parent = parent
        self.condition = condition
        self.body = body

    def __str__(self):
        return "LOOP UNTIL " + str(self.condition) + " DO\n" + "\n".join(map(str, self.body)) + "\nEND"
    
    def to_python(self, indent=0):
        return "    " * indent + "while not " + str(self.condition) + ":\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))


class LoopTimes:
    def __init__(self, times, body, parent=None):
        self.parent = parent
        self.times = times
        self.body = body

    def __str__(self):
        return "LOOP TIMES " + str(self.times) + " DO\n" + "\n".join(map(str, self.body)) + "\nEND"
    
    def to_python(self, indent=0):
        return "    " * indent + "for i in range(" + str(self.times) + "):\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))


class LoopForever:
    def __init__(self, body, parent=None):
        self.parent = parent
        self.body = body

    def __str__(self):
        return "LOOP FOREVER DO\n" + "\n".join(map(str, self.body)) + "\nEND"
    
    def to_python(self, indent=0):
        return "    " * indent + "while True:\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))
