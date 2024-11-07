# googleAcc.py

from accounts import accounts  # Mengimpor daftar akun dari accounts.py
from country_codes import get_country_code  # Mengimpor kode negara dari country_codes.py

def google_login():
    """Simulasikan login Google dengan memilih akun dari daftar akun yang tersedia."""
    print("Lanjutkan dengan Google: Pilih akun untuk melanjutkan ke Beam.")
    for index, account in enumerate(accounts, start=1):
        print(f"{index}. {account}")
    
    try:
        choice = int(input("Pilih akun (masukkan nomor pilihan): "))
        if 1 <= choice <= len(accounts):
            print(f"Anda telah berhasil login dengan {accounts[choice - 1]}.")
        else:
            print("Pilihan tidak valid.")
            return google_login()
    except ValueError:
        print("Masukkan angka yang valid.")
        return google_login()

def phone_login():
    """Simulasikan login dengan nomor telepon dan memilih kode negara."""
    #print("Pilih kode negara:")
    #for country, code in country_codes.items():
    #    print(f"{country}: {code}")

    country_input = input("Masukkan nama negara atau singkatannya: ")
    #if country in country_codes:
    #    country_code = country_codes[country]
    #    phone_number = input("Masukkan nomor telepon: " + f"{country_code} ")
    #    full_number = f"{country_code}{phone_number}"
    #    print(f"Anda telah berhasil login dengan nomor telepon: {full_number}")
    #else:
    #    print("Negara tidak ditemukan.")
    #    return phone_login()
    
    country_code = get_country_code(country_input)

    if country_code:
        phone_number = input("Masukkan nomor telepon: " + f"{country_code} ")
        full_number = f"{country_code}{phone_number}"
        print(f"Anda telah berhasil login dengan nomor telepon: {full_number}")
    else:
        print("Negara tidak ditemukan. Coba lagi.")
        return phone_login()