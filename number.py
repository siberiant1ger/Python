total = 0 
#this is the beggining of the total, it is 0 because we haven't added any numbers yet

count = int(input("How many numbers do you want to add? "))

while count != 0:
    num = int(input(f"Enter number : "))
    total += num
    count -= 1

print(f"Calculating the total... {total}")

