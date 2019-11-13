from samples import constants


def stable(*args, **kwargs):
    return kwargs['stability']


def dynamic_limited(*args, **kwargs):
    if not kwargs['limiter']:
        kwargs['limiter'] = constants.default_limiter
    return kwargs['stability'] / (kwargs['delta'] + kwargs['limiter'])
