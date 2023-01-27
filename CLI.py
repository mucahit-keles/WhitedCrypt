# Make sure this is in the same folder as WhitedCrypt.py

import hashlib
import WhitedCrypt
import pyperclip

def Start():
	print("Press CTRL+C anytime to exit.")
	Operation = input("Operation: ").lower()
	ValidOperations = {"encode", "decode", "encrypt", "decrypt"}
	if Operation in ValidOperations:
		Text = input("Text: ")
		if Operation == "encode":
			IsMapped = input("Do you want the output to be obfuscated? (Y/N): ").lower() == "y" and True or False
			MappingMethod = 0
			if IsMapped:
				MappingMethod = input("Mapping Method (1 = Whitespaces, 2 = Numbers, 3 = Emojis): ")
				if not (int(MappingMethod) in WhitedCrypt.ValidMappingMethods):
					print("[ERROR] You entered an invalid/unsupported MappingMethod. Supported MappingMethods are: 1 (Whitespace), 2 (Numbers), 3 (Emojis)")
					Start()
			EncodedText = WhitedCrypt.Encode(IsMapped and int(MappingMethod) or 2, Text)
			print("Encoded Text [" + str(len(EncodedText)) + "]: \"" + EncodedText + "\"")
			CopyToClipboard = input("Do you want the output to be copied to your clipboard? (Y/N): ").lower() == "y" and True or False
			if CopyToClipboard:
				pyperclip.copy(EncodedText)
			Start()
		elif Operation == "decode":
			DecodedText = WhitedCrypt.Decode(Text)
			print("Decoded Text [" + str(len(DecodedText)) + "]: \"" + DecodedText + "\"")
			CopyToClipboard = input("Do you want the output to be copied to your clipboard? (Y/N): ").lower() == "y" and True or False
			if CopyToClipboard:
				pyperclip.copy(DecodedText)
			Start()
		elif Operation == "encrypt":
			Key = input("Key: ")
			HashingAlgorithm = input("Hashing Algorithm (md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512): ").lower()
			IsMapped = input("Do you want the output to be obfuscated? (Y/N): ").lower() == "y" and True or False
			MappingMethod = 2
			if IsMapped:
				MappingMethod = input("Mapping Method (1 = Whitespaces, 2 = Numbers, 3 = Emojis): ")
				if not (int(MappingMethod) in WhitedCrypt.ValidMappingMethods):
					print("[ERROR] You entered an invalid/unsupported MappingMethod. Supported MappingMethods are: 1 (Whitespace), 2 (Numbers), 3 (Emojis)")
					Start()
			if WhitedCrypt.HashingAlgorithms[HashingAlgorithm]:
				EncryptedText = WhitedCrypt.Encrypt(HashingAlgorithm, IsMapped, int(MappingMethod), Text, Key)
				print("Encrypted Text [" + str(len(EncryptedText)) + "]: \"" + EncryptedText + "\"")
				CopyToClipboard = input("Do you want the output to be copied to your clipboard? (Y/N): ").lower() == "y" and True or False
				if CopyToClipboard:
					pyperclip.copy(EncryptedText)
				Start()
			else:
				print("[ERROR] You entered an invalid/unsupported Hashing Algorithm. Supported hashing algorithms are (lightest -> heaviest): md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512")
				Start()
		elif Operation == "decrypt":
			Key = input("Key: ")
			DecryptedText = WhitedCrypt.Decrypt(Text, Key)
			print("Decrypted Text [" + str(len(DecryptedText)) + "]: \"" + DecryptedText + "\"")
			CopyToClipboard = input("Do you want the output to be copied to your clipboard? (Y/N): ").lower() == "y" and True or False
			if CopyToClipboard:
				pyperclip.copy(DecryptedText)
			Start()
	else:
		print("[ERROR] You entered an invalid/unsupported operation. Supported operations are: encode, decode, encrypt, decrypt")
		Start()

Start()
