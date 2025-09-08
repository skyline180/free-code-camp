text = input('Enter your message: ')
shift = input('Enter shift number: ')
shift = int(shift)

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text
encrytion = caesar(text, shift)
print('Encrypted Text: ',  encrytion)
