# Built-in instructions for BefunPY
# region Init
import util
import random
import sys
# endregion
# region Instructions


def bp_right(settings, program, stack):
    settings[2] = 0
    return (settings, program, stack)


def bp_down(settings, program, stack):
    settings[2] = 1
    return (settings, program, stack)


def bp_left(settings, program, stack):
    settings[2] = 2
    return (settings, program, stack)


def bp_up(settings, program, stack):
    settings[2] = 3
    return (settings, program, stack)


def bp_str(settings, program, stack):
    settings = util.newpos(settings)
    char = program[settings[4]][settings[3]]
    while char != '"':
        util.push(stack, ord(char))
        settings = util.newpos(settings)
        char = program[settings[4]][settings[3]]
    return (settings, program, stack)


def bp_dup(settings, program, stack):
    util.push(stack, stack[-1] if len(stack) > 0 else 0)
    return (settings, program, stack)


def bp_hif(settings, program, stack):
    if util.pop(stack) == 0:
        settings[2] = 0
    else:
        settings[2] = 2
    return (settings, program, stack)


def bp_pst(settings, program, stack):
    print(chr(util.pop(stack)), end="", flush=True)
    return (settings, program, stack)


def bp_end(settings, program, stack):
    exit(0)


def bp_int(settings, program, stack, character):
    util.push(stack, int(character))
    return (settings, program, stack)


def bp_add(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    util.push(stack, a + b)
    return (settings, program, stack)


def bp_sub(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    util.push(stack, b - a)
    return (settings, program, stack)


def bp_mul(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    util.push(stack, a * b)
    return (settings, program, stack)


def bp_div(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    util.push(stack, b / a)
    return (settings, program, stack)


def bp_mod(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    util.push(stack, b % a)
    return (settings, program, stack)


def bp_not(settings, program, stack):
    last = util.pop(stack)
    if last == 0:
        last = 1
    else:
        last = 0
    util.push(stack, last)
    return (settings, program, stack)


def bp_grt(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    if b > a:
        last = 1
    else:
        last = 0
    util.push(stack, last)
    return (settings, program, stack)


def bp_vif(settings, program, stack):
    if util.pop(stack) == 0:
        settings[2] = 1
    else:
        settings[2] = 3
    return (settings, program, stack)


def bp_swp(settings, program, stack):
    a = util.pop(stack)
    b = util.pop(stack)
    util.push(stack, a)
    util.push(stack, b)
    return (settings, program, stack)


def bp_pop(settings, program, stack):
    util.pop(stack)
    return (settings, program, stack)


def bp_pin(settings, program, stack):
    print(util.pop(stack), end="", flush=True)
    return (settings, program, stack)


def bp_brd(settings, program, stack):
    settings = util.newpos(settings)
    return (settings, program, stack)


def bp_get(settings, program, stack):
    y = util.pop(stack)
    x = util.pop(stack)
    if x >= settings[0] or y >= settings[1] or x < 0 or y < 0:
        last = 0
    else:
        getline = program[y]
        last = ord(getline[x])
    util.push(stack, last)
    return (settings, program, stack)


def bp_put(settings, program, stack):
    y = util.pop(stack)
    x = util.pop(stack)
    v = util.pop(stack)
    if x < settings[0] or y < settings[1] or x >= 0 or y >= 0:
        getline = program[y]
        getline[x] = v
        program[y] = getline
    return (settings, program, stack)


def bp_rnd(settings, program, stack):
    settings[2] = random.int(0, 3)
    return (settings, program, stack)


def bp_gin(settings, program, stack):
    util.push(stack, int(input()))
    return (settings, program, stack)


def bp_gch(settings, program, stack):
    tp = sys.stdin.read(1)
    if tp == '':
        util.push(0)
    else:
        util.push(ord(tp))
    return (settings, program, stack)


def bp_ssp(settings, program, stack):
    return (settings, program, stack)


def register(regfunc, reglist):
    regfunc('>', bp_right)
    regfunc('v', bp_down)
    regfunc('<', bp_left)
    regfunc('^', bp_up)
    regfunc('"', bp_str)
    regfunc(':', bp_dup)
    regfunc('_', bp_hif)
    regfunc(',', bp_pst)
    regfunc('@', bp_end)
    reglist(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], bp_int)
    regfunc('+', bp_add)
    regfunc('-', bp_sub)
    regfunc('*', bp_mul)
    regfunc('/', bp_div)
    regfunc('%', bp_mod)
    regfunc('!', bp_not)
    regfunc('`', bp_grt)
    regfunc('|', bp_vif)
    regfunc('\\', bp_swp)
    regfunc('$', bp_pop)
    regfunc('.', bp_pin)
    regfunc('#', bp_brd)
    regfunc('g', bp_get)
    regfunc('p', bp_put)
    regfunc('?', bp_rnd)
    regfunc('&', bp_gin)
    regfunc('~', bp_gch)
    reglist(['\t', '\n', '\v', '\f', '\r', ' '], bp_ssp)
# endregion
