# main.py

from login import google_login, phone_login
from qr_scanner import scan_qr
from helmet_check import check_helmet
from timer import start_count_up
from trip_cost import calculate_trip_cost
from promo import check_and_apply_promo, reset_promo, promo_countdown, get_promo_discount

def main():
    print("Selamat datang di Beam.")
    print("Pilih salah satu opsi untuk melanjutkan:")
    print("1. Lanjutkan dengan Google")
    print("2. Masuk dengan nomor telepon")
    
    try:
        choice = int(input("Masukkan pilihan (1 atau 2): "))
        
        if choice == 1:
            google_login()
        elif choice == 2:
            phone_login()
        else:
            print("Pilihan tidak valid.")
            return main()  # Restart main jika pilihan tidak valid
    except ValueError:
        print("Masukkan pilihan yang valid.")
        return main()  # Restart main jika input bukan angka

    # Setelah login, pindai QR
    if scan_qr():
        # Tanyakan apakah ingin menggunakan promo sebelum memulai perjalanan
        # if get_promo_discount() > 0:
        promo_response = input("Apakah Anda ingin menggunakan promo? (yes/no): ").strip().lower()
        if promo_response == "yes" or promo_response == "y":
            # Terapkan diskon promo
            print("Promo diterapkan! Anda mendapatkan diskon biaya dasar.")
            promo_active = True
        else:
            promo_active = False
            print("Anda memilih untuk tidak menggunakan promo.")
        # else:
        #    promo_active = False
        #    print("Tidak ada promo yang tersedia.")

        # Setelah QR berhasil dipindai, periksa helm
        helmet_warning = not check_helmet()

        # Memulai timer dengan status helm, dan tangani KeyboardInterrupt
        limit_seconds = 600  # Batas waktu dalam detik (misalnya 10 menit)
        initial_battery = 23  # Baterai awal dalam persen
        seconds_elapsed = 0

        try:
            # Memulai timer dan menghitung waktu yang berlalu
            seconds_elapsed = start_count_up(limit_seconds, initial_battery, helmet_warning)
        except KeyboardInterrupt:
            print("\n\nTimer dihentikan oleh pengguna.")
        
        # Menghitung biaya perjalanan berdasarkan waktu yang ditempuh
        trip_cost = calculate_trip_cost(seconds_elapsed)

        if promo_active:
            # Jika promo aktif, terapkan diskon
            discount = get_promo_discount()
            trip_cost -= discount  # Terapkan diskon promo
            print(f"Biaya perjalanan setelah diskon promo: Rp{trip_cost}")
        else:
            print(f"Biaya perjalanan tanpa promo: Rp{trip_cost}")

        # Cek dan aktifkan promo jika durasi perjalanan kurang dari 5 menit
        check_and_apply_promo(seconds_elapsed)

        # Jika promo aktif, beri opsi untuk memulai perjalanan baru dengan promo
        if promo_countdown():
            main()  # Jalankan perjalanan lagi jika pengguna memilih "yes"
    else:
        print("Program berhenti.")

if __name__ == "__main__":
    main()
