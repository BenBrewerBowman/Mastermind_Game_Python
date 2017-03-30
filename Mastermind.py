import random

print("----MASTERMIND----")
print("Guess the 4 numbers in as few tries as possible (a '*' means the number is in the correct position).")

four_digit_number = [0,0,0,0]

for i in range(len(four_digit_number)):
    four_digit_number[i] = random.randint(0,6)

# print(four_digit_number)
output_count = 0
while output_count < 4:
    guess = input("Your guess: ")
    while len(guess) != 4 :
        print("Error, please enter a four digit number")
        guess = input("Your guess: ")

    guess_int = [0,0,0,0]
    for i in range(len(guess)):
        guess_int[i] = int(guess[i])

    output = ["_","_","_","_"]
    for i in range(len(four_digit_number)):
        if (four_digit_number[i] == guess_int[i]) :
            output[i] = "*"

    output_count = 0
    for i in range(len(output)):
        if (output[i] == "*"):
            output_count += 1

    print("*" * output_count)

if output_count == 4:
    print("Wow, you are amazing! You completed the sequence. You are a mastermind!!!")
