top_num = int(input("Upper number for the range: ")) # Do not change this line

for number in range(1, top_num):
    da_sum=0
    for i in range(1, number):
        if number%i==0:
            da_sum += i
    if da_sum == number:
        print(da_sum)
