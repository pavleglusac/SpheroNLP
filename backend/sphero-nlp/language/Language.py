indent_marker = "    "


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

    def to_javascript(self, indent=0):

        return """
async function startProgram()  { 
""" + "\n".join(map(lambda x: x.to_javascript(indent + 1), self.commands)) + "\n" + indent_marker + "exitProgram();\n}"

    def to_codeblocks(self, indent = 0):
        return "".join(map(lambda x: x.to_codeblocks(indent + 1) + ',', self.commands))


class RollStatement:
    def __init__(self, degrees, speed, seconds, parent=None):
        self.parent = parent
        self.degrees = degrees
        self.speed = speed
        self.seconds = seconds

    def __str__(self):
        return "ROLL " + str(self.degrees) + " DEGREES AT " + str(self.speed) + " SPEED FOR " + str(
            self.seconds) + " SECONDS"

    def to_python(self, indent=0):
        return indent_marker * indent + "droid.roll(" + str(self.degrees) + ", " + str(self.speed) + ", " + str(
            self.seconds) + ")"

    def to_javascript(self, indent=0):
        return indent_marker * indent + "await roll(" + str(self.degrees) + ", " + str(self.speed) + ", " + str(
            self.seconds) + ");"

    def to_codeblocks(self, indent = 0):
        return str(['roll', indent, self.degrees, self.speed, self.seconds])


class LEDStatement:
    def __init__(self, red, green, blue, parent=None):
        self.parent = parent
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return "LED " + str(self.red) + " " + str(self.green) + " " + str(self.blue)

    def to_python(self, indent=0):
        return indent_marker * indent + "droid.set_main_led(Color(r=" + str(self.red) + ", g=" + str(
            self.green) + ", b=" + str(self.blue) + "))"

    def to_javascript(self, indent=0):
        return indent_marker * indent + "set_main_led({ r:" + str(self.red) + ", g:" + str(self.green) + ", b:" + str(
            self.blue) + "});"

    def to_codeblocks(self, indent = 0):
        return str(['led', indent, self.red, self.green, self.blue])


class SoundStatement:
    def __init__(self, sound, parent=None):
        self.parent = parent
        self.sound = sound

    def __str__(self):
        return "SOUND " + str(self.sound)

    def to_python(self, indent=0):
        return indent_marker * indent + "droid.play_sound(" + str(self.sound) + ")"

    def to_javascript(self, indent=0):
        return indent_marker * indent + "await Sound.Game." + str(self.sound) + ".play(true);"

    def to_codeblocks(self, indent = 0):
        return str(['sound', indent, self.sound])


class DeclareStatement:
    def __init__(self, name, value, parent=None):
        self.parent = parent
        self.name = name
        self.value = value

    def __str__(self):
        return "DECLARE " + str(self.name) + " " + str(self.value)

    def to_python(self, indent=0):
        return indent_marker * indent + str(self.name) + " = " + str(self.value)

    def to_javascript(self, indent=0):
        return indent_marker * indent + "var " + str(self.name) + " = " + str(self.value) + ";"

    def to_codeblocks(self, indent = 0):
        return str(['declare', indent, self.name, self.value])


class AssignStatement:
    def __init__(self, name, value, parent=None):
        self.parent = parent
        self.name = name
        self.value = value

    def __str__(self):
        return "ASSIGN " + str(self.name) + " " + str(self.value)

    def to_python(self, indent=0):
        return indent_marker * indent + str(self.name) + " = " + str(self.value)

    def to_javascript(self, indent=0):
        return indent_marker * indent + str(self.name) + " = " + str(self.value) + ";"

    def to_codeblocks(self, indent = 0):
        return str(["assign", indent, self.name, self.value])


class IfStatement:
    def __init__(self, condition, body, parent=None):
        self.parent = parent
        self.condition = condition
        self.body = body

    def __str__(self):
        return "IF " + str(self.condition) + " THEN\n" + "\n".join(map(str, self.body)) + "\nEND"

    def to_python(self, indent=0):
        return indent_marker * indent + "if " + str(self.condition) + ":\n" + "\n".join(
            map(lambda x: x.to_python(indent + 1), self.body))

    def to_javascript(self, indent=0):
        return indent_marker * indent + "if (" + str(self.condition) + ")   {\n" + "\n".join(
            map(lambda x: x.to_javascript(indent + 1), self.body)) + "\n" + indent_marker * indent + "}"

    def to_codeblocks(self, indent = 0):
        return str(["if", indent, get_body_lines_count(self.body)]) + ',' + ''.join(self.condition.to_codeblocks()) + ',' + ','.join(map
               (lambda x: x.to_codeblocks(indent + 1), self.body))


class IfElseStatement:
    def __init__(self, condition, body, elsebody, parent=None):
        self.parent = parent
        self.condition = condition
        self.body = body
        self.elsebody = elsebody

    def __str__(self):
        return "IF " + str(self.condition) + " THEN\n" + "\n".join(map(str, self.body)) + "\n ELSE\n" + "\n".join(map(str, self.elsebody)) + "\nEND"

    def to_python(self, indent=0):
        return indent_marker * indent + "if " + str(self.condition) + ":\n" + "\n".join(
            map(lambda x: x.to_python(indent + 1), self.body)) + "\n" + \
               indent_marker * indent + "else:\n" + "\n".join(
            map(lambda x: x.to_python(indent + 1), self.elsebody))

    def to_javascript(self, indent=0):
        return indent_marker * indent + "if (" + str(self.condition) + ")   {\n" + "\n".join(
            map(lambda x: x.to_javascript(indent + 1), self.body)) + "\n" + indent_marker * indent + "} " + "else   {\n" + "\n".join(
            map(lambda x: x.to_javascript(indent + 1), self.body)) + "\n" + indent_marker * indent + "}"

    def to_codeblocks(self, indent = 0):
        return str(["if-else", indent, get_body_lines_count(self.body), get_body_lines_count(self.elsebody)]) + ',' + ''.join(self.condition.to_codeblocks(indent)) + ',' + ','.join(map
               (lambda x: x.to_codeblocks(indent + 1), self.body)) + ',' + ','.join(map
               (lambda x: x.to_codeblocks(indent + 1), self.elsebody))


# class ElseStatement:
#     def __init__(self, body, parent=None):
#         self.parent = parent
#         self.body = body
#
#     def __str__(self):
#         return "ELSE\n" + "\n".join(map(str, self.body)) + "\nEND"
#
#     def to_python(self, indent=0):
#         return indent_marker * indent + "else:\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))
#
#     def to_javascript(self, indent=0):
#         return indent_marker * indent + "else {\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body)) + "}"
#
#     def to_codeblocks(self):
#         return str(["else"])
#

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

    def to_javascript(self, indent=0):
        return str(self.left) + " " + str(self.op) + " " + str(self.right)

    def to_codeblocks(self, indent = 0):
        return str(['compare', indent, self.left, self.op, self.right])


class Random:
    def __init__(self, min, max, parent=None):
        self.parent = parent
        self.min = min
        self.max = max

    def __str__(self):
        return "random(" + str(self.min) + ", " + str(self.max) + ")"

    def to_python(self, indent=0):
        return "random.randint(" + str(self.min) + ", " + str(self.max) + ")"

    def to_javascript(self, indent=0):
        return "getRandomInt(" + str(self.min) + ", " + str(self.max) + ")"

    def to_codeblocks(self, indent = 0):
        return str(['random', indent, self.min, self.max])

class Literal:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value

    def __str__(self):
        return str(self.value)

    def to_python(self, indent=0):
        return str(self.value)

    def to_javascript(self, indent=0):
        return str(self.value)


class LoopUntil:
    def __init__(self, condition, body, parent=None):
        self.parent = parent
        self.condition = condition
        self.body = body

    def __str__(self):
        return "LOOP UNTIL " + str(self.condition) + " DO\n" + "\n".join(map(str, self.body)) + "\nEND"

    def to_python(self, indent=0):
        return indent_marker * indent + "while not " + str(self.condition) + ":\n" + "\n".join(
            map(lambda x: x.to_python(indent + 1), self.body))

    def to_javascript(self, indent=0):
        return "vidjecu sta cu pisati ovdje"

    def to_codeblocks(self, indent = 0):
        return str(['loopUntil', indent, self.condition])




class LoopTimes:
    def __init__(self, times, body, parent=None):
        self.parent = parent
        self.times = times
        self.body = body

    def __str__(self):
        return "LOOP TIMES " + str(self.times) + " DO\n" + "\n".join(map(str, self.body)) + "\nEND"

    def to_python(self, indent=0):
        return indent_marker * indent + "for i in range(" + str(self.times) + "):\n" + "\n".join(
            map(lambda x: x.to_python(indent + 1), self.body))

    # TODO: trebace automatsko generisanje slova
    def to_javascript(self, indent=0):
        return indent_marker * indent + "for (var i = 0; i < " + str(self.times) + "; ++i) {\n" + "\n".join(
            map(lambda x: x.to_javascript(indent + 1), self.body)) + "\n" + indent_marker * indent + "}"

    def to_codeblocks(self, indent = 0):
        return str(["loopTimes", indent, self.times, get_body_lines_count(self.body)]) + ','+ ','.join(map
                (lambda x: x.to_codeblocks(indent + 1), self.body))



class LoopForever:
    def __init__(self, body, parent=None):
        self.parent = parent
        self.body = body

    def __str__(self):
        return "LOOP FOREVER DO\n" + "\n".join(map(str, self.body)) + "\nEND"

    def to_python(self, indent=0):
        return indent_marker * indent + "while True:\n" + "\n".join(map(lambda x: x.to_python(indent + 1), self.body))

    def to_javascript(self, indent=0):
        return "while (true) {\n" + "\n".join(
            map(lambda x: x.to_python(indent + 1), self.body)) + "\n" + indent_marker * indent + "}"

    def to_codeblocks(self, indent = 0):
        return str(["loopForver", indent, get_body_lines_count(self.body), map(lambda x: x.to_codeblocks(indent + 1), self.body)])


def get_body_lines_count(body):
    ret_val = len(body)
    for command in body:
        ret_val += str(command).count('\n') #- str(command).count('END')
    return ret_val

# a = ["ovo je moj novi tekst \n i on bi trebalo da \n ima 3 nova reda", 'jedan red']
# print(get_body_lines_count(a))