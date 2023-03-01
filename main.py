# def greetings(name):  # name is parameter
#     print(f"Hello {name.title()}")
#
#
# greetings("Arshad")  # Arshad is argument from call function to function
#
#
# def learning(subject):
#     print(f"I am learning {subject} in A.I ")
#
#
# learning("Python")
#
#
# def fav_book(book):
#     print(f"My favorite book is auther Collen Hoover's {book.title()}. ")
#
# fav_book("It End With Us..")

# Keyword arguments in functions
# def intro(fname, lastname, job="Unemployed"):
#     print(f"Hello My name is {fname} {lastname} and i am {job}")
#
#
# intro(fname="Arshad", lastname="Mahar", job="Software developer")


# Return value in function python.
# The return statement takes value from inside the function and return value to that line from function was called.
def full_name(first_name,last_name, middle_name='' ):
    if middle_name:
        name = f"{first_name} {middle_name} {last_name}"
    else:
        name = f"{first_name} {last_name}"
    return name.title()

fullName = full_name("Arshad", "Mahar")
print(fullName)

fullName = full_name("Arshad","Ali", "Mahar")
print(fullName)
# optional argument by setting default value to empty