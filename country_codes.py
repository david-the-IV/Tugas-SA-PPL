# country_codes.py

# Dictionary yang menyimpan negara sebagai kunci dan kode negara sebagai nilai
country_codes = {
    "Indonesia": "+62",
    "United States": "+1",
    "India": "+91",
    "Canada": "+1",
    # Tambahkan lebih banyak negara sesuai kebutuhan
}

# Dictionary yang menyimpan alias untuk masing-masing negara
country_aliases = {
    "Indonesia": ["Indonesia", "Indo", "indo"],
    "United States": ["United States", "US", "USA", "Amerika", "amerika", "us", "usa"],
    "India": ["India", "ind", "IND"],
    "Canada": ["Canada", "CA", "ca"],
    # Tambahkan alias lain untuk negara lain sesuai kebutuhan
}

def get_country_code(country_input):
    """Mencari kode negara berdasarkan input negara atau alias."""
    for country, aliases in country_aliases.items():
        if country_input in aliases:
            return country_codes[country]
    return None  # Jika negara tidak ditemukan
