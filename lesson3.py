number = int(input("Please enter an even number: "))

if number % 2 == 0:
    print("Thank you")
else:
    print("This is not an even number")



age = int(input("Enter your age: "))

if age <5 or age >59:
    print("Ticket is free for you")

elif age < 17:
    print("Ticket will be 10.000")

elif age >18:
    print("Ticket will be 20.000")

else:
    print("You need to pay for the ticket")


n = int(input("Enter a number: "))
next_number = n + 1
print(f"{n} is followed by {next_number}")