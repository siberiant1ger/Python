# first = input("what is your username? ")
# second = input("what is your password? ")

# username_length = len(first)
# password_length = len(second)

# hidden_username = "*" * username_length
# hidden_password = "*" * password_length

# print(
#     f"your username is {hidden_username} and your password is {hidden_password}")

# SECOND WAY TO DO IT

# username_length = ""
# password_length = ""
# for letter in first:
#     skrt += "*"
# for letter in second:
#     skrt2 += "*"

# print (f"your usernam is {skrt} and your password is {skrt2}")

# is_friend = False
# canmessage = "message allowed" if is_friend else "not allowed"
# print (canmessage)

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#     print("you are a master magician")

# if is_magician and not is_expert:
#     print('at least you\'re magician')

# if not is_magician:
#     print('you need magic dildo')

# for item in 'Zero to Mastery'
#     print('item')

# user = {
#     'name' : 'golem',
#     'age' : 500,
#     'can_swim' : False,
# }

# for key,value in user.items():
#     print(key, value)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)
# total = 0
# my_list = [1,2,3,4,5,6,7,8,9,10]
# for char in my_list:
#     total += char

# print(total)

# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f"index of 50 is {i}")

duplicates = []
some_list = [ 'a', 'b', 'c', 'd', 'b', 'd']
for char in some_list:
    if some_list.count(char) > 1:
        duplicates.append(char)

print(duplicates)

def say_chunga():
    print('heloooooooooooo')

say_chunga()
        