# qr_scanner.py

def scan_qr():
    """Simulasi pemindaian QR setelah login."""
    #print("Silakan scan QR untuk melanjutkan.")
    choice = input("Silakan scan QR untuk melanjutkan. (yes/no): ").strip().lower()
    
    if choice == "yes" or choice == "y":
        print("QR berhasil dipindai.")
        return True
    elif choice == "no"or choice == "n":
        print("Proses dihentikan oleh pengguna.")
        return False
    else:
        print("Pilihan tidak valid. Harap masukkan 'yes' atau 'no'.")
        return scan_qr()
