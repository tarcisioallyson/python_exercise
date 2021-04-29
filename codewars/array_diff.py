def array_diff(a, b):
    c = []
    for item in a:
        if item not in b:
            c.append(item)
    return c

a = [1,2,3,4,5]
b = [1,2]

print(array_diff(a,b))