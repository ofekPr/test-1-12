import sys

Y_END = 'y'
Y_END_SUFFIX = 'ies'
DOUBLE_END = ['sh', 'ch']
SINGLE_END = ['x', 's', 'o', 'z']
SPECIAL_SUFFIX = 'es'
REGULAR_SUFFIX = 's'


def make_3sg_form(verb):
    if verb.endswith(Y_END):
        verb = verb[:-len(Y_END)] + Y_END_SUFFIX
    elif verb[-2:] in DOUBLE_END:
        verb += SPECIAL_SUFFIX
    elif verb[-1:] in SINGLE_END:
        verb += SPECIAL_SUFFIX
    else:
        verb += REGULAR_SUFFIX

    return verb


def make_char_twice(s):
    return ''.join(2 * char for char in s)


print(make_3sg_form("eat"))
assert make_3sg_form("eat") == "eats", "eat -> eats"

print(make_3sg_form("catch"))
assert make_3sg_form("catch") == "catches", "catch -> catches"

print(make_3sg_form("fly"))
assert make_3sg_form("fly") == "flies", "fly -> flies"

print(make_3sg_form("die"))
assert make_3sg_form("die") == "dies", "die -> dies"

print(make_char_twice("I LOVE FOOD"))
