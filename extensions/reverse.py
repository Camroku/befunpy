# Reverse Extension
import util


def rtz(settings, program, stack):
    """
    Pop until you find 0, push 0, reverse all values you've found, push them.
    """
    torev = []
    val = -1
    while True:
        val = util.pop(stack)
        if val != 0:
            util.push(torev, val)
        else:
            break

    util.push(stack, 0)
    for val in torev:
        util.push(stack, val)
    return (settings, program, stack)


def register(regfunc, reglist):
    regfunc(';', rtz)
