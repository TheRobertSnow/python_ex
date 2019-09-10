my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
if my_int == 0:
    print("The binary of", my_int, "is", my_int)
else:
    quotient = my_int
    remainder = 0
    bin_str = ''
    running = True
    while running:
        remainder = quotient % 2
        quotient = quotient // 2
        bin_str = bin_str + str(remainder)
        if quotient == 2:
            running = False
            bin_str = bin_str + '1'
        if quotient == 1:
            running = False
            bin_str = bin_str + '1'
    bin_str = bin_str[::-1]
    print("The binary of", my_int, "is", bin_str)
