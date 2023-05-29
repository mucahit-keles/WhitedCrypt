# WhitedCrypt

**Bu repository'nin sahipliği eski hesabımdan bu hesaba aktarıldığı için, önceki commitlerim eski hesabımın adına gözükmekte.**

Sıfırdan benim tarafımdan yapılmış bir şifreleme algoritması. Bunu söylemeye gerek olmadığını düşünüyorum, fakat algoritma yeterince güvenli olmadığı için önemli verileri şifrelemek için kullanmanızı **ÖNERMİYORUM**. ***Henüz kırılmamış olması hiçbir zaman kırılmayacağı anlamına gelmiyor.***
Bu algoritmayı kullanarak şifrelediğiniz herhangi bir veri kırılırsa, bunun sorumluluğu tamamen sizin üzerinizde.

Pull requestlere açığım.

## Nasıl mı çalışıyor?
Temel olarak 4 fonksiyon var:

**Kodla(*DuzYazi: string*):**
- [DuzYazi] içindeki her karakterin üzerinden geçer.
- Karakterin eşdeğer Unicode numarasını alır.
- Ayırıcılarla (Örnek: "unicode1\unicode2\unicode3") bir [UnicodeSatiri] (Tüm Unicode numaralarının bir satırda olması hali) oluşturur.
- Ardından, [UnicodeSatiri] içindeki tüm Unicode numaralarının üzerinden geçer.
- Karakterleri seçilen maskeleme tipine göre farklı karakterler ile değiştirerek [UnicodeSatiri]'nı maskeler.

**KodlamayiCoz(*KodlanmisMetin: string*):**
- [Kodla]'nin tersini yapar.

**Sifrele(*DuzYazi: string*, *Anahtar: string*):**
- [Anahtar]'ı seçilen hash algoritması ile hashler.
- [HashliAnahtar]'ı [Kodla] fonksiyonu ile sayı maskelemesi kullanarak kodlar.
- [DuzYazi]'yı da [Kodla] fonksiyonu ile sayı maskelemesi kullanarak kodlar.
* Sayı maskelemesi kullanmamızın sebebi bu string'leri mantıksal birer sayıya dönüştürüp üzerlerinde matematiksel işlemler yapabilmek.
* Artık hem [HashliAnahtar], hem de [DuzYazi] mantıksal birer sayı olduğuna göre, bunların üzerlerinde matematiksel işlemler yapabiliriz.
- [KodlanmisHashliAnahtar]'ı [KodlanmisDuzYazi]'ya ekler.
* Bir yazı olarak sonuna eklemez, tam anlamıyla matematiksel bir işlem olarak ekler, bu da metnin kendisini elde etmek için sonuçtan [KodlanmisHashliAnahtar]'ı matematiksel olarak çıkartmanız gerektiği anlamına gelir. Bu da anahtara sahip olmanızı gerektirir.
- Sonucu [Kodla] fonksiyonu ile seçilen maskeleme tipi ile kodlayıp kullanıcıya döndürür.

**SifrelemeyiCoz(*SifrelenmisYazi: string*, *Anahtar: string*):**
- [Sifrele]'nin tersini yapar.
