# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")

# result = len(name)    length of string(include space)
# result = name.find("o")    only first char
# result = name.rfind('o')    r for reverse, only find last
# result = name.rfind('q')    No result = -1
# result = name.capitalize()    first char upper
# result = name.upper()    all upper
# result = name.lower()    all lower
# result = name.isdigit()    only digit == true
# result = name.isalpha()    only alpha == true
# result = phone_number.count('-')    count how many specific char
# result = phone_number.replace('-', '')    Ex. replace "-" to nothing

# print(result)
#  print(help(str))




# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")

elif not username.find(' ') == -1:
    print("Your username can't contain spaces")

# elif not username.isdigit() == -1:
#     print("Your username can't contain digits")

elif not username.isalpha():
    print("Your username can't contain numbers")

else:
    print(f"Welcome {username}")