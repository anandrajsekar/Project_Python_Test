# "Learning a little each day adds level up."
string_of_words = input("Enter Any String With Palindrome : ")

print(f"'{string_of_words}' Reverse The String : {string_of_words[::-1]}")

print(f"\n'{string_of_words}' Reverse The Word In The String : {" ".join((string_of_words.split())[::-1])}")

print(f"\n'{string_of_words}' Reverse Each Word In The String : {" ".join([ string_of_word[::-1] for string_of_word in string_of_words.split()])}")

Plandrome_Word = []
for string_of_word in string_of_words.split():
    if string_of_word[::-1].lower() == string_of_word.lower():
        Plandrome_Word.append(string_of_word)
        print(f"\n'{string_of_word}' is Palindrome Word")
    else:
        Plandrome_Word.append(string_of_word)
        print(f"\n'{string_of_word}' is Not Palindrome Word")
print(f"\n'{string_of_words}' Finding The Palindrome Word : {Plandrome_Word}")