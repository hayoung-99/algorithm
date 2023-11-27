def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(w,h):
    if w == h:
        return w * w - w
    
    gcd = GCD(w, h)
    unit_w, unit_h = w / gcd, h / gcd
    units = (unit_w + unit_h - 1) * gcd
    
    return w * h - units
    