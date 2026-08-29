def equilateral(sides):
    """Return True if the triangle is equilateral."""
    a, b, c = sides
    if is_triangle(sides):
        if a == b == c:
            return True
    return False


def isosceles(sides):
    """Return True if the triangle is isosceles (at least two sides equal)."""
    a, b, c = sides
    if is_triangle(sides):
        if a == b or b == c or a == c:
            return True
    return False


def scalene(sides):
    """Return True if the triangle is scalene (all sides different)."""
    a, b, c = sides
    if is_triangle(sides):
        if a != b and b != c and a != c:
            return True
    return False

def is_triangle(sides):
    """Return True if sides a, b, c can form a valid triangle."""
    a, b, c = sides
    return (a + b > c) and (b + c > a) and (a + c > b)