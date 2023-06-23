string = "hello world"
blank_string = "" 

for char in range(len(string)):
    if char % 2 == 1:
        blank_string += string[char].lower()
    else:
        blank_string += string[char].upper() 

print(blank_string)


string_2 = "I am learning to code"
new_string_2 = []
string_divided = string_2.split()

for i in range(len(string_divided)):
    if i % 2 == 1:
        new_string_2.append(string_divided[i].lower())
    else:
        new_string_2.append(string_divided[i].upper())

print(" ".join(new_string_2))