# I heard you like comments
#+----------------------------------+
#|       Part ONE of Project 3      |
#+----------------------------------+
for number in range(10, 100):
    first_Digit, second_Digit = number//10, number%10   # Assign first digit of i to first_Digit and the second digit of i to second_Digit

    if (first_Digit + second_Digit)**2 == number:       # Check if the sum of first_Digit and second_Digit squared is equal to current number assigned to i
        print(number)
#+----------------------------------+
#|      Part TWO of Project 3       |
#+----------------------------------+
for number in range(1, 100):
    counter = 0

    for i in range(1, number+1):                        # For all numbers between 1 and current number assigned to "number"
        if number % i == 0:                             # If j is devisor of i
            counter += 1                                # Add one to counter(the divisors)

    if counter == 10:
        print(number)

"""
                      ,       ,
                  ___( '-$$$-' )___
                 '.__./       \__.'
    _      _     _ .-'   O   O \
  /' '--' ( ('--' '\           |
 /         ) )      \  \ _    _|
|         ( (        | / (0_._0)
|          ) )       |/   '---'
|         ( (        |
|          ) )       |
 \        ((        /
   |     /:))\     |
   |    /:((::\    |
   |   |:::):::|   |
   /   \::&&:::/   \
   \   /:U&::U:\   /
    | | | U:U | | |
    | | |     | | |
    | | \     / | |
    /_\__|   |__/_\
   |___|       |___|
"""
