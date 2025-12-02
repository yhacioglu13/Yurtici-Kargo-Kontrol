"""Yurtiçi Kargo e-fatura formunu Selenium ile otomatik dolduran script."""
from __future__ import annotations

import time
from pathlib import Path
from typing import Optional

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import tkinter as tk
from tkinter import messagebox

# config.py'den CHROMEDRIVER_PATH'i almaya çalış
try:
    from config import CHROMEDRIVER_PATH
except ModuleNotFoundError:
    # Eğer bu dosyayı app klasöründen tek başına çalıştırırsan,
    # proje kökünü sys.path'e ekleyip tekrar dene
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[1]  # ...\Yurtiçi Kargo Çalışmaları V3
    if str(ROOT) not in sys.path:
        sys.path.append(str(ROOT))

    from config import CHROMEDRIVER_PATH

from app.helpers import today_str_en  # tarih formatı için helpers'ı buradan alıyoruz


# ==================== YARDIMCI FONKSİYONLAR ====================

def find_daily_excel() -> Optional[Path]:
    """
    Bugünün tarihine göre masaüstündeki Excel'i bulur.

    Örn: 19.November.2025 - Yurtiçi Kargo Faturaları.xlsx
    """
    today = today_str_en()
    desktop = Path.home() / "Desktop"
    filename = f"{today} - Yurtiçi Kargo Faturaları.xlsx"
    path = desktop / filename

    if not path.exists():
        print(f"❌ Hata: Günlük Excel bulunamadı! ({path})")
        return None

    print(f"📄 Günlük Excel bulundu: {path}")
    return path


def kullanici_onayi_al() -> bool:
    """Kullanıcıdan 'Excelleri indirdin mi?' onayı alır."""
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle
    cevap = messagebox.askquestion(
        "İndirme Kontrolü",
        "Mailine gelen excelleri 'İndirilenler' klasörüne tamamını indirdin mi?"
    )
    root.destroy()
    return cevap == "yes"


def read_all_invoice_data(excel_path: Path | str) -> Optional[pd.DataFrame]:
    """Yurtiçi Kargo'ya gönderilecek Excel'i okur."""
    excel_path = Path(excel_path)

    if not excel_path.exists():
        print(f"❌ Hata: Excel dosyası bulunamadı! ({excel_path})")
        return None

    try:
        df = pd.read_excel(excel_path)
        print(f"📄 Gönderim Excel'i yüklendi: {excel_path}")
        return df
    except Exception as exc:
        print(f"❌ Hata: Excel dosyası okunamadı! ({exc})")
        return None


# ==================== FORM DOLDURMA İŞLEMLERİ ====================

def fill_invoice_form(driver, row: pd.Series) -> None:
    """Tek bir satır için Yurtiçi Kargo e-fatura formunu doldurur."""
    wait = WebDriverWait(driver, 10)

    try:
        # Fatura no
        wait.until(EC.presence_of_element_located((By.ID, "input-invoice-number"))).send_keys(
            str(row["no"])
        )
        # Vergi / TC
        wait.until(EC.presence_of_element_located((By.ID, "input-tax-number"))).send_keys(
            str(row["avkntckn"])
        )

        # Tutar
        tutar_str = str(row["odenecek"]).replace(",", ".")
        parts = tutar_str.split(".")
        integer = parts[0]
        decimal = parts[1] if len(parts) > 1 else "00"

        wait.until(EC.presence_of_element_located((By.ID, "input-total-amount"))).send_keys(
            integer
        )
        wait.until(
            EC.presence_of_element_located((By.ID, "input-total-amount-decimals"))
        ).send_keys(decimal)

        # Mail adresi
        wait.until(EC.presence_of_element_located((By.ID, "input-email-address"))).send_keys(
            str(row["mail"])
        )

        # Aydınlatma metni onayı
        checkbox = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "clarification-check"))
        )
        driver.execute_script("arguments[0].click();", checkbox)

        # Gönder butonu
        submit = wait.until(EC.element_to_be_clickable((By.ID, "einvoice-send-button")))
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        driver.execute_script("arguments[0].click();", submit)

        # Başarı mesajı kontrolü
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
            print(f"✅ {row['no']} - Talep başarıyla iletildi (onay mesajı alındı).")
        except Exception:
            print(
                f"⚠️ {row['no']} - Gönderildi ama başarı mesajı alınamadı. "
                "Gözle kontrol gerekebilir."
            )

    except Exception as exc:
        print(f"❌ {row.get('no', 'Bilinmeyen Fatura')} - Hata oluştu: {exc}")


def process_all_rows(driver, df: pd.DataFrame) -> None:
    """Excel'deki her satır için formu doldurur."""
    for _, row in df.iterrows():
        driver.get("https://www.yurticikargo.com/tr/online-servisler/e-fatura")
        fill_invoice_form(driver, row)
        time.sleep(2)  # Hafif bekleme, siteyi boğmamak için


# ==================== ANA FONKSİYON ====================

def main() -> None:
    """Günlük Excel'i okuyup Yurtiçi Kargo e-fatura formunu otomatik doldurur."""
    # 1) Excel dosyasını bul
    excel_path = find_daily_excel()
    if excel_path is None:
        return

    # 2) Veriyi oku
    df = read_all_invoice_data(excel_path)
    if df is None or df.empty:
        print("❌ Excel verisi okunamadı ya da boş.")
        return

    # 3) Kullanıcı onayı
    if not kullanici_onayi_al():
        print("⛔ İşlem iptal edildi. Lütfen excelleri indirdikten sonra tekrar çalıştırın.")
        return

    # 4) WebDriver başlat
    service = Service(str(CHROMEDRIVER_PATH))
    driver = webdriver.Chrome(service=service)

    try:
        process_all_rows(driver, df)
    finally:
        driver.quit()
        print("🧹 Tarayıcı kapatıldı.")


if __name__ == "__main__":
    main()
