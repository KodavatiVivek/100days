from art import logo
numbers = ["0","1","2","3","4","5","6","7","8","9"]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cieser_cipher(original_text, shift_amount, encode_or_decode):
    outputtext = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter in numbers:
            shifted_position = numbers.index(letter) + shift_amount
            shifted_position %= len(numbers)
            outputtext += numbers[shifted_position]
        elif letter not in alphabet:
            outputtext += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            outputtext += alphabet[shifted_position]
    print(f"You {encode_or_decode}secret message {outputtext}")

check=True

while check:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cieser_cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)

    again=input("Want tp start again Y and N\n")
    if again.lower() =="n" :
        check = False
        print("Good Bye!")
