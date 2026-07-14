

# My_Data = True

# while My_Data:
#     print("Say Hi")

# ip : testing concepts
# op : tes*ing concep**s

input_val = "testing concepts"
target = 't'
output = []
count = 0

for char in input_val:
    if char == target:
        output.append("*" * count if count > 0 else char)
        count += 1
    else:
        output.append(char)

result = "".join(output)
print(result)