# 凯撒密码
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount,ciper_direction):
    end_text = ''
    if ciper_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {ciper_direction}d text is {end_text}")

caesar(start_text=text, shift_amount=shift, ciper_direction=direction)

def encrypt(plain_text, shift_amount):
    ciper_text = ''
    for letter in plain_text:
        position = (alphabet.index(letter) + shift_amount) % len(alphabet)
        ciper_text += alphabet[position]
    print(f"The encoded text is {ciper_text}")

def decrypt(ciper_text, shift_amount):
    plain_text = ''
    for letter in ciper_text:
        position = (alphabet.index(letter) - shift_amount) % len(alphabet)
        plain_text += alphabet[position]
    print(f"The decoded text is {plain_text}")

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print('wrong')
