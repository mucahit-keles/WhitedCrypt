import WhitedCrypt

def Start():
	print("Press CTRL+C anytime to exit.")
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
			HashingAlgorithm = HashingAlgorithms[input("Hashing Algorithm: ")]
			if HashingAlgorithm:
				EncryptedText = WhitedCrypt.Encrypt(HashingAlgorithm, Text, Key)
				print("Encrypted Text [" + str(len(EncryptedText)) + "]: \"" + EncryptedText + "\"")
			else:
				print("[ERROR] You entered an invalid/unsupported Hashing Algorithm. Supported hashing algorithms are (lightest -> heaviest): md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512")
				Start()
		elif Operation == "decrypt":
			Key = input("Key: ")
			DecryptedText = WhitedCrypt.Decrypt(Text, Key)
			print("Decrypted Text [" + str(len(DecryptedText)) + "]: \"" + DecryptedText + "\"")
	else:
		print("[ERROR] You entered an invalid/unsupported operation. Supported operations are: encode, decode, encrypt, decrypt")
		Start()

Start()
