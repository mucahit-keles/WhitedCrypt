# WhitedCrypt

**Bu repository'nin sahipliği eski hesabımdan bu hesaba aktarıldığı için, önceki commitlerim eski hesabımın adına gözükmekte.**

Kendimi denemek için Python ile geliştirdiğim bir şifreleme algoritması. Bunu söylemeye gerek olmadığını düşünüyorum, fakat algoritma yeterince güvenli olmadığı için önemli verilerin şifrelenmesi için kullanılmasını **ÖNERMİYORUM**.
Bu algoritmayı kullanarak şifrelediğiniz herhangi bir veri kırılırsa, bunun sorumluluğu tamamen sizin üzerinizde.

## Nasıl mı çalışıyor?
Temel olarak 4 fonksiyon var:

**Kodla(*KodlamaMetodu: int*, *DuzYazi: str*):**
- [DuzYazi] içindeki her karakterin üzerinden geçer.
- Karakterin eşdeğer Unicode numarasını alır.
- Ayırıcılarla (Örnek: "unicode1\unicode2\unicode3") bir [UnicodeSatiri] (Tüm Unicode numaralarının bir satırda olması hali) oluşturur.
- Ardından, [UnicodeSatiri] içindeki tüm Unicode numaralarının üzerinden geçer.
- Karakterleri, seçilen maskeleme tipine göre farklı karakterler ile değiştirerek [UnicodeSatiri]'nı maskeler.

**KodlamayiCoz(*KodlanmisMetin: str*):**
- [Kodla]'nin tersini yapar.

**Sifrele(*HashlemeAlgoritmasiAdi: str*, *DuzYazi: str*, *Anahtar: str*):**
- [Anahtar]'ı, seçilen hashleme algoritması ile hashler.
- [HashliAnahtar]'ı, [Kodla] fonksiyonu ile sayı maskelemesi kullanarak kodlar.
- [DuzYazi]'yı da, [Kodla] fonksiyonu ile sayı maskelemesi kullanarak kodlar.
* Sayı maskelemesi kullanmamızın sebebi bu string'leri mantıksal birer sayıya dönüştürüp üzerlerinde matematiksel işlemler yapabilmek.
* Artık hem [HashliAnahtar], hem de [DuzYazi] mantıksal birer sayı olduğuna göre, bunların üzerlerinde matematiksel işlemler yapabiliriz.
- [KodlanmisHashliAnahtar]'ı, [KodlanmisDuzYazi]'ya ekler.
* Bir yazı olarak sonuna eklemez, tam anlamıyla matematiksel bir işlem olarak ekler, bu da metnin kendisini elde etmek için sonuçtan [KodlanmisHashliAnahtar]'ı matematiksel olarak çıkartmanız gerektiği anlamına gelir. Bu da anahtara sahip olmanızı gerektirir.
- Sonucu, [Kodla] fonksiyonu ile kodlayıp kullanıcıya döndürür.

**SifrelemeyiCoz(*SifrelenmisYazi: str*, *Anahtar: str*):**
- [Sifrele]'nin tersini yapar.
