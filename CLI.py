import hashlib
import WhitedCrypt

HashingAlgorithms = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha224": hashlib.sha224, "sha256": hashlib.sha256, "sha384": hashlib.sha384, "sha512": hashlib.sha512, "sha3_224": hashlib.sha3_224, "sha3_256": hashlib.sha3_256, "sha3_384": hashlib.sha3_384, "sha3_512": hashlib.sha3_512}

def Start():
	print("Press CTRL+C anytime to exit.")
	Operation = input("Operation: ").lower()
	ValidOperations = {"encode", "decode", "encrypt", "decrypt"}
	if Operation in ValidOperations:
		Text = input("Text: ")
		if Operation == "encode":
			IsMapped = input("Do you want the output to be obfuscated with whitespaces? (Y/N): ").lower() == "y" and True or False
			EncodedText = WhitedCrypt.Encode(IsMapped and 1 or 2, Text)
			print("Encoded Text [" + str(len(EncodedText)) + "]: \"" + EncodedText + "\"")
			Start()
		elif Operation == "decode":
			DecodedText = WhitedCrypt.Decode(Text)
			print("Decoded Text [" + str(len(DecodedText)) + "]: \"" + DecodedText + "\"")
			Start()
		elif Operation == "encrypt":
			Key = input("Key: ")
			HashingAlgorithm = input("Hashing Algorithm: ").lower()
			IsMapped = input("Do you want the output to be obfuscated with whitespaces? (Y/N): ").lower() == "y" and True or False
			if HashingAlgorithms[HashingAlgorithm]:
				EncryptedText = WhitedCrypt.Encrypt(HashingAlgorithm, IsMapped, Text, Key)
				print("Encrypted Text [" + str(len(EncryptedText)) + "]: \"" + EncryptedText + "\"")
				Start()
			else:
				print("[ERROR] You entered an invalid/unsupported Hashing Algorithm. Supported hashing algorithms are (lightest -> heaviest): md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512")
				Start()
		elif Operation == "decrypt":
			Key = input("Key: ")
			DecryptedText = WhitedCrypt.Decrypt(Text, Key)
			print("Decrypted Text [" + str(len(DecryptedText)) + "]: \"" + DecryptedText + "\"")
			Start()
	else:
		print("[ERROR] You entered an invalid/unsupported operation. Supported operations are: encode, decode, encrypt, decrypt")
		Start()

Start()
