str = " Today is 12-06-2025"

print(f"given string is given string '{str}' output: {str[::-1]}")
print(f"print the date only from the string '{str}' output:{(str.split(" ")[3])}")

# Output: given string is:5202-60-21 si yadoT

str_split = str.split()
print(f"given string is:{' '.join(str_split[::-1])}")

# Output: given string is:2025-06-12Todayis

str_split = str.split()
print(f"given string is:{' '.join(str_splits[::-1] for str_splits in str_split)}")

# Output: given string is: yadoT si 5202-60-21

print("**************************************************************");
word = "@madam@"

# word_upper = word.upper()
if word != word[::-1]:
    print(f"It is not a palindrome '{word}'")
else:
    print(f"It is a palindrome '{word}'")