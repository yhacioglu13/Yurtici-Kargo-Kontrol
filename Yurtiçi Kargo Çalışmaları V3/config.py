"""Projenin tüm yol ve sabit ayarları burada toplanır."""

from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent


def _env_path(key: str, default: Path) -> Path:
    """Ortam değişkeniyle özelleştirilebilir yol döndürür."""

    env_value = os.getenv(key)
    if env_value:
        try:
            return Path(env_value).expanduser().resolve()
        except Exception:
            pass
    return default

# Z sürücüsündeki e-fatura klasörü (İNTERKAN)
Z_EFATURA_FOLDER = _env_path(
    "Z_EFATURA_FOLDER",
    Path(r"Z:\SATINALMA - LOJİSTİK\ÖDEMELER\KONTROL EDİLECEK E-FATURALAR\İNTERKAN"),
)

# Yurtiçi PDF’leri için prefix
YURTICI_PREFIXES = ("YKA20", "YKB20")


# 2) Mail’den gelen RPT excelleri için klasörler
MAIL_EXCEL_ROOT = _env_path("MAIL_EXCEL_ROOT", PROJECT_ROOT / "MailExcels")
# 5. adım fatura bazlı exceller
RESULT_EXCEL_ROOT = _env_path("RESULT_EXCEL_ROOT", PROJECT_ROOT / "Results")

# 3) Tarife klasörü ve dosyası
TARIFF_FOLDER = _env_path("TARIFF_FOLDER", PROJECT_ROOT / "Tarife")
TARIFF_EXCEL_PATH = _env_path(
    "TARIFF_EXCEL_PATH", TARIFF_FOLDER / "Yurt İçi Kargo Fiyatları.xlsx"
)

# 4) Windows Downloads klasörü
DOWNLOADS_FOLDER = _env_path("DOWNLOADS_FOLDER", Path.home() / "Downloads")

# 5) ChromeDriver için klasör ve dosya yolu
# drivers/
#   └─ chromedriver.exe
DRIVERS_FOLDER = _env_path("DRIVERS_FOLDER", PROJECT_ROOT / "drivers")
CHROMEDRIVER_PATH = _env_path("CHROMEDRIVER_PATH", DRIVERS_FOLDER / "chromedriver.exe")

# 6) Yurtiçi e-fatura formu için varsayılan mail adresi
# (excelde 'mail' kolonu boşsa bu adres kullanılır)
DEFAULT_EMAIL = "yhacioglu@interkan.com.tr"

# 7) V2 otomasyon dosya yolu (gerekirse ortam değişkeniyle güncellenebilir)
LEGACY_AUTOMATION_PATH = _env_path(
    "LEGACY_AUTOMATION_PATH", PROJECT_ROOT / "app" / "yurtici_site_otomasyon.py"
)

# 8) QR okuma sonucunun yazılacağı Excel yolu
QR_OUTPUT_PATH = _env_path(
    "QR_OUTPUT_PATH", PROJECT_ROOT / "Duzenlenen_QR_listesi.xlsx"
)
