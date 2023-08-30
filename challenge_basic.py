def hitung_tip(jumlah_tagihan):
    if 50 <= jumlah_tagihan <= 300:
        tip = jumlah_tagihan * 0.15
    else:
        tip = jumlah_tagihan * 0.20
    return tip

def format_mata_uang(jumlah):
    return "{:.2f}".format(jumlah)

def hitung_total_tagihan(jumlah_tagihan, jumlah_tip):
    return jumlah_tagihan + jumlah_tip

def tampilkan_info_tagihan(jumlah_tagihan, jumlah_tip, total_jumlah):
    print(f"Tagihannya {format_mata_uang(jumlah_tagihan)}, tipnya {format_mata_uang(jumlah_tip)}, dan total nilainya {format_mata_uang(total_jumlah)}")

# Data uji
jumlah_tagihan_list = [275, 40, 430]

for jumlah_tagihan in jumlah_tagihan_list:
    tip = hitung_tip(jumlah_tagihan)
    total_jumlah = hitung_total_tagihan(jumlah_tagihan, tip)
    tampilkan_info_tagihan(jumlah_tagihan, tip, total_jumlah)
