import random
import pyperclip

class Password:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.password = ""

    def password_generate(self):
        self.password = ""
        for char in range(1, 8 + 1):
            self.password += random.choice(self.letters)

        for char in range(1, 2 + 1):
            self.password += random.choice(self.symbols)

        for char in range(1, 2 + 1):
            self.password += random.choice(self.numbers)

        ''.join(random.sample(self.password, len(self.password)))

        return self.password
        pyperclip.copy(self.password)
