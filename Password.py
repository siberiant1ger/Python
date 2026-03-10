first=input("what is your username? ")
second=input("what is your password? ")

username_length = len(first)
password_length = len(second)

hidden_username = "*" * username_length
hidden_password = "*" * password_length

print (f"your username is {hidden_username} and your password is {hidden_password}")

# SECOND WAY TO DO IT

# skrt = ""
# skrt2 = ""
# for letter in first:
#     skrt += "*"
# for letter in second:
#     skrt2 += "*"

# print (f"your usernam is {skrt} and your password is {skrt2}")