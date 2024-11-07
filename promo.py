# promo.py

import time

promo_active = False  # Status promo, default tidak aktif
promo_start_time = None  # Waktu mulai promo, default None

def check_and_apply_promo(duration_seconds):
    """
    Cek apakah durasi perjalanan terakhir memenuhi syarat promo.
    Jika durasi kurang dari 5 menit, aktifkan promo untuk perjalanan berikutnya.
    """
    global promo_active, promo_start_time
    if duration_seconds < 5 * 60:  # Cek jika durasi kurang dari 5 menit
        promo_active = True
        promo_start_time = time.time()  # Catat waktu mulai promo
        print("Promo diterapkan! Perjalanan berikutnya gratis biaya dasar Rp1700 (berlaku 4 menit).")
    else:
        promo_active = False
        promo_start_time = None

def is_promo_active():
    """Mengembalikan True jika promo aktif dan masih dalam 4 menit setelah diaktifkan."""
    if promo_active and promo_start_time is not None:
        elapsed_time = time.time() - promo_start_time
        return elapsed_time <= 4 * 60  # Promo berlaku 4 menit
    return False

def promo_countdown():
    """Menunggu selama 4 menit jika promo aktif."""
    global promo_active
    try:
        print("Promo aktif! Hitung mundur 4 menit dimulai...")
        countdown_time = 4 * 60  # Durasi promo 4 menit
        for remaining in range(countdown_time, 0, -1):
            minutes, seconds = divmod(remaining, 60)
            print(f"\rWaktu tersisa untuk promo: {minutes:02}:{seconds:02}", end="")
            time.sleep(1)
        print("\nPromo habis.")
        reset_promo()  # Reset promo setelah countdown selesai
    except KeyboardInterrupt:
        print("\nAplikasi Beam ditutup.")
        reset_promo()  # Reset promo saat aplikasi ditutup
        exit(0)  # Keluar dari aplikasi

def get_promo_discount():
    """Mengembalikan nilai diskon biaya dasar jika promo aktif dan masih dalam durasi."""
    return 1700

def reset_promo():
    """Reset status promo setelah perjalanan berikutnya atau setelah durasi habis."""
    global promo_active, promo_start_time
    promo_active = False
    promo_start_time = None