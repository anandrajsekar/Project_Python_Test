User_Name = input("Enter Your Name : ")
User_Age = input("Enter Your Age : ")

Thaeter_Name = input("Enter Theater Name You Want To Watch Movie : ")
Movie_Name = input("Enter Movie Name You Want To Watch : ")

User_Age_Limit = 18

if float(User_Age) >= User_Age_Limit:

    print("Welcome '{}' To '{}' Theater '{}' Movie Is Available For You To Watch Your Age Is '{}' Perfect For Watching This Movie The Age Limit is '{}'".format(User_Name, Thaeter_Name, Movie_Name, User_Age, User_Age_Limit))

else:

    print("Welcome '{}' To '{}' Theater '{}' Movie Is Not Suitable For You Age '{}' To Watch This Movie The Age Limit is '{}'".format(User_Name, Thaeter_Name, Movie_Name, User_Age, User_Age_Limit))