import random
import sys

if len(sys.argv) < 2:
    print("You need to provide a file!")
    exit(1)

file = open(sys.argv[1]).read().splitlines()

settings = [
    0, # Line length
    0, # Line count
    0, # Direction
        # 0 - Right  >
        # 1 - Down   v
        # 2 - Left   <
        # 3 - Up     ^
    0, # x position
    0  # y position
]

stack = [0]

def newpos(settings):
    if settings[2] == 0:
        settings[3] += 1
        if settings[3] == settings[0]:
            settings[3] = 0
    elif settings[2] == 1:
        settings[4] += 1
        if settings[4] == settings[1]:
            settings[4] = 0
    elif settings[2] == 2:
        settings[3] -= 1
        if settings[3] == -1:
            settings[3] = settings[0] - 1
    elif settings[2] == 3:
        settings[4] -= 1
        if settings[4] == 0:
            settings[4] = settings[1]
    return settings


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

running = True

while running:
    char = program[settings[4]]
    char = char[settings[3]]
    if char == '>':
        settings[2] = 0
    elif char == 'v':
        settings[2] = 1
    elif char == '<':
        settings[2] = 2
    elif char == '^':
        settings[2] = 3
    elif char == '"':
        settings = newpos(settings)
        char = program[settings[4]]
        char = char[settings[3]]
        while char != '"':
            stack.append(ord(char))
            settings = newpos(settings)
            char = program[settings[4]]
            char = char[settings[3]]
    elif char == ':':
        stack.append(stack[-1])
    elif char == '_':
        if stack.pop() == 0:
            settings[2] = 0
        else:
            settings[2] = 2
    elif char == ',':
        print(chr(stack.pop()), end="", flush=True)
    elif char == '@':
        exit()
    elif char == '1':
        stack.append(1)
    elif char == '2':
        stack.append(2)
    elif char == '3':
        stack.append(3)
    elif char == '4':
        stack.append(4)
    elif char == '5':
        stack.append(5)
    elif char == '6':
        stack.append(6)
    elif char == '7':
        stack.append(7)
    elif char == '8':
        stack.append(8)
    elif char == '9':
        stack.append(9)
    elif char == '0':
        stack.append(0)
    elif char == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif char == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif char == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif char == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    elif char == '%':
        a = stack.pop()
        b = stack.pop()
        stack.append(b % a)
    elif char == '!':
        last = stack.pop()
        if last == 0:
            last = 1
        else:
            last = 0
        stack.append(last)
    elif char == '`':
        a = stack.pop()
        b = stack.pop()
        if b > a:
            last = 1
        else:
            last = 0
        stack.append(last)
    elif char == '|':
        last = stack.pop()
        if last == 0:
            settings[2] = 1
        else:
            settings[2] = 3
    elif char == '\\':
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
    elif char == '$':
        stack.pop()
    elif char == '.':
        print(stack.pop(), end="", flush=True)
    elif char == '#':
        settings = newpos(settings)
    elif char == 'g':
        y = stack.pop()
        x = stack.pop()
        if x >= settings[0] or y >= settings[1] or x < 0 or y < 0:
            last = 0
        else:
            getline = program[y]
            last = ord(getline[x])
        stack.append(last)
    elif char == 'p':
        y = stack.pop()
        x = stack.pop()
        v = stack.pop()
        if x < settings[0] or y < settings[1] or x >= 0 or y >= 0:
            getline = program[y]
            getline[x] = v
            program[y] = getline
    elif char == '?':
        settings[2] = random.int(0, 3)
    settings = newpos(settings)