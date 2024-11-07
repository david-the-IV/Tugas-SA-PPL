# helmet_check.py

def check_helmet():
    """Simulasi pemasangan helm sebelum melanjutkan ke timer."""
    print("Apakah Anda sudah memasang helm?")
    choice = input("Jawab (yes/no): ").strip().lower()

    if choice == "yes" or choice == "y":
        print("Helm terpasang.")
        return True
    elif choice == "no" or choice == "n":
        print("Helm tidak terpasang.")
        return False
    else:
        print("Pilihan tidak valid. Harap masukkan 'yes' atau 'no'.")
        return check_helmet()