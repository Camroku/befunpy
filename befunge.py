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

def newpos():
    global settings
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
        if settings[4] == -1:
            settings[4] = settings[1] - 1

def pop():
    global stack
    if len(stack) == 0:
        return 0
    else:
        return stack.pop()

def push(num):
    global stack
    stack.append(num)

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
    char = program[settings[4]][settings[3]]
    if char == '>':
        settings[2] = 0
    elif char == 'v':
        settings[2] = 1
    elif char == '<':
        settings[2] = 2
    elif char == '^':
        settings[2] = 3
    elif char == '"':
        newpos()
        char = program[settings[4]][settings[3]]
        while char != '"':
            push(ord(char))
            newpos()
            char = program[settings[4]][settings[3]]
    elif char == ':':
        push(stack[-1] if len(stack) > 0 else 0)
    elif char == '_':
        if pop() == 0:
            settings[2] = 0
        else:
            settings[2] = 2
    elif char == ',':
        print(chr(pop()), end="", flush=True)
    elif char == '@':
        exit()
    elif char in '1234567890':
        push(int(char))
    elif char == '+':
        a = pop()
        b = pop()
        push(a + b)
    elif char == '-':
        a = pop()
        b = pop()
        push(b - a)
    elif char == '*':
        a = pop()
        b = pop()
        push(a * b)
    elif char == '/':
        a = pop()
        b = pop()
        push(b / a)
    elif char == '%':
        a = pop()
        b = pop()
        push(b % a)
    elif char == '!':
        last = pop()
        if last == 0:
            last = 1
        else:
            last = 0
        push(last)
    elif char == '`':
        a = pop()
        b = pop()
        if b > a:
            last = 1
        else:
            last = 0
        push(last)
    elif char == '|':
        last = pop()
        if last == 0:
            settings[2] = 1
        else:
            settings[2] = 3
    elif char == '\\':
        a = pop()
        b = pop()
        push(a)
        push(b)
    elif char == '$':
        pop()
    elif char == '.':
        print(pop(), end="", flush=True)
    elif char == '#':
        newpos()
    elif char == 'g':
        y = pop()
        x = pop()
        if x >= settings[0] or y >= settings[1] or x < 0 or y < 0:
            last = 0
        else:
            getline = program[y]
            last = ord(getline[x])
        push(last)
    elif char == 'p':
        y = pop()
        x = pop()
        v = pop()
        if x < settings[0] or y < settings[1] or x >= 0 or y >= 0:
            getline = program[y]
            getline[x] = v
            program[y] = getline
    elif char == '?':
        settings[2] = random.int(0, 3)
    elif char == '&':
        push(int(input()))
    elif char == '~':
        tp = sys.stdin.read(1)
        if tp == '':
            push(0)
        else:
            push(ord(tp))
    newpos()