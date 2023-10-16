# function: horizontal_line
# input: a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output: returns the generated pattern (string)


def horizontal_line(width,char):
 return width*char + "\n"



# function: vertical_line
# input: a shift value and a height value (both integers) and a single character (string)
# processing: generates a single vertical line of the desired height. the line is
# offset from the left side of the screen using the shift value
# output: returns the generated pattern (string)


def vertical_line(shift,height,char):
 pattern = ""
 for i in range(height):
    pattern += shift*" " + char + "\n"
 return pattern


# function: two_vertical_lines
# input: a width value and a height value (both integers) and a single character (string)
# processing: generates two vertical lines. the first line is along the left side of
# the screen. the second line is offset using the "width" value supplied
# output: returns the generated pattern (string)


def two_vertical_lines(width,height,char):
 pattern = ""
 for i in range(height):
    pattern += char + " "*(width-2) + char + "\n"
 return pattern



# function: number_1
# input: a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
# using the supplied width value
# output: returns the generated pattern (string)


def number_0(width, character):
    pattern = (
        horizontal_line(width, character),
        two_vertical_lines(width, 3, character),
        horizontal_line(width, character)
    )
    return ''.join(pattern)

#creating the patterns for the numbers

def number_1(width, character):
    pattern = vertical_line(width-1, 5, character)
    return pattern


def number_2(width, character):
    pattern = (
         horizontal_line(width, character),
        vertical_line(width-1, 1, character),
        horizontal_line(width, character),
        vertical_line(0, 1, character),
        horizontal_line(width, character),
        )
        
    
    return ''.join(pattern)



def number_3(width, character):
    pattern = (
        horizontal_line(width, character),
        vertical_line(width-1, 1, character),
        horizontal_line(width, character),
        vertical_line(width-1, 1, character),
        horizontal_line(width, character),
    )
    return ''.join(pattern)


def number_4(width, character):
    pattern = (
        two_vertical_lines(width, 2, character),
        horizontal_line(width, character),
        vertical_line(width-1, 2, character),
        
    )

    return ''.join(pattern)


def number_5(width, character):
    pattern = (
        horizontal_line(width, character),
        vertical_line(0, 1, character),
        horizontal_line(width, character),
        vertical_line(width-1, 1, character),
        horizontal_line(width, character)
    )
    return ''.join(pattern)


def number_6(width, character):
    pattern = (
        horizontal_line(width, character),
        vertical_line(0, 1, character),
        horizontal_line(width, character),
        two_vertical_lines(width, 1, character),
        horizontal_line(width, character)
    )
    return ''.join(pattern)


def number_7(width, character):
    pattern = (
        horizontal_line(width, character),
        vertical_line(width-1, 4, character),
   
    )
    return ''.join(pattern)


def number_8(width, character):
    pattern = (
        horizontal_line(width, character),
        two_vertical_lines(width, 1, character),
        horizontal_line(width, character),
        two_vertical_lines(width, 1, character),
        horizontal_line(width, character)
    )
    return ''.join(pattern)


def number_9(width, character):
    pattern = (
        horizontal_line(width, character),
        two_vertical_lines(width, 1, character),
        horizontal_line(width, character),
        vertical_line(width-1, 2, character),
        
    )
    return ''.join(pattern)

#finding the numbers width 

def print_number(num, width, character):
    numbers = {
        0: number_0,
        1: number_1,
        2: number_2,
        3: number_3,
        4: number_4,
        5: number_5,
        6: number_6,
        7: number_7,
        8: number_8,
        9: number_9
    }
    pattern = numbers[num](width, character)
    print(pattern)

# subtraction and addition

def plus(width, character):
    mid = width // 2
    pattern = ''
    
    if width % 2 == 0:
         pattern += ' ' * (mid - 1) + character * 2 + ' ' * (mid - 1)
         pattern += '\n'

         pattern += ' ' * (mid - 1) + character * 2 + ' ' * (mid - 1)
         pattern += '\n'
    else:
       
         pattern += ' ' * (mid ) + character  + ' ' * (mid)
         pattern += '\n'

         pattern += ' ' * (mid ) + character  + ' ' * (mid )
         pattern += '\n'
        
   
   
    
    pattern += character * width
    pattern += '\n'
    

   
    
    if width % 2 == 0:
         pattern += ' ' * (mid - 1) + character * 2 + ' ' * (mid - 1)
         pattern += '\n'

         pattern += ' ' * (mid - 1) + character * 2 + ' ' * (mid - 1)
         pattern += '\n'
    else:
       
         pattern += ' ' * (mid ) + character  + ' ' * (mid )
         pattern += '\n'

         pattern += ' ' * (mid ) + character  + ' ' * (mid )
         pattern += '\n'
      
     
        
    return pattern

def minus(width, char):
    pattern = ''
    for i in range(width):
        if i == width // 2:
            pattern += char * width
        else:
            pattern += ' ' * width + '\n'
    return pattern

   

def check_answer(number1, number2, answer, operator):
    if operator == "+":
        return number1 + number2 == answer
    elif operator == "-":
        return number1 - number2 == answer
    else:
        return False
