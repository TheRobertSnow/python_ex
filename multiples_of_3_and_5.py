multiple_sum = 0
for i in range(1, 1000):
    if i%3==0:
        multiple_sum += i
    elif i%5==0:
        multiple_sum += i
print('The sum of all the multiples of 3 & 5 below 100: ', multiple_sum)
