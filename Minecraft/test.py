# map x from range a-b to range c-d
def map_to_range(x, a, b, c, d, clamp=False):
    result = (x - a) * (d - c) / (b - a) + c
    if clamp:
        return max(min(result, d), c)
    return result
