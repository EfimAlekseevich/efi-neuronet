import math


def simple_proportional(stability):
    return stability + 1


def simple_exponential(stability):
    return pow(math.e, stability)
