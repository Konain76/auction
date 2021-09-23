alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar( word, shift_amount, path):
    message = ""
    if path == "decode":
        shift_amount *= -1
    for x in word:
        if x in alphabet:
            a = alphabet.index(x)
            position = a+shift_amount
            message += alphabet[position]
        else:
            message += x
    print(f"Here is the {path}d result: {message}")
# if shift > 26:
#     shift = shift % 2



should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again.Otherwise type 'no'.\n ")
    if restart == 'no':
        should_end = True
        print("Good bye")