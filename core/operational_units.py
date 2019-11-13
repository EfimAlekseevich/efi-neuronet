def summer(*args, **kwargs):
    result = sum(args) + sum(kwargs.values())
    return result


def divider(in_signal, denominator):
    result = in_signal / denominator
    return result


def multiplier(*args, **kwargs):
    result = 1
    for arg in args:
        result *= arg
    for kwarg in kwargs:
        result *= kwarg
    return result
