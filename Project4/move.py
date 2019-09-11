### Declaring variables ###

RANGE_START, RANGE_STOP = 1, 11 # Declaring range constants
x, o = 'x', 'o'
characterPosition = int(input('Input a position between 1 and 10: '))
print('Character position is', characterPosition)

### Fucntions ###

def printLine(position):
    position = position
    for character in range(RANGE_START, RANGE_STOP):
        if character == position:
            print(o, end='')
        else:
            print(x, end='')

def moveCharacterLeft(position):
    position = position
    if position == 1:
        printLine(position)
        return position
    else:
        position -= 1
        printLine(position)
        return position

def moveCharacterRight(position):
    position = position
    if position == 10:
        printLine(position)
        return position
    else:
        position += 1
        printLine(position)
        return position

def waitForInput(position):    # Function that waits for user input and preformes the associated action
    position = position
    running = True              # Controller for while loop
    while running:
        user_input = input('\nInput your choice: ')
        if user_input == 'r':
            position = moveCharacterRight(position)
        elif user_input== 'l':
            position = moveCharacterLeft(position)
        else:
            running = False

def startProgram(characterPosition):     # Function that prints the
    position = characterPosition
    printLine(position)         # Print the line with the character
    print('\nl - for moving left')
    print('r - for moving right')
    print('Any other letter for quitting', end='')
    waitForInput(position)      # Call waitForInput() function


# Call startProgram()
startProgram(characterPosition)
