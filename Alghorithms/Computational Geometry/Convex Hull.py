from functools import cmp_to_key


def orientation(p1: tuple, p2: tuple, p3: tuple) -> int:
    """
    Finds the orientation of the ordered triplet (p1, p2, p3).
    
    Based on the formula:
    D = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    
    Returns:
    +ve : Counter-Clockwise (CCW)
    -ve : Clockwise (CW)
    0 : Colinear
    """

    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def dist_sq(p1: tuple, p2: tuple) -> int:
    """Calculates the square of the distance between two points."""

    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def graham_scan(points) -> list:
    """Computes the Convex Hull of a set of points using the Graham Scan algorithm."""
    
    n = len(points)
    
    if n < 3:
        return []

    # Find the anchor point
    p0 = min(points, key = lambda point: (point[1], point[0]))

    def compare(p1, p2):
        """Custom comparison function for sorting."""

        o = orientation(p0, p1, p2)
        
        if o == 0:
            return dist_sq(p0, p1) - dist_sq(p0, p2)
        
        return -1 if o > 0 else 1

    sorted_points = sorted(points, key = cmp_to_key(compare))
    filtered_points = [sorted_points[0]]
    
    i = 1
    while i < n:
        while i < n - 1 and orientation(p0, sorted_points[i], sorted_points[i+1]) == 0:
            i += 1
        
        filtered_points.append(sorted_points[i])
        i += 1

    if len(filtered_points) < 3:
        return []

    stack = [filtered_points[0], filtered_points[1], filtered_points[2]]

    for i in range(3, len(filtered_points)):
        next_point = filtered_points[i]
        
        # Keep removing while points creates a clockwise (or colinear) turn
        while len(stack) > 1 and orientation(stack[-2], stack[-1], next_point) <= 0: # +ve: CCW
            stack.pop()
        
        stack.append(next_point)

    return stack


P0 = (0, 0)
P1 = (1, 1)
P2 = (4, 3)
P3 = (3, 2)
P4 = (5, 6)
P5 = (2, 5)
points = [P0, P1, P2, P3, P4, P5]

hull = graham_scan(points)

print("Points provided:", points)
print("---")
print("Convex Hull (Final Stack):", hull)