# region Init
import builtin_ints
import random
import sys
import util

if len(sys.argv) < 2:
    print("You need to provide a file!")
    exit(1)

file = open(sys.argv[1]).read().splitlines()

settings = [
    0,  # Line length
    0,  # Line count
    0,  # Direction
        # 0 - Right  >
        # 1 - Down   v
        # 2 - Left   <
        # 3 - Up     ^
    0,  # x position
    0,  # y position
]
# endregion
# region Prepare the program
for line in file:
    len_ = len(line)
    if len_ > settings[0]:
        settings[0] = len_

settings[1] = len(file)

program = [0] * settings[1]
for i in range(settings[1]):
    tmplist = [" "] * settings[0]
    program[i] = tmplist

for line in range(len(file)):
    for char in range(len(file[line])):
        program[line][char] = file[line][char]
# endregion
# region Program


class Program:
    def __init__(self, program, settings):
        self.stack = [0]
        self.program = program
        self.settings = settings
        self.handlers = {}
        self.rhandlers = {}

    def register(self, character, function):
        self.handlers[character] = function

    def reglist(self, characters, function):
        for character in characters:
            self.rhandlers[character] = function

    def handle(self, character):
        if character in self.handlers:
            self.settings, self.program, self.stack = self.handlers[character](
                self.settings, self.program, self.stack)
        elif character in self.rhandlers:
            self.settings, self.program, self.stack = self.rhandlers[character](
                self.settings, self.program, self.stack, character)
        else:
            exit("Character '" + character + "' is not supported.")

    def run(self):
        while True:
            char = self.program[settings[4]][settings[3]]
            self.handle(char)
            self.settings = util.newpos(settings)


prog = Program(program, settings)
# Load built-ins
builtin_ints.register(prog.register, prog.reglist)

# Finally, run.
prog.run()

# endregion
