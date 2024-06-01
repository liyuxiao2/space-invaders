# collision.py

def check_collision(obj1, obj2):
    # Extract coordinates and dimensions of the objects
    x1, y1, w1, h1 = obj1.x, obj1.y, obj1.width, obj1.height
    x2, y2, w2, h2 = obj2.x, obj2.y, obj2.width, obj2.height

    # Check for collision between the two objects
    if (x1 < x2 + w2 and x1 + w1 > x2 and
        y1 < y2 + h2 and y1 + h1 > y2):
        return True  # Collision detected
    else:
        return False  # No collision detected