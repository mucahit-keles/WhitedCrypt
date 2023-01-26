import WhitedCrypt

Operation = input("Operation: ").lower()
ValidOperations = {"encode", "decode", "encrypt", "decrypt"}
if Operation in ValidOperations:
	Text = input("Text: ")
	if Operation == "encode":
		EncodedText = WhitedCrypt.Encode(Text)
		print("Encoded Text [" + str(len(EncodedText)) + "]: \"" + EncodedText + "\"")
	elif Operation == "decode":
		DecodedText = WhitedCrypt.Decode(Text)
		print("Decoded Text [" + str(len(DecodedText)) + "]: \"" + DecodedText + "\"")
	elif Operation == "encrypt":
		Key = input("Key: ")
		EncryptedText = WhitedCrypt.Encrypt(Text, Key)
		print("Encrypted Text [" + str(len(EncryptedText)) + "]: \"" + EncryptedText + "\"")
	elif Operation == "decrypt":
		Key = input("Key: ")
		DecryptedText = WhitedCrypt.Decrypt(Text, Key)
		print("Decrypted Text [" + str(len(DecryptedText)) + "]: \"" + DecryptedText + "\"")
