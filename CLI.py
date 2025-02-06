# Make sure that this script is in the same directory as "WhitedCrypt.py".

import WhitedCrypt
import pyperclip

def Start():
	print("You can press CTRL+C to exit.")
	Operation = input("Enter Operation (Encode, Decode, Encrypt, Decrypt): ").lower()
	ValidOperations = {"encode", "decode", "encrypt", "decrypt"}
	if Operation in ValidOperations:
		Text = input("Enter Text: ")
		if Operation == "encode":
			Masked = input("Would you like the output to be masked? (y/n): ").lower() == "y" and True or False
			MaskingMethod = 0
			if Masked:
				MaskingMethod = input("Masking Method (1 = Whitespaces, 2 = Numbers, 3 = Emojis): ")
				if not (int(MaskingMethod) in WhitedCrypt.ValidMaskingMethods):
					print("[ERROR] You entered an invalid or unsupported masking method. Valid masking methods are as follows: 1 (Whitespaces), 2 (Numbers), 3 (Emojis)")
					Start()
			EncodedPlainText = WhitedCrypt.Encode(Masked and int(MaskingMethod) or 2, Text)
			print("Encoded Text [" + str(len(EncodedPlainText)) + "]: \"" + EncodedPlainText + "\"")
			ToBeCopied = input("Would you like the result to be copied? (y/n): ").lower() == "y" and True or False
			if ToBeCopied:
				pyperclip.copy(EncodedPlainText)
			Start()
		elif Operation == "decode":
			PlainText = WhitedCrypt.Decode(Text)
			print("Decoded Text [" + str(len(PlainText)) + "]: \"" + PlainText + "\"")
			ToBeCopied = input("Would you like the result to be copied? (y/n): ").lower() == "y" and True or False
			if ToBeCopied:
				pyperclip.copy(PlainText)
			Start()
		elif Operation == "encrypt":
			Key = input("Enter Key: ")
			HashingAlgorithm = input("Hashing Algorithm (md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512): ").lower()
			Masked = input("Would you like the output to be masked? (y/n): ").lower() == "y" and True or False
			MaskingMethod = 2
			if Masked:
				MaskingMethod = input("Masking Method (1 = Whitespaces, 2 = Numbers, 3 = Emojis): ")
				if not (int(MaskingMethod) in WhitedCrypt.ValidMaskingMethods):
					print("[ERROR] You entered an invalid or unsupported masking method. Valid masking methods are as follows: 1 (Whitespaces), 2 (Numbers), 3 (Emojis)")
					Start()
			if WhitedCrypt.HashingAlgorithms[HashingAlgorithm]:
				EncryptedText = WhitedCrypt.Encrypt(HashingAlgorithm, Masked, int(MaskingMethod), Text, Key)
				print("Encrypted Text [" + str(len(EncryptedText)) + "]: \"" + EncryptedText + "\"")
				ToBeCopied = input("Would you like the result to be copied? (y/n): ").lower() == "y" and True or False
				if ToBeCopied:
					pyperclip.copy(EncryptedText)
				Start()
			else:
				print("[ERROR] You entered an invalid or unsupported hashing algorithm. Valid hashing algorithms are as follows: md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512")
				Start()
		elif Operation == "decrypt":
			Key = input("Enter Key: ")
			PlainText = WhitedCrypt.Decrypt(Text, Key)
			print("Decrypted Text [" + str(len(PlainText)) + "]: \"" + PlainText + "\"")
			ToBeCopied = input("Would you like the result to be copied? (y/n): ").lower() == "y" and True or False
			if ToBeCopied:
				pyperclip.copy(PlainText)
			Start()
	else:
		print("[ERROR] You entered an invalid or unsupported operation. Valid operations are as follows: Encode, Decode, Encrypt, Decrypt")
		Start()

Start()
