
def isNumber(a):
    try:
        float(repr(a))
        return True
    except:
        return False


def calculateQuadraticEquationRoots(a, b, c):
    if not a or not b or not c:
        return None, None

    if not isNumber(a) or not isNumber(b) or not isNumber(c):
        return None, None

    if a == 0:
        return None, None

    delta = b * b - 4 * a * c
    doubleA = 2 * a
    realBase = -b / doubleA

    if delta > 0: # two difrent roots
        dv = delta**0.5 / doubleA
        x1 = realBase + dv
        x2 = realBase - dv
        return x1, x2

    if delta == 0: # tween roots
        return realBase, realBase

    # if delta < 0: complex roots
    dv = (-delta)**0.5 / doubleA
    x1 = [realBase, dv]
    x2 = [realBase, -dv]
    return x1, x2

