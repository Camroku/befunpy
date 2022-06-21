# Push a new line
import util


def pnl(settings, program, stack):
    util.push(stack, 10)
    return (settings, program, stack)


def register(regfunc, reglist):
    regfunc('n', pnl)
