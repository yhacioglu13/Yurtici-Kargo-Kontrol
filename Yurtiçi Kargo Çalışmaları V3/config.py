"""Projenin tüm yol ve sabit ayarları burada toplanır."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

# Z sürücüsündeki e-fatura klasörü (İNTERKAN)
Z_EFATURA_FOLDER = Path(
    r"Z:\SATINALMA - LOJİSTİK\ÖDEMELER\KONTROL EDİLECEK E-FATURALAR\İNTERKAN"
)

# Yurtiçi PDF’leri için prefix
YURTICI_PREFIXES = ("YKA20", "YKB20")


# 2) Mail’den gelen RPT excelleri için klasörler
MAIL_EXCEL_ROOT = PROJECT_ROOT / "MailExcels"   # 4. adımın sonuçları burada
RESULT_EXCEL_ROOT = PROJECT_ROOT / "Results"    # 5. adım fatura bazlı exceller

# 3) Tarife klasörü ve dosyası
TARIFF_FOLDER = PROJECT_ROOT / "Tarife"
TARIFF_EXCEL_PATH = TARIFF_FOLDER / "Yurt İçi Kargo Fiyatları.xlsx"

# 4) Windows Downloads klasörü
DOWNLOADS_FOLDER = Path.home() / "Downloads"

# 5) ChromeDriver için klasör ve dosya yolu
# drivers/
#   └─ chromedriver.exe
DRIVERS_FOLDER = PROJECT_ROOT / "drivers"
CHROMEDRIVER_PATH = DRIVERS_FOLDER / "chromedriver.exe"

# 6) Yurtiçi e-fatura formu için varsayılan mail adresi
# (excelde 'mail' kolonu boşsa bu adres kullanılır)
DEFAULT_EMAIL = "yhacioglu@interkan.com.tr"
