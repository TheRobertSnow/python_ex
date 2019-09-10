n = int(input("Input a natural number: ")) # Do not change this line
prime = True
counter = 1
n2 = 0
# Fill in the missing code below
while counter <= n:
    n2 = n%counter
    if n2 == 0:
        if counter>1 and counter<n:
            prime = False

    counter+=1
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")
