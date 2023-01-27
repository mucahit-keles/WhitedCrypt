import hashlib

HashingAlgorithms = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha224": hashlib.sha224, "sha256": hashlib.sha256, "sha384": hashlib.sha384, "sha512": hashlib.sha512, "sha3_224": hashlib.sha3_224, "sha3_256": hashlib.sha3_256, "sha3_384": hashlib.sha3_384, "sha3_512": hashlib.sha3_512}
ValidMappingMethods = {1, 2, 3}

def Map(Method: int, Numbers: str):
	Mapping = Method == 1 and "          " or Method == 2 and "0945862731" or Method == 3 and "😮😀🙃😏🧐😘😍😬😠🤬"
	Mapped = ""
	for Number in Numbers:
		Mapped += Mapping[int(Number)]
	return Mapped

def Unmap(Method: int, MappedNumbers: str):
	Mapping = Method == 1 and "          " or Method == 2 and "0945862731" or Method == 3 and "😮😀🙃😏🧐😘😍😬😠🤬"
	Unmapped = ""
	for MappedNumber in MappedNumbers:
		Unmapped += str(Mapping.find(MappedNumber))
	return Unmapped

def ToUnicodeOrder(Separator: str, Text: str, Mapped: bool, MappingMethod: int):
	UnicodeOrder = ""
	for Index in range(0, len(Text)):
		Character = Text[Index]
		Unicode = str(ord(Character))
		UnicodeOrder += Mapped == True and Map(MappingMethod, Unicode) or Unicode
		if Index != len(Text) - 1:
			UnicodeOrder += Separator
	return UnicodeOrder

def FromUnicodeOrder(Separator: str, UnicodeOrder: str, Mapped: bool, MappingMethod: int):
	Text = ""
	for RawUnicode in UnicodeOrder.split(Separator):
		Unicode = Mapped == True and Unmap(MappingMethod, RawUnicode) or RawUnicode
		Text += chr(int(Unicode))
	return Text

def Encode(MappingMethod: int, PlainText: str):
	if MappingMethod in ValidMappingMethods:
		return ToUnicodeOrder(MappingMethod == 1 and " " or MappingMethod == 2 and "1114112" or MappingMethod == 3 and "😳", PlainText, True, MappingMethod) # separator is "1114112" because a unicode can be 0x10ffff at max in python
	else:
		return "[ERROR] You entered an invalid/unsupported MappingMethod. Supported MappingMethods are: 1 (Whitespace), 2 (Numbers), 3 (Emojis)"

def Decode(EncodedText: str, ForDecryption: bool = False):
	MappingMethod = EncodedText.find(" ") != -1 and 1 or EncodedText.find("1114112") != -1 and 2 or EncodedText.find("😳") != -1 and 3
	if MappingMethod:
		return FromUnicodeOrder(MappingMethod == 1 and " " or MappingMethod == 2 and "1114112" or MappingMethod == 3 and "😳", EncodedText, True, MappingMethod) # separator is "1114112" because a unicode can be 0x10ffff at max in python
	else:
		return ForDecryption == True and "[ERROR] You entered an invalid key" or "[ERROR] Mapping is corrupted."

def Encrypt(HashingAlgorithmName: str, Mapped: bool, MappingMethod: int, PlainText: str, Key: str):
	HashingAlgorithm = HashingAlgorithms[HashingAlgorithmName.lower()]
	if HashingAlgorithm:
		if MappingMethod in ValidMappingMethods:
			HashedKey = HashingAlgorithm(Key.encode()).hexdigest()
			MappedKey = Encode(2, HashedKey) # first parameter is 2 to map it with numbers instead of whitespaces
			MappedText = Encode(2, PlainText) # first parameter is 2 to map it with numbers instead of whitespaces
			EncryptedText = HashingAlgorithmName + "|" + str(int(MappedText) + int(MappedKey))
			return Mapped == True and Encode(MappingMethod, EncryptedText) or EncryptedText
		else:
			return "[ERROR] You entered an invalid/unsupported MappingMethod. Supported MappingMethods are: 1 (Whitespace), 2 (Numbers), 3 (Emojis)"
	else:
		return "[ERROR] You entered an invalid/unsupported Hashing Algorithm. Supported hashing algorithms are (lightest -> heaviest): md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512"

def Decrypt(EncryptedText: str, Key: str):
	EncryptedText = EncryptedText.find("|") != -1 and EncryptedText or Decode(EncryptedText)
	HashingAlgorithm = HashingAlgorithms[EncryptedText.split("|")[0]]
	EncryptedText = EncryptedText.split("|")[1]
	if HashingAlgorithm:
		HashedKey = HashingAlgorithm(Key.encode()).hexdigest()
		MappedKey = Encode(2, HashedKey)
		MappedText = str(int(EncryptedText) - int(MappedKey))
		PlainText = Decode(MappedText, True)
		return PlainText
	else:
		return "[ERROR] Hashing Algorithm header is corrupted."

