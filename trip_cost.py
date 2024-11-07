# trip_cost.py

from promo import get_promo_discount  # Mengimpor diskon promo

def calculate_trip_cost(duration_seconds):
    """Menghitung biaya perjalanan berdasarkan durasi dalam detik."""
    base_fare = 1700
    per_minute_rate = 700

    # Cek promo untuk mengurangi biaya dasar jika aktif
    # discount = get_promo_discount()
    # base_fare -= discount  # Mengurangi biaya dasar dengan diskon promo

    # Mengonversi durasi ke menit penuh dengan pembulatan ke bawah
    minutes = duration_seconds // 60

    # Menghitung total biaya perjalanan
    total_cost = max(0, base_fare + (minutes * per_minute_rate))  # Menghindari nilai negatif
    return total_cost
