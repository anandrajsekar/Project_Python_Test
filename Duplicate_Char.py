from collections import Counter

Input_Text = input("Enter the string or word : ").lower()

print({char: count for char, count in Counter(Input_Text).items() if count >1})

def duplicate_char(text):

    return {char: count for char, count in Counter(text).items() if count > 1}

print(f"\n {duplicate_char(Input_Text)}")