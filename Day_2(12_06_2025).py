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

print("**************************************************************");

str = "My ip address is 192.168.1.1 and my subnet mask is 255.255.255.0"

def extract_ip_addresses(input_string):
    import re
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, input_string)
    return ip_addresses

ip_addresses = extract_ip_addresses(str)
print(f"Extracted IP addresses: {ip_addresses}")