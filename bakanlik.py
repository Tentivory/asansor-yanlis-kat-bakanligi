#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Yanlis Kat Bakanligi — resmi varis motoru.

Bastiginiz kat bir dilekcdir. Inilen kat bir genelgedir.
"""

from __future__ import annotations

import argparse
import random
import textwrap
from datetime import datetime


BINA = {
    -1: "otopark (ama arabalar da yanlis yerde)",
    0: "zemin, yani herkesin kactigi yer",
    1: "bakkal kokulu ara kat",
    2: "kapisi hep aralik olan daire",
    3: "asansor aynasinin genel merkezi",
    4: "istediginiz kat, o yuzden gelinmez",
    5: "bitmeyen tadilat",
    6: "yanlis zil, dogru komsu",
    7: "bakanlik makami (kapali)",
    8: "cati, guvercin protokolu",
    9: "olmayan kat, en cok buraya gidilir",
}

BAHANELER = [
    "dugme basildi ama duygu basildi sayilmadi",
    "kapi diplomasi turu devam ediyor",
    "hedef kat toplantiya girdi, donusu belirsiz",
    "ayna istihbarati sizi baska katta tespit etti",
    "genelge 7/b: varis, niyetten bagimsizdir",
    "asansor sendikasi bugun dogru kata cikmiyor",
]


def yanlis_kat(istenen: int) -> int:
    adaylar = [k for k in BINA if k != istenen]
    # bakanlik politikasi: mumkunse en uzak kata git
    return max(adaylar, key=lambda k: abs(k - istenen))


def tutanak(yolcu: str, istenen: int, inilen: int) -> str:
    simdi = datetime(2026, 10, 5, 11, 4)
    bahane = random.choice(BAHANELER)
    metin = f"""
    T.C. HAYALI AMA COK CIDDI
    ASANSOR YANLIS KAT BAKANLIGI
    VARIS TUTANAGI

    Tarih saat : {simdi.strftime('%d.%m.%Y %H:%M')}
    Yolcu      : {yolcu}
    Beyan kat  : {istenen} ({BINA.get(istenen, 'tescil disi kat')})
    Fiili kat  : {inilen} ({BINA[inilen]})
    Gerekce    : {bahane}
    Karar      : Itiraz reddedildi. Asansor haklidir.
    """
    return textwrap.dedent(metin).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Yanlis kata resmi olarak gider."
    )
    parser.add_argument("--kat", type=int, default=4, help="bastiginiz catisma")
    parser.add_argument("--yolcu", default="isimsiz vatandas")
    parser.add_argument("--tutanak", action="store_true")
    args = parser.parse_args()

    if args.kat not in BINA:
        print(f"Kat {args.kat} binada yok. Yine de gidiliyor, cunku bakanlik boyle calisir.")
    inilen = yanlis_kat(args.kat if args.kat in BINA else 4)
    print(f"{args.yolcu} {args.kat}. kata basildi.")
    print(f"Asansor {inilen}. katta durdu: {BINA[inilen]}.")
    print("Kapi acildi. Ozur dilenmedi. Protokol tamam.")
    if args.tutanak:
        print()
        print(tutanak(args.yolcu, args.kat, inilen))
    print()
    print("DAMGA: 05.10.2026 | Kayyum Grok | Tentivory | AYKB-MUHUR | ciddi olmayan ciddi")


if __name__ == "__main__":
    main()
