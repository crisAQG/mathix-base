def lerp(a, b, t):
    return a + (b - a) * t

def inverse_lerp(a, b, value):
    if a == b:
        return 0
    return (value - a) / (b - a)

def remap(in_min, in_max, out_min, out_max, value):
    t = inverse_lerp(in_min, in_max, value)
    return lerp(out_min, out_max, t)

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def ease_in_quad(t):
    return t * t

def ease_out_quad(t):
    return t * (2 - t)

def ease_in_out_quad(t):
    return 2*t*t if t < 0.5 else -1 + (4 - 2*t)*t

def ease_in_cubic(t):
    return t**3

def ease_out_cubic(t):
    return (t - 1)**3 + 1

def ease_in_out_cubic(t):
    return 4*t**3 if t < 0.5 else (t - 1)*(2*t - 2)**2 + 1
