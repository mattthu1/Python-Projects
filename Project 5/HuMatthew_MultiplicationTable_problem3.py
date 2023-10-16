lowest = int(input('Lowest number: '))
while lowest < 0:
    print('Lowest number must be 0 or greater')
    lowest = int(input('Lowest number: -5'))

highest = int(input('Highest number: '))
while highest <= lowest:
    print('Highest number must be larger than lowest number!')
    highest = int(input('Highest number: '))

# Calculate the maximum width of the numbers in the multiplication table
max_width = len(str(highest**2))

# Define column width for the header
header_width = max_width + 1

# Print the  header
print("+" ," "*header_width, end="")
for i in range(lowest, highest+1):
    print(f"{i:>{header_width}}", end="")
print("\n" + "-"*header_width*(highest-lowest+2)+'--')

# Print the table
for i in range(lowest, highest+1):
    print(f"{i:>{header_width}} |", end="")
    for j in range(lowest, highest+1):
        print(f"{i*j:>{header_width}}", end="")
    print()
