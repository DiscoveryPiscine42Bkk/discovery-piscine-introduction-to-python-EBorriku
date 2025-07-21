print("Enter a number less than 25")
value = int(input())
if value >= 25:
    print("Error")
else:
    for num in range(value, 26):
        print(f"Inside the loop, my variable is {num}")