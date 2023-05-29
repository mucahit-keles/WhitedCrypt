# Bu scriptin WhitedCrypt.py ile aynı klasör içerisinde olduğundan emin olun.

import hashlib as HashKutuphanesi
import WhitedCrypt
import pyperclip

def Start():
	print("Çıkmak için CTRL+C'ye basabilirsiniz.")
	Operasyon = input("Operasyon (Kodla, KodlamayiCoz, Sifrele, SifrelemeyiCoz): ").lower()
	GecerliOperasyonlar = {"kodla", "kodlamayicoz", "sifrele", "sifrelemeyicoz"}
	if Operasyon in GecerliOperasyonlar:
		Yazi = input("Yazı: ")
		if Operasyon == "kodla":
			Maskeli = input("Çıktının maskelenmesini ister misiniz? (E/H): ").lower() == "e" and True or False
			MaskelemeMetodu = 0
			if Maskeli:
				MaskelemeMetodu = input("Maskeleme Metodu (1 = Boşluklar, 2 = Sayılar, 3 = Emojiler): ")
				if not (int(MaskelemeMetodu) in WhitedCrypt.GecerliMaskelemeMetodlari):
					print("[HATA] Geçersiz veya desteklenmeyen bir maskeleme metodu girdiniz. Geçerli maskeleme metodları listedeki gibidir: 1 (Boşluklar), 2 (Sayılar), 3 (Emojiler)")
					Start()
			KodlanmisYazi = WhitedCrypt.Kodla(Maskeli and int(MaskelemeMetodu) or 2, Yazi)
			print("Kodlanmış Yazı [" + str(len(KodlanmisYazi)) + "]: \"" + KodlanmisYazi + "\"")
			Kopyalanacak = input("Çıktının kopyalanmasını ister misiniz? (E/H): ").lower() == "e" and True or False
			if Kopyalanacak:
				pyperclip.copy(KodlanmisYazi)
			Start()
		elif Operasyon == "kodlamayicoz":
			CozulmusYazi = WhitedCrypt.KodlamayiCoz(Yazi)
			print("Çözülmüş Yazı [" + str(len(CozulmusYazi)) + "]: \"" + CozulmusYazi + "\"")
			Kopyalanacak = input("Çıktının kopyalanmasını ister misiniz? (E/H): ").lower() == "e" and True or False
			if Kopyalanacak:
				pyperclip.copy(CozulmusYazi)
			Start()
		elif Operasyon == "sifrele":
			Anahtar = input("Anahtar: ")
			HashlemeAlgoritmasi = input("Hashleme Algoritması (md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512): ").lower()
			Maskeli = input("Çıktının maskelenmesini istermisiniz? (E/H): ").lower() == "e" and True or False
			MaskelemeMetodu = 2
			if Maskeli:
				MaskelemeMetodu = input("Maskeleme Metodu (1 = Boşluklar, 2 = Sayılar, 3 = Emojiler): ")
				if not (int(MaskelemeMetodu) in WhitedCrypt.GecerliMaskelemeMetodlari):
					print("[HATA] Geçersiz veya desteklenmeyen bir maskeleme metodu girdiniz. Geçerli maskeleme metodları listedeki gibidir: 1 (Boşluklar), 2 (Sayılar), 3 (Emojiler)")
					Start()
			if WhitedCrypt.HashlemeAlgoritmalari[HashlemeAlgoritmasi]:
				SifrelenmisYazi = WhitedCrypt.Sifrele(HashlemeAlgoritmasi, Maskeli, int(MaskelemeMetodu), Yazi, Anahtar)
				print("Şifreli Yazı [" + str(len(SifrelenmisYazi)) + "]: \"" + SifrelenmisYazi + "\"")
				Kopyalanacak = input("Çıktının kopyalanmasını ister misiniz? (E/H): ").lower() == "e" and True or False
				if Kopyalanacak:
					pyperclip.copy(SifrelenmisYazi)
				Start()
			else:
				print("[HATA] Geçersiz veya desteklenmeyen bir hashleme algoritması girdiniz. Geçerli hashleme algoritmaları listedeki gibidir: md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512")
				Start()
		elif Operasyon == "sifrelemeyicoz":
			Anahtar = input("Anahtar: ")
			CozulmusYazi = WhitedCrypt.SifrelemeyiCoz(Yazi, Anahtar)
			print("Çözülmüş Yazı [" + str(len(CozulmusYazi)) + "]: \"" + CozulmusYazi + "\"")
			Kopyalanacak = input("Çıktının kopyalanmasını ister misiniz? (E/H): ").lower() == "e" and True or False
			if Kopyalanacak:
				pyperclip.copy(CozulmusYazi)
			Start()
	else:
		print("[HATA] Geçersiz veya desteklenmeyen bir operasyon girdiniz. Geçerli operasyonlar listedeki gibidir: Kodla, KodlamayiCoz, Sifrele, SifrelemeyiCoz")
		Start()

Start()
