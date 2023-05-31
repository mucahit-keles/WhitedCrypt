import hashlib as HashKutuphanesi

HashlemeAlgoritmalari = {"md5": HashKutuphanesi.md5, "sha1": HashKutuphanesi.sha1, "sha224": HashKutuphanesi.sha224, "sha256": HashKutuphanesi.sha256, "sha384": HashKutuphanesi.sha384, "sha512": HashKutuphanesi.sha512, "sha3_224": HashKutuphanesi.sha3_224, "sha3_256": HashKutuphanesi.sha3_256, "sha3_384": HashKutuphanesi.sha3_384, "sha3_512": HashKutuphanesi.sha3_512}
GecerliMaskelemeMetodlari = {1, 2, 3}

def Maskele(MaskelemeMetodu: int, UnicodeSayisi: str):
	Maskeleme = MaskelemeMetodu == 1 and "          " or MaskelemeMetodu == 2 and "0945862731" or MaskelemeMetodu == 3 and "😮😀🙃😏🧐😘😍😬😠🤬"
	MaskeliUnicodeSayisi = ""
	for UnicodeHanesi in UnicodeSayisi:
		MaskeliUnicodeSayisi += Maskeleme[int(UnicodeHanesi)]
	return MaskeliUnicodeSayisi

def MaskelemeyiCoz(MaskelemeMetodu: int, MaskelenmisUnicodeSayisi: str):
	Maskeleme = MaskelemeMetodu == 1 and "          " or MaskelemeMetodu == 2 and "0945862731" or MaskelemeMetodu == 3 and "😮😀🙃😏🧐😘😍😬😠🤬"
	MaskesizUnicodeSayisi = ""
	for MaskelenmisUnicodeHanesi in MaskelenmisUnicodeSayisi:
		MaskesizUnicodeSayisi += str(Maskeleme.find(MaskelenmisUnicodeHanesi))
	return MaskesizUnicodeSayisi

def UnicodeSatirinaCevir(Ayirici: str, Yazi: str, Maskeli: bool, MaskelemeMetodu: int):
	UnicodeSatiri = ""
	for Indis in range(0, len(Yazi)):
		Karakter = Yazi[Indis]
		UnicodeSayisi = str(ord(Karakter))
		UnicodeSatiri += Maskeli == True and Maskele(MaskelemeMetodu, UnicodeSayisi) or UnicodeSayisi
		if Indis != len(Yazi) - 1:
			UnicodeSatiri += Ayirici
	return UnicodeSatiri

def UnicodeSatiriniCoz(Ayirici: str, UnicodeSatiri: str, Maskeli: bool, MaskelemeMetodu: int):
	Yazi = ""
	for UnicodeSayisi in UnicodeSatiri.split(Ayirici):
		UnicodeSayisi = Maskeli == True and MaskelemeyiCoz(MaskelemeMetodu, UnicodeSayisi) or UnicodeSayisi
		Yazi += chr(int(UnicodeSayisi))
	return Yazi

def Kodla(MaskelemeMetodu: int, DuzYazi: str):
	if MaskelemeMetodu in GecerliMaskelemeMetodlari:
		return UnicodeSatirinaCevir(MaskelemeMetodu == 1 and " " or MaskelemeMetodu == 2 and "1114112" or MaskelemeMetodu == 3 and "😳", DuzYazi, True, MaskelemeMetodu) # separator is "1114112" because a unicode can be 0x10ffff at max in python
	else:
		return "[HATA] Geçersiz veya desteklenmeyen bir maskeleme metodu girdiniz. Geçerli maskeleme metodları listedeki gibidir: 1 (Boşluklar), 2 (Sayılar), 3 (Emojiler)"

def KodlamayiCoz(KodlanmisYazi: str, SifrelemeCozmekIcin: bool = False):
	MaskelemeMetodu = KodlanmisYazi.find(" ") != -1 and 1 or KodlanmisYazi.find("1114112") != -1 and 2 or KodlanmisYazi.find("😳") != -1 and 3
	if MaskelemeMetodu:
		return UnicodeSatiriniCoz(MaskelemeMetodu == 1 and " " or MaskelemeMetodu == 2 and "1114112" or MaskelemeMetodu == 3 and "😳", KodlanmisYazi, True, MaskelemeMetodu) # separator is "1114112" because a unicode can be 0x10ffff at max in python
	else:
		return SifrelemeCozmekIcin == True and "[HATA] Geçersiz bir şifre girdiniz." or "[HATA] Maskeleme bozuk."

def Sifrele(HashlemeAlgoritmasiAdi: str, Maskeli: bool, MaskelemeMetodu: int, DuzYazi: str, Anahtar: str):
	HashlemeAlgoritmasi = HashlemeAlgoritmalari[HashlemeAlgoritmasiAdi.lower()]
	if HashlemeAlgoritmasi:
		if MaskelemeMetodu in GecerliMaskelemeMetodlari:
			HashliAnahtar = HashlemeAlgoritmasi(Anahtar.encode()).hexdigest()
			KodlanmisHashliAnahtar = Kodla(2, HashliAnahtar) # İlk parametrenin 2 olmasının sebebi sayılarla maskeleme yapmak istememiz
			KodlanmisYazi = Kodla(2, DuzYazi) # İlk parametrenin 2 olmasının sebebi sayılarla maskeleme yapmak istememiz
			SifrelenmisYazi = HashlemeAlgoritmasiAdi + "|" + str(int(KodlanmisYazi) + int(KodlanmisHashliAnahtar))
			return Maskeli == True and Kodla(MaskelemeMetodu, SifrelenmisYazi) or SifrelenmisYazi
		else:
			return "[HATA] Geçersiz veya desteklenmeyen bir maskeleme metodu girdiniz. Geçerli maskeleme metodları listedeki gibidir: 1 (Boşluklar), 2 (Sayılar), 3 (Emojiler)"
	else:
		return "[HATA] Geçersiz veya desteklenmeyen bir hashleme algoritması girdiniz. Geçerli hashleme algoritmaları listedeki gibidir: md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512"

def SifrelemeyiCoz(SifrelenmisYazi: str, Anahtar: str):
	SifrelenmisYazi = SifrelenmisYazi.find("|") != -1 and SifrelenmisYazi or KodlamayiCoz(SifrelenmisYazi)
	HashlemeAlgoritmasi = HashlemeAlgoritmalari[SifrelenmisYazi.split("|")[0]]
	SifrelenmisYazi = SifrelenmisYazi.split("|")[1]
	if HashlemeAlgoritmasi:
		HashliAnahtar = HashlemeAlgoritmasi(Anahtar.encode()).hexdigest()
		KodlanmisHashliAnahtar = Kodla(2, HashliAnahtar)
		KodlanmisYazi = str(int(SifrelenmisYazi) - int(KodlanmisHashliAnahtar))
		CozulmusYazi = KodlamayiCoz(KodlanmisYazi, True)
		return CozulmusYazi
	else:
		return "[HATA] Hashleme Algoritması header'ı bozuk."
