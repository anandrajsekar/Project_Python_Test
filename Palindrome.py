Caputered_Word = input("Enter The Palindrom Word : ")

if Caputered_Word.lower() == Caputered_Word.lower()[::-1]:

    print(f"User Entered The Word : '{Caputered_Word}' and It's a Palindrome")

else:

    print(f"User Entered The Word : '{Caputered_Word}', It's not Palindrome '{Caputered_Word[::-1]}' and length of the Word '{len(Caputered_Word)}'")