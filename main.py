from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def user_input():
    global direction
    global text
    global shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
print(logo)    
user_input()    
def caesar(encode, plain_text, shift_amount):
    cypher_text = ''
    for letter in plain_text:
        try:
            old_index = alphabet.index(letter)
            if direction == 'encode':
                new_index = (old_index + shift_amount) % 26    
            if direction == 'decode':
                new_index = (old_index - shift_amount) % 26    
            cypher_text += alphabet[new_index]
        except ValueError:    
            cypher_text += ' '            
    if direction == 'encode':
        print(f"Your encrypted text is: {cypher_text}")  
    if direction == 'decode':
        print(f"Your decrypted text is: {cypher_text}") 
    again = input("Do you want to encrypt or decrypt something again? 'y' for yes 'n' for no:\n")
    if again == 'y':
        print(logo)
        user_input()
        caesar(encode=direction, plain_text=text, shift_amount=shift)
            
caesar(encode=direction, plain_text=text, shift_amount=shift)
