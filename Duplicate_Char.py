from collections import Counter

Input_Text = input("Enter the string or word : ").lower()

print(f"\n {Input_Text} Example 1.0 : ", {char: count for char, count in Counter(Input_Text).items() if count >1})

def duplicate_char(text):

    return {char: count for char, count in Counter(text).items() if count > 1}

print(f"\n {Input_Text} Example 1.1 : {duplicate_char(Input_Text)}")

# Example Two

print(f"\n {Input_Text} Example 2.0 : " , { char: Input_Text.count(char) for char in set(Input_Text) if Input_Text.count(char) > 1})

def duplicate_chacter(text):
    
    return { char: text.count(char) for char in set(text) if text.count(char) > 1}

print(f"\n {Input_Text} Example 2.1 : {duplicate_chacter(Input_Text)} ")

# Example Three

Counts = {}

for char in Input_Text:
        
        Counts[char] = Counts.get(char, 0) + 1

print(f"\n {Input_Text} Example 3.0 : ", {char: count for char, count in Counts.items()}) #if count > 1

def duplicate_chars(text):
    
    counts = {}

    for char in text:
        
        counts[char] = counts.get(char, 0) + 1

    return { char: count for char, count in counts.items() if count > 1}

print(f"\n {Input_Text} Example 3.1 : {duplicate_chars(Input_Text)}")