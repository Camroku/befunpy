# Reverse Extension

def rtz(settings, program, stack):
    """
    Pop until you find 0, push 0, reverse all values you've found, push them.
    """
    torev = []
    val = -1
    while True:
        val = stack.pop()
        if val != 0:
            torev.append(val)
        else:
            break

    stack.append(0)
    for val in torev:
        stack.append(val)
    return (settings, program, stack)


def register(regfunc, reglist):
    regfunc(';', rtz)
