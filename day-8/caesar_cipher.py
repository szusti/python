alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# private note - just make 2x alphabet - easiest but not fully fool proof

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for i in range(0,len(plain_text)):
        letter_position = alphabet.index(plain_text[i])
        letter_position_shifted = alphabet[letter_position+shift_amount]
        cipher_text += letter_position_shifted
    print("Your ciphered password:", cipher_text)

# for below, I could just copy above code with a difference of - instead plus for
# letter_position_shifted = alphabet[letter_position-shift_amount]
# but let's do it differently
def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    print("Your deciphered password:", cipher_text)

if direction != "encode" and direction != "decode":
    print("Please use [encode] or [decode]")
else:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text,shift)
    if direction == "decode":
        decrypt(text,shift)
