def pop(stack):
    if len(stack) == 0:
        return 0
    else:
        return stack.pop()


def push(stack, num):
    stack.append(num)


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
        if settings[4] == -1:
            settings[4] = settings[1] - 1
    return settings
