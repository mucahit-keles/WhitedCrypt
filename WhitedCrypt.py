import hashlib
HashingAlgorithms = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha224": hashlib.sha224, "sha256": hashlib.sha256, "sha384": hashlib.sha384, "sha512": hashlib.sha512, "sha3_224": hashlib.sha3_224, "sha3_256": hashlib.sha3_256, "sha3_384": hashlib.sha3_384, "sha3_512": hashlib.sha3_512}

def Map(Method: int, Numbers: str):
	Mapping = Method == 1 and "          " or Method == 2 and "0945862731"
	Mapped = ""
	for Number in Numbers:
		Mapped += Mapping[int(Number)]
	return Mapped

def Unmap(Method: int, MappedNumbers: str):
	Mapping = Method == 1 and "          " or Method == 2 and "0945862731"
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

def Encode(PlainText: str):
	return ToUnicodeOrder(" ", PlainText, True, 1)

def Decode(EncodedText: str):
	return FromUnicodeOrder(" ", EncodedText, True, 1)

def Encrypt(HashingAlgorithm, Mapped: bool, PlainText: str, Key: str):
	HashedKey = HashingAlgorithm(Key.encode()).hexdigest()
	MappedKey = ToUnicodeOrder("1114112", HashedKey, True, 2) # separator is "1114112" because a unicode can be 0x10ffff at max in python
	MappedText = ToUnicodeOrder("1114112", PlainText, True, 2) # last parameter is 2 to map it with numbers instead of whitespaces
	EncryptedText = HashingAlgorithm.__name__.split("openssl_")[1] + "|" + str(int(MappedText) + int(MappedKey))
	return Mapped == True and Encode(EncryptedText) or EncryptedText

def Decrypt(EncryptedText: str, Key: str):
	EncryptedText = EncryptedText.find("|") == -1 and Decode(EncryptedText) or EncryptedText
	HashingAlgorithm = HashingAlgorithms[EncryptedText.split("|")[0]]
	if not HashingAlgorithm:
		return "[ERROR] Hashing Algorithm header is corrupt."
	HashedKey = HashingAlgorithm(Key.encode()).hexdigest()
	MappedKey = ToUnicodeOrder("1114112", HashedKey, True, 2)
	MappedText = str(int(EncryptedText) - int(MappedKey))
	PlainText = FromUnicodeOrder("1114112", MappedText, True, 2)
	return PlainText
