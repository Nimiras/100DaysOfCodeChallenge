import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift, direction):
	caesar_text = ""
	if direction == "encode":
		for letter in text:
			if letter in alphabet:
				caesar_text += alphabet[(alphabet.index(letter)+shift) % (len(alphabet))]
			else:
				caesar_text += letter
		print(f"The encoded text is {caesar_text}")
	elif direction == "decode":
		for letter in text:
			if letter in alphabet:
				caesar_text += alphabet[(alphabet.index(letter)+26-shift) % (len(alphabet))]
			else:
				caesar_text += letter
		print(f"The decoded Text is {caesar_text}")

running = True
print(art.logo)
while running:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(text, shift % 26, direction)
	still_running = input("Do you want to encode or decode again?\n")
	if not still_running == "yes":
		running = False
		print("Bye")

#defineing the encryption function
#def encrypt(text, shift):
#	encryptedString = ""
#	for letter in text:
#		encryptedString += alphabet[(alphabet.index(letter)+shift) % (len(alphabet))]
#	print(f"The encoded text is {encryptedString}")

#defineing the decryption function
#def decode(text, shift):
#	decodedString = ""
#	for letter in text:
#		decodedString += alphabet[(alphabet.index(letter)+26-shift) % (len(alphabet))]
#	print(f"The decoded Text is {decodedString}")

#if direction == "encode":
#	encrypt(text, shift)
#elif direction == "decode":
#	decode(text, shift)
