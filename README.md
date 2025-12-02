# Yurtici-Kargo-Kontrol
📦 Yurtiçi Kargo Fatura Kontrol Otomasyonu (V3)

Bu proje, Interkan & Poliner firmalarında kullanılan Yurtiçi Kargo fatura kontrol sürecini otomatikleştirmek için geliştirilmiş kapsamlı bir Python uygulamasıdır.

Amaç:

PDF faturalarındaki QR kodları okuyup veriyi çıkarmak

Yurtiçi Kargo formatında gönderim Excel’i oluşturmak

Web otomasyonu ile Yurtiçi Kargo raporlarını indirmek

Mailden indirilen RPT Excel dosyalarını birleştirmek

Tarife tablosuna göre maliyet hesaplamak ve tutar kontrolü yapmak

Sonuçları fatura bazlı Excel’lere ayrılmış şekilde üretmek

Çıktıların yazıcıya uygun sayfa ayarlarını otomatik yapmak

Bu proje sayesinde faturaların manuel kontrolü yerine tamamen otomatik, hızlı ve hatasız bir süreç oluşur.

🚀 Özellikler

✔ PDF içinde çok sayfalı QR kod okuma

✔ Yurtiçi uyumlu tek tıklamayla Excel üretimi

✔ Selenium ile otomatik rapor talebi gönderme

✔ Mailden indirilen RPT dosyalarını otomatik birleştirme

✔ Tarife tablosuna göre otomatik maliyet hesaplama

✔ %5 hata payına göre Tutar Uygun / Tutar Hatalı kontrolü

✔ Her faturayı ayrı Excel olarak oluşturma

✔ Otomatik sayfa ayarları:

A4 dikey

1 sayfaya sığdırma

0.5 margin

Gridlines gizleme

✔ Düzenli klasör yapısı (V3 mimarisi)

📁 Proje Klasör Yapısı (V3) Yurtici-Kargo-v3/ │ ├── main.py # Ana menü ve işlem akışı ├── config.py # Kullanıcı yolları + global ayarlar │ ├── app/ │ ├── qr_okuma.py # PDF QR kod okuma │ ├── excel_olustur.py # Gönderim Excel’i üretme │ ├── yurtici_site_otomasyon.py # Web otomasyon (geçici V2) │ ├── mail_birlestir.py # RPT dosyalarını birleştirme │ ├── maliyet_kontrol.py # Tarife karşılaştırma + çıktı üretimi │ ├── helpers.py # Ortak fonksiyonlar │ └── init.py │ ├── Tarife/ │ └── Yurt İçi Kargo Fiyatları.xlsx │ └── README.md

⚙ Gereksinimler

Bu yazılım:

Python 3.10+

Anaconda ortamı (base environment da yeterli)

Aşağıdaki kütüphaneleri ister:

pandas openpyxl pymupdf Pillow pyzbar selenium tkinter (Windows'ta hazır gelir)

Chromedriver:

CHROMEDRIVER_PATH → config.py içinde ayarlanmıştır.

▶ Kullanım Akışı (V3) 1️⃣ Adım: PDF’lerden QR Kodlarını Okut python main.py → 1

Çıktı:

Duzenlenen_QR_listesi.xlsx

2️⃣ Adım: Gönderim Excel’i Oluştur python main.py → 2

Çıktı:

19.November.2025 - Yurtiçi Kargo Faturaları.xlsx

3️⃣ Adım: Yurtiçi Rapor Talebi Gönder (V2 otomasyon) python main.py → 3

Bu adım eski automation ile çalışır.

4️⃣ Adım: Mailden Gelen RPT Excel Dosyalarını Birleştir python main.py → 4

Çıktı:

V3\MailExcels\2025-11-19\2025-11-19 - Birleştirilmiş Mail Excelleri.xlsx

5️⃣ Adım: Maliyet Kontrolü ve Sonuç Excelleri python main.py → 5

Her fatura için ayrı dosya + otomatik yazıcı ayarlı sayfalar oluşturur.

📌 Ayarlar (config.py)

En kritik yollar burada tutulur:

PDF klasörü (Z sürücüsü)

Masaüstü yolu

ChromeDriver yolu

RPT birleştirme klasörü

Tarife Excel adresi

Desktop çıktılarının yolları

Prefix filtreleri (YKA20, YKB20)

Tüm proje tek dosyadan yönetilebilir.

📘 Gelecek Geliştirmeler (TODO)

3️⃣. adımı V3 için tamamen yenilemek

Yurtiçi sitesindeki başarı / hata mesajlarını otomatik algılama

EXE haline getirmek (pyinstaller)

GUI arayüz (Tkinter ile butonlu ekran)

Mail üzerinden direkt rapor indirme (IMAP + link parsing)

Loglama sistemi

Çoklu hesap / şirket desteği

requirement.txt eklemek

👨‍💻 Geliştirici

Yalçın Hacıoğlu Interkan / Poliner – Satınalma

🤝 Destek

Her türlü geliştirme, bakım, destek işlemi için ChatGPT üzerinden ilerleyebilirsiniz 💙

Bu README projen için mükemmel bir doküman olacak.

İstersen bir sonraki adımda sana:

✔ .gitignore dosyasını da hazırlayabilirim

(gereksiz Excel çıktıları repo’ya eklenmesin diye)

İster misin?
