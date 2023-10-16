#import the problem 2
import Hu_Matthew_Assign7_problem2a

A1 = 0

while True:
        pattern = input("Enter an encoding pattern, 'end' to end: ")
        if pattern == 'end':
            break

        #ask user for unput
        word = input("Enter a word to encode/decode: ")
      
        #create conditions for if certain characters are provided
        for char in pattern:
            if char == 'A':
                word = Hu_Matthew_Assign7_problem2a.add_letters(word,1)
                
                print(f"* Added 1 character: {word}")
            elif char == 'X':
                word = Hu_Matthew_Assign7_problem2a.delete_characters(word,1)
                print(f"* Deleted 1 character: {word}")
            elif char == 'F':
                word = Hu_Matthew_Assign7_problem2a.flip(word)
                print(f"* Flipped: {word}")
            elif char == 'U':
                word = Hu_Matthew_Assign7_problem2a.ascii_shift(word,1)
                print(f"* ASCII shifted up: {word}")
            elif char == 'D':
                word = Hu_Matthew_Assign7_problem2a.ascii_shift(word,-1)
                print(f"* ASCII shifted down: {word}")   
            elif char == 'L':
                word = Hu_Matthew_Assign7_problem2a.shift_left(word)
                print(f"* Shifted left: {word}")
            elif char == 'R':
                word = Hu_Matthew_Assign7_problem2a.shift_right(word)
                print(f"* Shifted right: {word}")
            else:
                print(f"Unrecognized command: {char}")
        print()
