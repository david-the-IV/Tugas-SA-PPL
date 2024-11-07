# timer.py

import time

def start_count_up(limit_seconds, initial_battery, helmet_warning=False):
    """Fungsi untuk menjalankan timer count-up dengan status baterai dan peringatan helm."""
    battery = initial_battery  # Set initial battery level
    seconds_elapsed = 0
    try:
        while battery >= 20 and seconds_elapsed <= limit_seconds:
            # Menghitung menit dan detik dari waktu yang sudah berlalu
            minutes = seconds_elapsed // 60
            seconds = seconds_elapsed % 60
            warning_message = " | WARNING: Helm tidak terpasang!" if helmet_warning else ""
            
            # Menampilkan waktu dan status baterai dengan atau tanpa peringatan
            print(f"Time: {minutes:02}:{seconds:02} | Battery: {battery}%{warning_message}   ", end="\r", flush=True)
            
            # Update timer dan baterai
            time.sleep(1)
            seconds_elapsed += 1

            # Kurangi baterai setiap 5 detik
            if seconds_elapsed % 5 == 0:
                battery -= 1

        # Menampilkan pesan jika baterai mencapai 20% atau waktu habis
        if battery < 20:
            print("\nSepeda listrik Beam terkunci! Menunggu untuk pengisian daya.")
        else:
            print("\nTime limit reached.")
        
        return seconds_elapsed  # Mengembalikan waktu yang telah berlalu

    except KeyboardInterrupt:
        print("\nAplikasi Beam ditutup.")
        return seconds_elapsed  # Kembalikan waktu yang berlalu jika dihentikan oleh pengguna
