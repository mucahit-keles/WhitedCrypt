import sys
import hashlib

HashingAlgorithms = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha224": hashlib.sha224, "sha256": hashlib.sha256, "sha384": hashlib.sha384, "sha512": hashlib.sha512, "sha3_224": hashlib.sha3_224, "sha3_256": hashlib.sha3_256, "sha3_384": hashlib.sha3_384, "sha3_512": hashlib.sha3_512}
ValidMaskingMethods = {1, 2, 3}

def Mask(MaskingMethod: int, UnicodeNumber: str):
	Masking = MaskingMethod == 1 and "          " or MaskingMethod == 2 and "0945862731" or MaskingMethod == 3 and "😮😀🙃😏🧐😘😍😬😠🤬" or "0945862731"
	MaskedUnicodeNumber = ""
	for UnicodeDigit in UnicodeNumber:
		MaskedUnicodeNumber += Masking[int(UnicodeDigit)]
	return MaskedUnicodeNumber

def Unmask(MaskingMethod: int, MaskedUnicodeNumber: str):
	Masking = MaskingMethod == 1 and "          " or MaskingMethod == 2 and "0945862731" or MaskingMethod == 3 and "😮😀🙃😏🧐😘😍😬😠🤬" or "0945862731"
	UnmaskedUnicodeNumber = ""
	for MaskedUnicodeDigit in MaskedUnicodeNumber:
		UnmaskedUnicodeNumber += str(Masking.find(MaskedUnicodeDigit))
	return UnmaskedUnicodeNumber

def ToUnicodeGroup(Separator: str, PlainText: str, Masked: bool, MaskingMethod: int):
	UnicodeGroup = ""
	for Index in range(0, len(PlainText)):
		Character = PlainText[Index]
		UnicodeNumber = str(ord(Character))
		UnicodeGroup += Masked == True and Mask(MaskingMethod, UnicodeNumber) or UnicodeNumber
		if Index != len(PlainText) - 1:
			UnicodeGroup += Separator
	return UnicodeGroup

def FromUnicodeGroup(Separator: str, UnicodeGroup: str, Masked: bool, MaskingMethod: int):
	PlainText = ""
	for UnicodeNumber in UnicodeGroup.split(Separator):
		UnicodeNumber = Masked == True and Unmask(MaskingMethod, UnicodeNumber) or UnicodeNumber
		PlainText += chr(int(UnicodeNumber))
	return PlainText

def Encode(MaskingMethod: int, PlainText: str):
	if MaskingMethod in ValidMaskingMethods:
		return ToUnicodeGroup(MaskingMethod == 1 and " " or MaskingMethod == 2 and "1114112" or MaskingMethod == 3 and "😳" or "1114112", PlainText, True, MaskingMethod) # The reason for the separator for number masking being "1114112" is because a unicode can be at most 0x10ffff in Python
	else:
		return "[ERROR] You entered an invalid or unsupported masking method. Valid masking methods are as follows: 1 (Whitespaces), 2 (Numbers), 3 (Emojis)"

def Decode(EncodedPlainText: str, ToDecrypt: bool = False):
	MaskingMethod = EncodedPlainText.find(" ") != -1 and 1 or EncodedPlainText.find("1114112") != -1 and 2 or EncodedPlainText.find("😳") != -1 and 3
	if MaskingMethod:
		return FromUnicodeGroup(MaskingMethod == 1 and " " or MaskingMethod == 2 and "1114112" or MaskingMethod == 3 and "😳" or "1114112", EncodedPlainText, True, MaskingMethod) # Sayı maskeleme ayırıcısının "1114112" olmasının sebebi Python'da bir unicode'un en fazla 0x10ffff olabilmesi
	else:
		return ToDecrypt == True and "[ERROR] You entered an invalid password." or "[ERROR] The masking is broken."

def Encrypt(HashingAlgorithmName: str, Masked: bool, MaskingMethod: int, PlainText: str, Key: str):
	if HashingAlgorithmName in HashingAlgorithms:
		HashingAlgorithm = HashingAlgorithms[HashingAlgorithmName.lower()]
		if Masked == False or MaskingMethod in ValidMaskingMethods:
			HashedKey = HashingAlgorithm(Key.encode()).hexdigest()
			EncodedHashedKey = Encode(2, HashedKey) # The first parameter is 2 to mask with numbers
			EncodedPlainText = Encode(2, PlainText) # The first parameter is 2 to mask with numbers
			EncryptedText = HashingAlgorithmName + "|" + str(int(EncodedPlainText) + int(EncodedHashedKey))
			return Masked == True and Encode(MaskingMethod, EncryptedText) or EncryptedText
		else:
			return "[ERROR] You entered an invalid or unsupported masking method. Valid masking methods are as follows: 1 (Whitespaces), 2 (Numbers), 3 (Emojis)"
	else:
		return "[ERROR] You entered an invalid or unsupported hashing algorithm. Valid hashing algorithms are as follows: md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512"

def Decrypt(EncryptedText: str, Key: str):
	EncryptedText = EncryptedText.find("|") != -1 and EncryptedText or Decode(EncryptedText)
	HashingAlgorithm = HashingAlgorithms[EncryptedText.split("|")[0]]
	EncryptedText = EncryptedText.split("|")[1]
	if HashingAlgorithm:
		HashedKey = HashingAlgorithm(Key.encode()).hexdigest()
		EncodedHashedKey = Encode(2, HashedKey) # The first parameter is 2 to mask with numbers
		EncodedPlainText = str(int(EncryptedText) - int(EncodedHashedKey))
		PlainText = Decode(EncodedPlainText, True)
		return PlainText
	else:
		return "[ERROR] The hashing algorithm's header is broken."


Parameters = sys.argv

if len(Parameters) > 1:
	Operation = Parameters[1].lower()
	if Operation == "encode":
		MaskingMethod = int(Parameters[2])
		PlainText = Parameters[3]
		print(Encode(MaskingMethod, PlainText))
	elif Operation == "decode":
		EncodedPlainText = Parameters[2]
		print(Decode(EncodedPlainText))
	elif Operation == "encrypt":
		HashingAlgorithmName = Parameters[2]
		Masked = Parameters[3].lower() == "true"
		MaskingMethod = int(Parameters[4])
		PlainText = Parameters[5]
		Key = Parameters[6]
		print(Encrypt(HashingAlgorithmName, Masked, MaskingMethod, PlainText, Key))
	elif Operation == "decrypt":
		EncryptedText = Parameters[2]
		Key = Parameters[3]
		print(Decrypt(EncryptedText, Key))
