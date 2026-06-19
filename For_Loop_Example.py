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