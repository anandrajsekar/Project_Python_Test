print("")
print("**************************************************************");
print("")
print("Example one: find the largest number among three numbers a, b and c")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a < b:

    print(f"a = {a} is less than b = {b}")

elif (a > b) and (a < c):

    print(f"a = {a} is greater than b = {b} but less than c = {c}")

elif a == b == c:

    print(f"a = {a} , b = {b} and c = {c} are all same")

else:

    print(f"a = {a} is equal to b = {b}")


print("")
print("**************************************************************");
print("")
print("Example Three: Find the element from the two lists and check if it is in the list or not")


shows_list = [show.lower() for show in ["Breaking Bad", "Game of Thrones", "Stranger Things", "The Crown", "The Mandalorian", "God"]]
movies_list = [movie.lower() for movie in ["Inception", "The Dark Knight", "Interstellar", "The Prestige", "Dunkirk", "God"]]
User_Input = input("Enter The name of the show or movie to check if it is in the list: ").lower()

if (User_Input in shows_list) and (User_Input not in movies_list):

    print(f"list of shows: {shows_list} and list of movies: {movies_list} == ['{User_Input}'] is in the shows list but not in the movies list")

elif (User_Input not in shows_list) and (User_Input in movies_list):

    print(f"list of shows: {shows_list} and list of movies: {movies_list} == ['{User_Input}'] is in the movies list but not in the shows list")

elif (User_Input in shows_list) and (User_Input in movies_list):

    print(f"list of shows: {shows_list} and list of movies: {movies_list} == ['{User_Input}'] is in both shows and movies lists")

else:

    print(f"list of shows: {shows_list} and list of movies: {movies_list} == ['{User_Input}'] is not in the shows or movies list")

print("")
print("**************************************************************");
print("")
print("Example three: Find the sales tax list of a country")


Country_In_Sales_Tax = [Country.lower() for Country in ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "INDIA"]]

Country_In_Sales_Tax_Other = [Country_Other.lower() for Country_Other in ["Malaysia", "SINGAPORE", "Indonesia", "Philippines", "ThaIland"]]

Added_Countery_To_Sales_List = [Added_Country.lower() for Added_Country in [input("Enter a country name to add to the sales tax list: ")]]

Country_In_Sales_Tax_After_Addition = Country_In_Sales_Tax + Added_Countery_To_Sales_List + Country_In_Sales_Tax_Other

My_Choice = input("Enter The country name to check if it is in the sales tax list: ").lower()


if(My_Choice in Country_In_Sales_Tax) and (My_Choice not in Country_In_Sales_Tax_Other) and (My_Choice not in Country_In_Sales_Tax_After_Addition):

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax} == {My_Choice} is in the sale tax list but not in the other sale tax list or after added into the list of sales tax")

elif (My_Choice in Country_In_Sales_Tax_Other) and (My_Choice not in Country_In_Sales_Tax) and (My_Choice not in Country_In_Sales_Tax_After_Addition):

    print(f"list of country in Other Sales Tax: {Country_In_Sales_Tax_Other} == {My_Choice} is in the Other sale tax list but not in the sale tax list or after added into the list of sales tax")

elif (My_Choice in Country_In_Sales_Tax_After_Addition) and (My_Choice not in Country_In_Sales_Tax) and (My_Choice not in Country_In_Sales_Tax_Other):

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax_After_Addition} == {My_Choice} is in the tax list after added into the list but not in the sale tax list or in the other sale tax list")

elif (My_Choice in Country_In_Sales_Tax) and (My_Choice in Country_In_Sales_Tax_Other) and (My_Choice in Country_In_Sales_Tax_After_Addition):

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax} , list of country in Other Sales Tax: {Country_In_Sales_Tax_Other} and after aadded country: {Country_In_Sales_Tax_After_Addition}== {My_Choice} is in the sale tax list and in the other sale tax list and after added into the list of sales tax")

elif (My_Choice in Country_In_Sales_Tax) and (My_Choice in Country_In_Sales_Tax_Other) and (My_Choice not in Country_In_Sales_Tax_After_Addition):

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax} , list of country in Other Sales Tax: {Country_In_Sales_Tax_Other} and after aadded country: {Country_In_Sales_Tax_After_Addition}== {My_Choice} is in the sale tax list and in the other sale tax list but not after added into the list of sales tax")

elif (My_Choice in Country_In_Sales_Tax) and (My_Choice not in Country_In_Sales_Tax_Other) and (My_Choice in Country_In_Sales_Tax_After_Addition):

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax} , list of country in Other Sales Tax: {Country_In_Sales_Tax_Other} and after aadded country: {Country_In_Sales_Tax_After_Addition}== {My_Choice} is in the sale tax list and after added into the list of sales tax but not in the other sale tax list")

elif (My_Choice not in Country_In_Sales_Tax) and (My_Choice in Country_In_Sales_Tax_Other) and (My_Choice in Country_In_Sales_Tax_After_Addition):

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax} , list of country in Other Sales Tax: {Country_In_Sales_Tax_Other} and after aadded country: {Country_In_Sales_Tax_After_Addition}== {My_Choice} is in the other sale tax list and after added into the list of sales tax but not in the sale tax list")

else:

    print(f"list of country in Sales Tax: {Country_In_Sales_Tax} , list of country in Other Sales Tax: {Country_In_Sales_Tax_Other} and after aadded country: {Country_In_Sales_Tax_After_Addition}== {My_Choice} is not the sale tax list or in the other sale tax list or after added into the list of sales tax")