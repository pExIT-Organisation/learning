'''
Example:
    out: Hello! What is your name?
    > Artur
    out: Hello Artur, give me first number to multiply!
    >5
    out: now give me second number.
    >3
    out: Artur, your result of multiplication for 3 and 5 is 15!

IMPORTANT: Learn about f-strings in python, use them to print messages!
'''


class InputPrinter:

    def __init__(self):
        self.name = input("Hello! What is your name? ")

    def multiplier(self):

        first_number = int(input(f"Hello {self.name}, give me first number to multiply! "))
        second_number = int(input("now give me second number. "))
        print(f"{self.name}, your result of multiplication for {first_number}  and {second_number} is {first_number * second_number}.")


if __name__ == "__main__":

    InputPrinter().multiplier()
