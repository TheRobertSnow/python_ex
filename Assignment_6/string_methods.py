name = input("Input a name: ")
last_name, first_name = name.split(', ')
first_initial = first_name[:1].upper()
last_name = last_name[:1].upper() + last_name[1:]
print("{}. {}".format(first_initial, last_name))
