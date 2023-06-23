total = 0
count = 0

while True:
    num = input("Enter a number (or -1 to stop): ")
    
    if num == "-1":
        break
    
    try:
        num = int(num)
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue
    
    total += num
    count += 1
    
average = total / count if count > 0 else 0

print("The average of the entered numbers is:", average)