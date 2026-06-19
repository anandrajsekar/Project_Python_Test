string_of_words = "Learning a little each day adds up. Research shows that students who make learning a habit are more likely to reach their goals. Set time aside to learn and get reminders using your learning scheduler."

Collection_Of_Words = []

for word in string_of_words.split():
    
    if len(word) <=3:
    
        Collection_Of_Words.append(word)
    
        print(word)

print(Collection_Of_Words)    

# Example: One

My_Cars = ['BMW', 'Sokada', 'YBD', 'Maruthi']

for Car in My_Cars:
    
    print(f"My Car : '{Car}'")

# Example: Two

for Number_List in range( 0 , 101):
    
    if Number_List ==0:

        print("Zero Non Divisible!!")

    elif Number_List%2 != 0:
        
        print("Number Is: {}".format(Number_List))
    
    else:

        print("It's an Even Number")