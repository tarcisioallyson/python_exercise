def find_next_square(sq):
    import math
    # Return the next square if sq is a square, -1 otherwise
    root = int(math.sqrt(sq))
    if root**2 == sq:
        sq += 1
        while int(math.sqrt(sq))**2 != sq:
            sq+=1
        return sq
    else:
        return -1

print(find_next_square(81))