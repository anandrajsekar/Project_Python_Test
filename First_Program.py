print("**************************************************************");
print("My List Program in Python is working fine");
print("**************************************************************");

my_word = ['usa','mexico','germany', 'france','ethiopia']

print(my_word[2:]);
print(my_word[-3:]);
print(my_word[2:10]);

my_word = ['usa','mexico','germany', 'france','ethiopia']

print(len(my_word));
print(my_word[0]);
print(my_word[1]);
print(my_word[2]);
print(my_word[3]);
print(my_word[4]);
# print(my_word[5]); IndexError: list index out of range

print("**************************************************************");

print("My Dictionaries Program in Python is working fine");

print("**************************************************************");
MY_DICT = {'Mike':32, 'Tom':25}
print(f"Mike is {MY_DICT['Mike']} years old and Tom is {MY_DICT.get('Tom')} years old");

MY_DICT = {}
MY_DICT['Mike'] = 35
MY_DICT['Tom'] = 27
print(f"Mike is {MY_DICT['Mike']} years old and Tom is {MY_DICT.get('Tom')} years old");

MY_DICT = dict(Mike=37, Tom=29)
print(f"Mike is {MY_DICT['Mike']} years old and Tom is {MY_DICT.get('Tom')} years old");


print("**************************************************************");

print("Exception Handling in Python is working fine");

print("**************************************************************");

# try: 
       
#        a = 10 / 0,
#        print(b)
       

# except ZeroDivisionError:
#          print("Error Happened due to Zero Division")
#          raise ZeroDivisionError("Unable to divide by zero in this program")

# except NameError:
#          print("Error Happened due to Name Error")
#          raise NameError("Variable is not defined")

# except (ZeroDivisionError, Exception) as e:
#          print(ZeroDivisionError);
#          print(f"Error Happened due to {e}");

print("**************************************************************");

print("Functions in Python is working fine");

print("**************************************************************");



def add_number(a, b):
    return a + b

result = add_number(10, 2)
print(f"The result of addition is {result}");


def sale_tax(states):

    List_Of_States = ['California', 'Texas', 'Florida', 'New York', 'Illinois']

    if states in List_Of_States:
        return True
    else: 
        return False

state_entered = 'California'
print(f"Is there any sales tax in {state_entered}? {sale_tax(state_entered)}");

print("**************************************************************");

print("Palindrome in Python is working fine");

print("**************************************************************");

def is_palindrome(s):

    if s == s[::-1]:
        return True
    else:
        return False

s = "level1" 
print(f"Is the entered string '{s}' a palindrome? {is_palindrome(s)}");

print("**************************************************************");

print("reverse word in the string in Python is working fine");

print("**************************************************************");

def reverse_word_string(s):
    words = s.split()
    return ' '.join([words_string[::-1] for words_string in words])

s = "Hi Anandraj How are you doing today?"
print(f"The reversed word in the string of '{s}' is '{reverse_word_string(s)}'");

print("**************************************************************");

print("reverse whole string in Python is working fine");

print("**************************************************************");

def reverse_string(s):
        return s[::-1]

s = "Hi Anandraj How are you doing today?"
print(f"The reversed entire string of '{s}' is '{reverse_string(s)}'");

print("**************************************************************");

print("reverse string in Python is working fine");

print("**************************************************************");

def reverse_string(s):
        words = s.split()
        return ' '.join(words[::-1])

s = "Hi Anandraj How are you doing today ? "
print(f"The reversed string of '{s}' is '{reverse_string(s)}'");
print(f"The length of the string '{s}' is '{len(s.split())}'");