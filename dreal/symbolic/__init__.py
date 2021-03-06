from dreal.symbolic._dreal_symbolic_py import *
from functools import reduce

# Explicitly import private symbols
from dreal.symbolic._dreal_symbolic_py import __logical_and, __logical_or


def logical_and(*formulas):
    assert len(formulas) >= 1, "Must supply at least one operand"
    return reduce(__logical_and, formulas)


def logical_or(*formulas):
    assert len(formulas) >= 1, "Must supply at least one operand"
    return reduce(__logical_or, formulas)
