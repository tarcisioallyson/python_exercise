def square_digits(num):
    string_number = str(num)
    sqr_digits = ''
    for i in string_number:
        sqr_digits += str(int(i)**2)
    return int(sqr_digits)