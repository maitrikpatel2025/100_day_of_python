alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#def encrypt(plain_text,shift_number):
#   cipher_text = ""
#   for letter in plain_text:
#       if letter in alphabet:
#           index_number = alphabet.index(letter)
#           new_number = index_number + shift_number
#           cipher_text += alphabet[new_number]

#    print(f"The encode text '{cipher_text}' ")

# def decrypt(plain_text,shift_number):
#   cipher_text = ""
#   for letter in plain_text:
#       if letter in alphabet:
#           index_number = alphabet.index(letter)
#           new_number = index_number - shift_number
#           cipher_text += alphabet[new_number]

#    print(f"The decode text '{cipher_text}' ")

def caesar(plain_text,shift_number,type_dec):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            index_number = alphabet.index(letter)
            if type_dec.lower() == "encode":
                new_number = index_number + shift_number
            elif type_dec.lower() == "decode":
                new_number = index_number - shift_number
            cipher_text += alphabet[new_number]

    print(f"The {type_dec} text '{cipher_text}' ")

caesar(text,shift,direction)