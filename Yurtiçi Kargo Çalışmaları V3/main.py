"""Yurtiçi Kargo Otomasyon Uygulaması - V3

Bu dosya, komut satırından menülü bir arayüz sunar.
Adımları sırayla veya tek tek çalıştırabilirsin.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from config import LEGACY_AUTOMATION_PATH

from app import (
    qr_okuma,
    excel_olustur,
    mail_rpt_birlestir,
    maliyet_kontrol,
)


def run_step_1_qr_okuma() -> None:
    """1. Adım: Z:\ klasöründeki PDF’lerden QR kodlarını oku."""
    print("\n=== 1) PDF'lerden QR okuma başlıyor ===\n")
    qr_okuma.main()
    print("\n✅ 1. adım tamamlandı.\n")


def run_step_2_excel_olustur() -> Path | None:
    """2. Adım: QR sonuçlarından Yurtiçi'ne gönderilecek Excel'i oluştur."""
    print("\n=== 2) Yurtiçi'ne gönderilecek Excel oluşturuluyor ===\n")
    path = excel_olustur.create_yurtici_excel()
    if path is None:
        print("\n⚠️ Excel oluşturulamadı.\n")
    else:
        print(f"\n✅ Excel hazır: {path}\n")
    return path


def run_step_3_yurtici_legacy() -> None:
    """3. Adım: Geçici olarak V3 içindeki yurtici_site_otomasyon.py çalıştırılır."""
    print("\n=== 3) Yurtiçi sitesine otomatik talep (V2 otomasyonu) ===\n")

    v2_script = Path(LEGACY_AUTOMATION_PATH)

    if not v2_script.exists():
        print(f"❌ Otomasyon dosyası bulunamadı: {v2_script}")
        print("   Dosya yoksa V2 klasöründen geri taşımalı veya Path'i düzeltmelisin.")
        return

    print(f"▶ Eski otomasyon çalıştırılıyor: {v2_script}\n")
    try:
        subprocess.run([sys.executable, str(v2_script)], check=False)
        print("\n✅ 3. adım tamamlandı.\n")
    except Exception as exc:
        print(f"\n❌ Otomasyon çalıştırılırken hata oluştu: {exc}\n")


def run_step_4_merge_rpt() -> Path | None:
    """4. Adım: Mail ile indirilen RPT Excel dosyalarını birleştir."""
    print("\n=== 4) Mail ile gelen RPT Excel dosyaları birleştiriliyor ===\n")
    merged_path = mail_rpt_birlestir.merge_rpt_excels()
    if merged_path is None:
        print("\n⚠️ Birleştirme yapılamadı.\n")
    else:
        print(f"\n✅ 4. adım tamamlandı. Birleştirilmiş dosya: {merged_path}\n")
    return merged_path


def run_step_5_maliyet() -> None:
    """5. Adım: Maliyet kontrolü ve fatura bazlı sonuç excellerini üret."""
    print("\n=== 5) Maliyet kontrolü ve sonuç excelleri ===\n")
    maliyet_kontrol.run_maliyet_kontrol()
    print("\n✅ 5. adım tamamlandı.\n")


def show_menu() -> None:
    """Kullanıcıya metin tabanlı menü gösterir."""
    while True:
        print(
            "\n" + "=" * 60 +
            "\nYURTİÇİ KARGO OTOMASYON V3 - MENÜ\n"
            "Lütfen yapmak istediğiniz işlemi seçin:\n\n"
            "  1) PDF'lerden QR kodlarını oku ve Duzenlenen_QR_listesi.xlsx'i üret\n"
            "  2) Duzenlenen_QR_listesi.xlsx'ten masaüstüne Excel oluştur\n"
            "  3) Yurtiçi sitesine otomatik talep ilet (şimdilik V2 otomasyonu)\n"
            "  4) Mail ile gelen RPT excellerini birleştir (Downloads → V3\\MailExcels)\n"
            "  5) Maliyet kontrolü yap ve fatura bazlı sonuç excellerini üret\n"
            "  0) Çıkış\n"
        )
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            run_step_1_qr_okuma()
        elif secim == "2":
            run_step_2_excel_olustur()
        elif secim == "3":
            run_step_3_yurtici_legacy()
        elif secim == "4":
            run_step_4_merge_rpt()
        elif secim == "5":
            run_step_5_maliyet()
        elif secim == "0":
            print("\n👋 Programdan çıkılıyor...\n")
            break
        else:
            print("\n❌ Geçersiz seçim, lütfen 0–5 arasında bir değer girin.\n")


def main() -> None:
    show_menu()


if __name__ == "__main__":
    main()
