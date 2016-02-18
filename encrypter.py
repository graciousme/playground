
encryption_dict = {}
decryption_dict = {}
value = 0

alphabet = "abcdefghijklmnopqrstuvwxyz "

for character in alphabet:
	encryption_dict[character] = value
	decryption_dict[value] = character
	value += 1

def encrypt(message):
	encrypted_message = []
	for character in message:
		encrypted_message.append(encryption_dict[character])
	print " ".join(map(str, encrypted_message))

def decrypt(message):
	decrypted_message = []
	for i in message:
		decrypted_message.append(decryption_dict[int(i)])
	print "".join(decrypted_message)

message = raw_input ("What is your secret message? ")
encrypt(message)

decrypt_message = raw_input("What message would you like to decrypt? ")
decrypt_message_split = decrypt_message.split(" ")
decrypt(decrypt_message_split)

