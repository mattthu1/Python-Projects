import re

def cleanup_string(data):
    # Convert the string to lowercase
    cleaned_data = data.lower()
    # Remove all non-alphanumeric characters using regular expressions
    cleaned_data = re.sub(r"[^a-z0-9]", "", cleaned_data)
    return cleaned_data

# TEST CODE
test1 = cleanup_string("Hello World! This is a simple test of this function!")
print(test1)
# Output: helloworldthisisasimpletestofthisfunction

test2 = cleanup_string("ABC123abc this is Another TEST!!!#@@")
print(test2)
# Output: abc123abcthisisanothertest


phrase = input("Enter a phrase: ")
phrase = cleanup_string(phrase)  # Clean up the input phrase

# Create an empty dictionary to store the count of each character
char_count = {}

# Loop through each character in the phrase
for char in phrase:
    # If the character is not already in the dictionary, add it with a count of 1
    if char not in char_count:
        char_count[char] = 1
    # If the character is already in the dictionary, increment its count by 1
    else:
        char_count[char] += 1

# Sort the keys in the dictionary by their ASCII value
sorted_keys = sorted(char_count.keys())

# Print the report in ascending order by ASCII value
print("Report in ascending order by ASCII value:")
print(len(phrase)) #total number of letters and numbers
for key in sorted_keys:
    print(key, char_count[key])
