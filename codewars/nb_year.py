def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = int(p0 + p0*(percent/100) + aug)
        year += 1
    print(p0)
    return year

print(nb_year(1000, 2, 50, 1200))