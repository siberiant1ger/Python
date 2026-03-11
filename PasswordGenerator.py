import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

lettercount = int(input("how many letters do you want in your password? : \n"))
numbercount = int(input("how many numbers do you want in your password? : \n"))
symbolcount = int(input ("how many symbols do you want in your password? : \n"))

for char in range(lettercount):
    password.append(random.choice(letters))
for num in range(numbercount):
    password.append(random.choice(numbers)) 
for sym in range(symbolcount):
    password.append(random.choice(symbols))

print (password)


password_list = "".join(password)
print(password_list)