#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==========================================================
  CERDAS CERMAT MATEMATIKA  -  Numerasi Bilangan Desimal
  Kelas 6 SD  |  5 Kelompok  |  20 Soal Uraian  (versi ceria)
==========================================================
Cara menjalankan :  python cerdas_cermat.py
Kebutuhan        :  Python 3.8+ (tkinter sudah bawaan Python)

Cara bermain:
  1. Klik nomor soal (1-20) -> soal muncul + hitung mundur waktu.
  2. Klik "TAMPILKAN JAWABAN" untuk melihat kunci + pembahasan.
  3. Klik tombol kelompok yang menjawab benar -> maskot kelompok melompat maju.
  4. Kelompok pertama yang mencapai skor 5 menjadi JUARA (ada animasi pemenang).
Tips: klik nama kelompok untuk mengganti nama, klik "-1" untuk koreksi skor.
"""
import math
import random
import sys
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, simpledialog

# ----------------------------------------------------------------- PENGATURAN
MAX_SKOR = 5          # skor maksimal untuk menang
WAKTU_SOAL = 90       # detik per soal (hitung mundur)
NAMA_AWAL = ["Kelompok 1", "Kelompok 2", "Kelompok 3",
             "Kelompok 4", "Kelompok 5"]

# ------------------------------------------------------------------ 20 SOAL
# (soal, jawaban, pembahasan)
SOAL = [
    ("Ibu membeli 2,5 kg jeruk dan 1,75 kg apel di pasar. "
     "Berapa kg seluruh buah yang dibeli Ibu?",
     "4,25 kg",
     "2,5 + 1,75 = 4,25 kg"),

    ("Tinggi badan Rani 1,45 m dan tinggi badan Dito 1,38 m. "
     "Berapa meter selisih tinggi mereka?",
     "0,07 meter (= 7 cm)",
     "1,45 - 1,38 = 0,07 meter"),

    ("Sebuah pita panjangnya 3,5 meter. Pita itu dipotong 1,25 meter untuk "
     "membuat hiasan. Berapa meter sisa pita?",
     "2,25 meter",
     "3,5 - 1,25 = 2,25 meter"),

    ("Harga 1 kg gula adalah Rp14.500. Pak Heri membeli 2 kg gula dan membayar "
     "dengan uang Rp50.000. Berapa rupiah uang kembaliannya?",
     "Rp21.000",
     "Harga 2 kg = 2 x 14.500 = 29.000\nKembalian = 50.000 - 29.000 = 21.000"),

    ("Sebuah botol berisi 1,5 liter air. Ada 4 botol yang isinya sama. "
     "Berapa liter air seluruhnya?",
     "6 liter",
     "4 x 1,5 = 6 liter"),

    ("Teh sebanyak 6 liter dituang ke dalam gelas-gelas. Setiap gelas berisi "
     "0,25 liter. Berapa gelas yang dibutuhkan?",
     "24 gelas",
     "6 : 0,25 = 600 : 25 = 24 gelas\n(Cara lain: 1 liter = 4 gelas, jadi 6 x 4 = 24)"),

    ("Andi berlari 0,8 km setiap pagi. Berapa km jarak yang ia tempuh "
     "selama 5 hari?",
     "4 km",
     "5 x 0,8 = 4 km"),

    ("Urutkan bilangan berikut dari yang TERKECIL ke TERBESAR:\n"
     "0,5 ;  0,45 ;  0,505 ;  0,055",
     "0,055 ; 0,45 ; 0,5 ; 0,505",
     "Samakan menjadi tiga angka di belakang koma:\n"
     "0,500 ; 0,450 ; 0,505 ; 0,055\nUrutan: 0,055 < 0,450 < 0,500 < 0,505"),

    ("Ubahlah pecahan 3/4 menjadi bilangan desimal, kemudian tambahkan "
     "dengan 0,5. Berapa hasilnya?",
     "1,25",
     "3/4 = 0,75\n0,75 + 0,5 = 1,25"),

    ("Dina membeli 3 buku tulis seharga Rp4.500 per buku dan sebuah pensil "
     "seharga Rp2.750. Berapa rupiah yang harus ia bayar?",
     "Rp16.250",
     "Buku = 3 x 4.500 = 13.500\nTotal = 13.500 + 2.750 = 16.250"),

    ("Pak Tani memanen 12,5 kg cabai pada pagi hari dan 8,75 kg pada sore hari. "
     "Jika 15 kg cabai sudah dijual, berapa kg cabai yang tersisa?",
     "6,25 kg",
     "Total panen = 12,5 + 8,75 = 21,25 kg\nSisa = 21,25 - 15 = 6,25 kg"),

    ("Nilai tiga kali ulangan matematika Budi adalah 7,5 ; 8,0 ; dan 8,5. "
     "Berapa nilai rata-ratanya?",
     "8,0",
     "Jumlah = 7,5 + 8,0 + 8,5 = 24\nRata-rata = 24 : 3 = 8,0"),

    ("Sebuah motor menempuh 40 km dengan 1 liter bensin. Berapa km jarak yang "
     "dapat ditempuh dengan 2,5 liter bensin?",
     "100 km",
     "2,5 x 40 = 100 km"),

    ("Kain sepanjang 2,4 meter dibagi sama rata untuk 3 anak. "
     "Berapa meter kain yang diterima setiap anak?",
     "0,8 meter",
     "2,4 : 3 = 0,8 meter"),

    ("Sebuah taman berbentuk persegi dengan panjang sisi 1,5 meter. "
     "Berapa m² luas taman tersebut?",
     "2,25 m²",
     "Luas persegi = sisi x sisi\n1,5 x 1,5 = 2,25 m²"),

    ("Rina menabung Rp2.500 setiap hari selama 6 hari. Uang itu dipakai untuk "
     "membeli buku seharga Rp12.000. Berapa rupiah sisa uang Rina?",
     "Rp3.000",
     "Tabungan = 6 x 2.500 = 15.000\nSisa = 15.000 - 12.000 = 3.000"),

    ("Bu Ani menimbang beras dan hasilnya 3,76 kg. Jika dibulatkan ke "
     "persepuluhan terdekat, berapa kg beras Bu Ani?",
     "3,8 kg",
     "Angka perseratusan adalah 6 (lebih dari 5), maka dibulatkan ke atas.\n"
     "3,76 menjadi 3,8 kg"),

    ("Perhatikan pola bilangan berikut:\n0,5 ;  1,0 ;  1,5 ;  2,0 ; ...\n"
     "Berapakah bilangan pada urutan ke-8?",
     "4,0",
     "Pola: ditambah 0,5 setiap kali.\n"
     "Urutan ke-8 = 8 x 0,5 = 4,0"),

    ("Sebuah buku cerita berharga Rp20.000 mendapat potongan harga 0,1 bagian "
     "dari harganya. Berapa rupiah yang harus dibayar?",
     "Rp18.000",
     "Potongan = 0,1 x 20.000 = 2.000\nBayar = 20.000 - 2.000 = 18.000"),

    ("Keran mengalirkan 1,5 liter air setiap menit. Setelah 8 menit, air itu "
     "dimasukkan ke ember berkapasitas 20 liter. Berapa liter lagi yang "
     "dibutuhkan agar ember penuh?",
     "8 liter",
     "Air mengalir = 8 x 1,5 = 12 liter\nKekurangan = 20 - 12 = 8 liter"),
]

# ------------------------------------------------------------------- TEMA
BG = "#CDEBFF"          # langit
WHITE = "#FFFFFF"
INK = "#2B2D42"         # teks gelap
SOFT = "#5C6B8A"
BORDER = "#9ED2FF"
YELLOW = "#FFD43B"
GREEN = "#2FB36D"
RAINBOW = ["#FF6B6B", "#FF9F45", "#4D96FF", "#2FB36D", "#9B72F2", "#FF6B9D"]

# warna jalur tiap kelompok: (utama, latar muda)
TEAMS = [("#FF9F45", "#FFF0E0"),   # kucing
         ("#4D96FF", "#E4F0FF"),   # panda
         ("#FF6B9D", "#FFE6EF"),   # kelinci
         ("#2FB36D", "#E0F6E8"),   # katak
         ("#9B72F2", "#EEE7FF")]   # burung hantu
MASCOTS = ["cat", "panda", "bunny", "frog", "owl"]
N = len(TEAMS)                     # jumlah kelompok

# kartu nomor soal: (warna, warna teks)
NUM_COLORS = [("#FF6B6B", WHITE), ("#FF9F45", WHITE), ("#FFD43B", "#5A4300"),
              ("#4D96FF", WHITE), ("#9B72F2", WHITE), ("#FF6B9D", WHITE)]

if sys.platform.startswith("win"):
    FONT = "Trebuchet MS"
elif sys.platform == "darwin":
    FONT = "Arial Rounded MT Bold"
else:
    FONT = "DejaVu Sans"


def F(size, weight="bold"):
    return (FONT, size, weight)


# ------------------------------------------------------------- GAMBAR VEKTOR
def rrect(c, x1, y1, x2, y2, r, **kw):
    """Persegi panjang sudut membulat."""
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2,
           x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


def star_pts(cx, cy, r_out, r_in, rot=-math.pi / 2):
    pts = []
    for k in range(10):
        a = rot + k * math.pi / 5
        rad = r_out if k % 2 == 0 else r_in
        pts += [cx + rad * math.cos(a), cy + rad * math.sin(a)]
    return pts


def draw_mascot(c, kind, cx, cy, r, tag, glow=0, happy=False):
    """Maskot lucu: kucing, panda, kelinci, katak, burung hantu."""
    dark = "#3B2C2C"
    lw = max(2, int(r * 0.07))
    if glow > 0:  # cincin + bintang kilau saat skor naik
        g = r * 1.2 + glow * 0.25
        c.create_oval(cx - g, cy - g, cx + g, cy + g, outline=YELLOW,
                      width=4, tags=tag)
        for k in range(4):
            a = glow * 0.12 + k * math.pi / 2
            sx, sy = cx + g * math.cos(a), cy + g * math.sin(a)
            c.create_polygon(star_pts(sx, sy, 8, 3.5), fill=YELLOW,
                             outline="", tags=tag)

    # ---- telinga / hiasan kepala
    if kind in ("cat", "owl"):
        fur, inner = ("#FFA94D", "#FFC9C9") if kind == "cat" else \
                     ("#9B72F2", "#D6C5FF")
        for sgn in (-1, 1):
            c.create_polygon(cx + sgn * 0.88 * r, cy - 0.1 * r,
                             cx + sgn * 0.78 * r, cy - 1.18 * r,
                             cx + sgn * 0.2 * r, cy - 0.78 * r,
                             fill=fur, outline=dark, width=lw, tags=tag)
            c.create_polygon(cx + sgn * 0.74 * r, cy - 0.3 * r,
                             cx + sgn * 0.70 * r, cy - 0.92 * r,
                             cx + sgn * 0.33 * r, cy - 0.68 * r,
                             fill=inner, outline="", tags=tag)
    elif kind == "panda":
        fur = "#FFFFFF"
        for sgn in (-1, 1):
            ex, ey, er = cx + sgn * 0.72 * r, cy - 0.78 * r, 0.36 * r
            c.create_oval(ex - er, ey - er, ex + er, ey + er,
                          fill=dark, outline=dark, tags=tag)
    elif kind == "frog":
        fur = "#6BCB77"
    else:  # bunny
        fur, inner = "#FFE3EE", "#FF9BB8"
        for sgn in (-1, 1):
            ex = cx + sgn * 0.45 * r
            c.create_oval(ex - 0.24 * r, cy - 1.6 * r, ex + 0.24 * r, cy - 0.5 * r,
                          fill=fur, outline=dark, width=lw, tags=tag)
            c.create_oval(ex - 0.12 * r, cy - 1.42 * r, ex + 0.12 * r, cy - 0.75 * r,
                          fill=inner, outline="", tags=tag)

    # ---- wajah
    c.create_oval(cx - r, cy - 0.92 * r, cx + r, cy + 0.92 * r, fill=fur,
                  outline=dark, width=lw, tags=tag)
    if kind == "owl":  # bulu perut / wajah bagian bawah
        c.create_oval(cx - 0.55 * r, cy + 0.1 * r, cx + 0.55 * r, cy + 0.8 * r,
                      fill="#E6DAFF", outline="", tags=tag)
    if kind == "frog":  # mata besar menonjol di atas kepala
        for sgn in (-1, 1):
            ex, ey, er = cx + sgn * 0.5 * r, cy - 0.72 * r, 0.34 * r
            c.create_oval(ex - er, ey - er, ex + er, ey + er, fill=WHITE,
                          outline=dark, width=lw, tags=tag)

    # ---- mata
    for sgn in (-1, 1):
        ex, ey = cx + sgn * 0.4 * r, cy - 0.06 * r
        k = 1.0
        if kind == "frog":
            ex, ey, k = cx + sgn * 0.5 * r, cy - 0.72 * r, 1.0
        if kind == "owl":
            ey, k = cy - 0.12 * r, 1.0
            c.create_oval(ex - 0.33 * r, ey - 0.33 * r, ex + 0.33 * r, ey + 0.33 * r,
                          fill=WHITE, outline=dark, width=max(2, lw - 1), tags=tag)
        if kind == "panda":
            c.create_oval(ex - 0.25 * r, ey - 0.34 * r, ex + 0.25 * r, ey + 0.34 * r,
                          fill=dark, outline="", tags=tag)
        if happy:
            c.create_arc(ex - 0.16 * r * k, ey - 0.12 * r * k,
                         ex + 0.16 * r * k, ey + 0.2 * r * k,
                         start=20, extent=140, style="arc",
                         outline=WHITE if kind == "panda" else dark,
                         width=max(3, lw), tags=tag)
        else:
            if kind not in ("owl", "frog"):
                c.create_oval(ex - 0.15 * r * k, ey - 0.17 * r * k,
                              ex + 0.15 * r * k, ey + 0.17 * r * k,
                              fill=WHITE, outline="", tags=tag)
            pr = 0.14 if kind in ("owl", "frog") else 0.08
            c.create_oval(ex - pr * r * k, ey - pr * 1.25 * r * k,
                          ex + pr * r * k, ey + pr * 1.25 * r * k,
                          fill=dark, outline="", tags=tag)
            c.create_oval(ex - 0.02 * r, ey - 0.09 * r, ex + 0.04 * r, ey - 0.03 * r,
                          fill=WHITE, outline="", tags=tag)

    # ---- pipi
    for sgn in (-1, 1):
        px, py = cx + sgn * 0.68 * r, cy + 0.32 * r
        c.create_oval(px - 0.15 * r, py - 0.1 * r, px + 0.15 * r, py + 0.1 * r,
                      fill="#FF9BB3", outline="", tags=tag)

    # ---- hidung / paruh / mulut
    if kind == "owl":
        c.create_polygon(cx - 0.15 * r, cy + 0.08 * r, cx + 0.15 * r, cy + 0.08 * r,
                         cx, cy + 0.42 * r, fill="#FF9F45", outline=dark,
                         width=max(1, lw - 1), tags=tag)
    elif kind == "frog":
        for sgn in (-1, 1):
            c.create_oval(cx + sgn * 0.12 * r - 0.04 * r, cy + 0.02 * r,
                          cx + sgn * 0.12 * r + 0.04 * r, cy + 0.1 * r,
                          fill=dark, outline="", tags=tag)
        if happy:
            c.create_arc(cx - 0.5 * r, cy - 0.05 * r, cx + 0.5 * r, cy + 0.65 * r,
                         start=200, extent=140, style="chord", fill="#C0392B",
                         outline=dark, width=lw, tags=tag)
        else:
            c.create_arc(cx - 0.5 * r, cy - 0.1 * r, cx + 0.5 * r, cy + 0.6 * r,
                         start=200, extent=140, style="arc", outline=dark,
                         width=max(2, lw), tags=tag)
    else:
        c.create_oval(cx - 0.1 * r, cy + 0.1 * r, cx + 0.1 * r, cy + 0.26 * r,
                      fill="#FF6B8B" if kind != "panda" else dark, outline="",
                      tags=tag)
        if happy:
            c.create_arc(cx - 0.3 * r, cy + 0.15 * r, cx + 0.3 * r, cy + 0.65 * r,
                         start=200, extent=140, style="chord", fill="#C0392B",
                         outline=dark, width=lw, tags=tag)
        else:
            for sgn in (-1, 1):
                c.create_arc(cx - 0.2 * r + sgn * 0.1 * r, cy + 0.17 * r,
                             cx + 0.2 * r + sgn * 0.1 * r, cy + 0.5 * r,
                             start=200, extent=140, style="arc", outline=dark,
                             width=max(2, lw - 1), tags=tag)
    if kind == "cat":
        for sgn in (-1, 1):
            for dy in (-0.05, 0.12):
                c.create_line(cx + sgn * 0.78 * r, cy + (0.3 + dy) * r,
                              cx + sgn * 1.2 * r, cy + (0.24 + dy * 2.2) * r,
                              fill=dark, width=max(1, lw - 1), tags=tag)


def draw_trophy(c, cx, cy, s, tag):
    """Piala emas."""
    gold, light, deep = "#FFC933", "#FFF3B0", "#E09F00"
    for sgn in (-1, 1):
        c.create_arc(cx + sgn * 0.4 * s if sgn > 0 else cx - 1.05 * s, cy - 0.75 * s,
                     cx + 1.05 * s if sgn > 0 else cx - 0.4 * s, cy - 0.05 * s,
                     start=270 if sgn > 0 else 90, extent=180, style="arc",
                     outline=gold, width=max(4, int(s * 0.13)), tags=tag)
    cup = [(-0.62, -0.9), (0.62, -0.9), (0.55, -0.1), (0.3, 0.3),
           (-0.3, 0.3), (-0.55, -0.1)]
    c.create_polygon([v for px, py in cup for v in (cx + px * s, cy + py * s)],
                     fill=gold, outline=deep, width=3, tags=tag)
    c.create_rectangle(cx - 0.12 * s, cy + 0.3 * s, cx + 0.12 * s, cy + 0.65 * s,
                       fill=deep, outline="", tags=tag)
    c.create_rectangle(cx - 0.48 * s, cy + 0.65 * s, cx + 0.48 * s, cy + 0.9 * s,
                       fill=gold, outline=deep, width=3, tags=tag)
    c.create_polygon(star_pts(cx, cy - 0.42 * s, 0.32 * s, 0.14 * s),
                     fill=light, outline="", tags=tag)


def hover_button(parent, text, bg, fg, hover, command, font, padx=18, pady=8):
    b = tk.Button(parent, text=text, bg=bg, fg=fg, activebackground=hover,
                  activeforeground=fg, relief="flat", bd=0, cursor="hand2",
                  font=font, padx=padx, pady=pady, command=command)
    b.bind("<Enter>", lambda e: b.config(bg=hover))
    b.bind("<Leave>", lambda e: b.config(bg=bg))
    return b


def darker(hexcol, f=0.86):
    h = hexcol.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f))


# ===================================================================== APP
class App:
    def __init__(self, root):
        self.root = root
        root.title("Cerdas Cermat Matematika - Desimal Kelas 6")
        root.geometry("1360x790")
        root.minsize(1100, 700)
        root.configure(bg=BG)

        self.names = list(NAMA_AWAL)
        self.score = [0] * N
        self.cur = [0.0] * N     # posisi animasi maskot
        self.glow = [0] * N
        self.phase = 0
        self.done = set()
        self.animating = False
        self.winner = None
        self.overlay = None
        self.win_job = None
        self.win_t = 0
        self.confetti = []
        self.balloons = []
        self.cards = []

        self._build_header()
        self._build_body()
        self._bind_track()
        self.root.after(200, self.draw_track)

    # --------------------------------------------------------------- LAYOUT
    def _build_header(self):
        self.head = tk.Canvas(self.root, bg=WHITE, height=96, highlightthickness=0)
        self.head.pack(fill="x")
        stripe = tk.Frame(self.root, height=7, bg=BG)
        stripe.pack(fill="x")
        for col in RAINBOW:
            tk.Frame(stripe, bg=col, height=7).pack(side="left", fill="x",
                                                    expand=True)
        self.btn_reset = hover_button(self.head, "↻  ULANGI LOMBA", "#FF6B6B",
                                      WHITE, "#E55050", self.reset, F(11))
        self.head.bind("<Configure>", lambda e: self.draw_header())

    def draw_header(self):
        c = self.head
        c.delete("all")
        W = c.winfo_width()
        rnd = random.Random(7)
        for _ in range(26):  # titik-titik konfeti dekorasi
            x, y = rnd.uniform(0, W), rnd.uniform(0, 96)
            r = rnd.uniform(3, 7)
            c.create_oval(x - r, y - r, x + r, y + r,
                          fill=rnd.choice(RAINBOW), outline="", stipple="gray50")
        # judul pelangi
        title = "CERDAS CERMAT MATEMATIKA"
        fnt = tkfont.Font(family=FONT, size=29, weight="bold")
        total = sum(fnt.measure(ch) for ch in title)
        x = 34
        for k, ch in enumerate(title):
            if ch != " ":
                c.create_text(x + 2, 40 + 2, text=ch, anchor="w", font=fnt,
                              fill="#E3EAF5")
                c.create_text(x, 40, text=ch, anchor="w", font=fnt,
                              fill=RAINBOW[k % len(RAINBOW)])
            x += fnt.measure(ch)
        c.create_text(36, 76, text="Numerasi Bilangan Desimal  •  Kelas 6",
                      anchor="w", font=F(12, "normal"), fill=SOFT)
        c.create_window(W - 28, 48, window=self.btn_reset, anchor="e")

    def _build_body(self):
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=20, pady=14)
        body.columnconfigure(0, weight=2, uniform="a")
        body.columnconfigure(1, weight=3, uniform="a")
        body.rowconfigure(0, weight=1)

        # --- panel soal
        lp = tk.Frame(body, bg=WHITE, highlightbackground=BORDER,
                      highlightthickness=4)
        lp.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
        tk.Label(lp, text="✨ PILIH NOMOR SOAL ✨", bg=WHITE, fg="#9B72F2",
                 font=F(16)).pack(pady=(16, 2))
        self.lbl_prog = tk.Label(lp, text="", bg=WHITE, fg=SOFT,
                                 font=F(11, "normal"))
        self.lbl_prog.pack(pady=(0, 10))

        grid = tk.Frame(lp, bg=WHITE)
        grid.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        cols = 5
        for i in range(cols):
            grid.columnconfigure(i, weight=1, uniform="c")
        for r in range((len(SOAL) + cols - 1) // cols):
            grid.rowconfigure(r, weight=1, uniform="r")
        for n in range(len(SOAL)):
            b = tk.Button(grid, text=str(n + 1), font=F(22), relief="flat", bd=0,
                          cursor="hand2",
                          command=lambda k=n: self.open_question(k))
            b.grid(row=n // cols, column=n % cols, sticky="nsew", padx=5, pady=5)
            self.cards.append(b)
        self.refresh_cards()

        # --- papan lomba
        rp = tk.Frame(body, bg=WHITE, highlightbackground=BORDER,
                      highlightthickness=4)
        rp.grid(row=0, column=1, sticky="nsew")
        tk.Label(rp, text="★ PAPAN PERLOMBAAN ★", bg=WHITE, fg="#FF6B9D",
                 font=F(16)).pack(pady=(16, 0))
        tk.Label(rp, text=f"Siapa lebih dulu mencapai {MAX_SKOR} jawaban benar, "
                          f"dialah juara!", bg=WHITE, fg=SOFT,
                 font=F(11, "normal")).pack(pady=(0, 6))
        self.track = tk.Canvas(rp, bg=WHITE, highlightthickness=0)
        self.track.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.track.bind("<Configure>", lambda e: self.draw_track())

    def _bind_track(self):
        c = self.track
        for i in range(N):
            c.tag_bind(f"name{i}", "<Button-1>", lambda e, k=i: self.rename(k))
            c.tag_bind(f"minus{i}", "<Button-1>", lambda e, k=i: self.minus(k))
            for t in (f"name{i}", f"minus{i}"):
                c.tag_bind(t, "<Enter>", lambda e: c.config(cursor="hand2"))
                c.tag_bind(t, "<Leave>", lambda e: c.config(cursor=""))

    # ------------------------------------------------------------- PAPAN
    def draw_track(self):
        c = self.track
        c.delete("all")
        W, H = c.winfo_width(), c.winfo_height()
        if W < 120 or H < 120:
            return
        pad = 8
        lane_h = (H - pad * (N + 1)) / N
        left, right = 215, W - 62
        step = (right - left) / MAX_SKOR
        for i in range(N):
            color, tint = TEAMS[i]
            top = pad + i * (lane_h + pad)
            bot = top + lane_h
            cy = (top + bot) / 2 + lane_h * 0.06
            rrect(c, 6, top, W - 6, bot, 22, fill=tint, outline=color, width=3)
            # nama + skor
            c.create_text(24, cy - lane_h * 0.26, text=self.names[i], anchor="w",
                          fill=INK, font=F(15), tags=f"name{i}")
            c.create_text(24, cy + lane_h * 0.02,
                          text=f"Skor  {self.score[i]} / {MAX_SKOR}",
                          anchor="w", fill=darker(color, 0.8), font=F(12))
            c.create_text(24, cy + lane_h * 0.28, text="ganti nama ✎", anchor="w",
                          fill=SOFT, font=F(8, "normal"), tags=f"name{i}")
            c.create_text(W - 20, top + 12, text="-1", anchor="e", fill=SOFT,
                          font=F(10), tags=f"minus{i}")
            # jalur putus-putus
            c.create_line(left - 24, cy + 4, right, cy + 4, fill=color, width=5,
                          dash=(2, 9), capstyle="round")
            for n in range(1, MAX_SKOR + 1):
                x = left + n * step
                ok = self.score[i] >= n
                c.create_oval(x - 13, cy + 4 - 13, x + 13, cy + 4 + 13,
                              fill=color if ok else WHITE, outline=color, width=3)
                c.create_text(x, cy + 4, text=str(n), fill=WHITE if ok else color,
                              font=F(10))
            # bendera finish
            fx = right + 34
            c.create_line(fx, cy - 24, fx, cy + 20, fill=INK, width=3)
            c.create_polygon(fx, cy - 24, fx + 22, cy - 16, fx, cy - 8,
                             fill="#FF6B6B", outline="")
            # maskot (melompat saat bergerak)
            r = max(16, min(32, lane_h * 0.27))
            x = left + self.cur[i] * step
            moving = abs(self.score[i] - self.cur[i]) > 0.02
            hop = -abs(math.sin(self.phase * 0.55)) * 10 if moving else \
                  math.sin(self.phase * 0.12 + i) * 1.2
            draw_mascot(c, MASCOTS[i], x, cy - r * 0.15 + hop, r, f"mascot{i}",
                        glow=self.glow[i], happy=self.glow[i] > 0)

    def start_animation(self):
        if self.animating:
            return
        self.animating = True
        self._anim()

    def _anim(self):
        moving = False
        self.phase += 1
        for i in range(N):
            d = self.score[i] - self.cur[i]
            if abs(d) > 0.02:
                self.cur[i] += d * 0.12 + (0.012 if d > 0 else -0.012)
                moving = True
            else:
                self.cur[i] = float(self.score[i])
            if self.glow[i] > 0:
                self.glow[i] -= 1
                moving = True
        self.draw_track()
        if moving:
            self.root.after(25, self._anim)
        else:
            self.animating = False
            self.check_winner()

    # ------------------------------------------------------------ SOAL
    def refresh_cards(self):
        for n, b in enumerate(self.cards):
            if n in self.done:
                b.config(bg=GREEN, fg=WHITE, activebackground=GREEN,
                         activeforeground=WHITE,
                         text=f"{n + 1}\n✓", font=F(16))
            else:
                bg, fg = NUM_COLORS[n % len(NUM_COLORS)]
                b.config(bg=bg, fg=fg, activebackground=darker(bg),
                         activeforeground=fg, text=str(n + 1), font=F(22))
        self.lbl_prog.config(text=f"Soal selesai: {len(self.done)} / {len(SOAL)}")

    def open_question(self, idx):
        if self.winner is not None:
            return
        soal, jawab, bahas = SOAL[idx]
        main, ink = NUM_COLORS[idx % len(NUM_COLORS)]
        dlg = tk.Toplevel(self.root)
        dlg.title(f"Soal No. {idx + 1}")
        dlg.configure(bg="#FFF8E1")
        dlg.transient(self.root)
        w, h = 1000, 690
        x = self.root.winfo_rootx() + (self.root.winfo_width() - w) // 2
        y = self.root.winfo_rooty() + (self.root.winfo_height() - h) // 2
        dlg.geometry(f"{w}x{h}+{max(x, 0)}+{max(y, 0)}")
        state = {"left": WAKTU_SOAL, "job": None}

        def close():
            if state["job"]:
                try:
                    dlg.after_cancel(state["job"])
                except tk.TclError:
                    pass
            try:
                dlg.destroy()
            except tk.TclError:
                pass

        dlg._close = close
        dlg.protocol("WM_DELETE_WINDOW", close)

        # bar atas berwarna
        top = tk.Frame(dlg, bg=main)
        top.pack(fill="x")
        tk.Label(top, text=f"SOAL NO. {idx + 1}", bg=main, fg=ink,
                 font=F(26)).pack(side="left", padx=26, pady=14)
        lbl_t = tk.Label(top, text="", bg=main, fg=ink, font=F(22))
        lbl_t.pack(side="right", padx=26)

        def tick():
            m, s = divmod(state["left"], 60)
            if state["left"] <= 0:
                lbl_t.config(text="⏰ WAKTU HABIS!", fg="#B00020", bg=WHITE)
                return
            lbl_t.config(text=f"⏱ {m:02d}:{s:02d}",
                         fg="#B00020" if state["left"] <= 10 else ink)
            state["left"] -= 1
            state["job"] = dlg.after(1000, tick)

        tick()

        # kartu soal
        card = tk.Frame(dlg, bg=WHITE, highlightbackground=main,
                        highlightthickness=4)
        card.pack(fill="x", padx=28, pady=(22, 10))
        tk.Label(card, text=soal, bg=WHITE, fg=INK, font=F(21, "normal"),
                 wraplength=900, justify="left").pack(padx=24, pady=24, anchor="w")

        area = tk.Frame(dlg, bg="#FFF8E1")
        area.pack(fill="both", expand=True, padx=28)

        ans = tk.Frame(area, bg="#DDF8E6", highlightbackground=GREEN,
                       highlightthickness=3)
        tk.Label(ans, text="✓ JAWABAN", bg="#DDF8E6", fg="#1F8A55",
                 font=F(12)).pack(anchor="w", padx=20, pady=(12, 0))
        tk.Label(ans, text=jawab, bg="#DDF8E6", fg="#14683F",
                 font=F(28)).pack(anchor="w", padx=20)
        tk.Label(ans, text="Pembahasan:\n" + bahas, bg="#DDF8E6", fg=INK,
                 font=F(13, "normal"), justify="left",
                 wraplength=900).pack(anchor="w", padx=20, pady=(4, 12))

        award = tk.Frame(area, bg="#FFF8E1")
        if idx in self.done:
            tk.Label(award, text="Soal ini sudah dinilai sebelumnya.",
                     bg="#FFF8E1", fg=SOFT, font=F(12, "normal")).pack(pady=8)
            hover_button(award, "TUTUP", "#4D96FF", WHITE, "#3A7EE0", close,
                         F(12)).pack(pady=4)
        else:
            tk.Label(award, text="Kelompok mana yang menjawab BENAR?",
                     bg="#FFF8E1", fg=INK, font=F(14)).pack(pady=(8, 8))
            row = tk.Frame(award, bg="#FFF8E1")
            row.pack(fill="x")
            for i in range(N):
                row.columnconfigure(i, weight=1, uniform="tim")
                hover_button(row, self.names[i], TEAMS[i][0], WHITE,
                             darker(TEAMS[i][0], 0.88),
                             lambda k=i: self.award(k, idx, dlg),
                             F(13), padx=6, pady=12).grid(row=0, column=i,
                                                          sticky="ew", padx=5)
            hover_button(award, "Tidak ada yang benar", "#8D99AE", WHITE, "#6F7B93",
                         lambda: self.no_winner(idx, dlg), F(11),
                         pady=6).pack(pady=(10, 0))

        def reveal():
            btn.pack_forget()
            ans.pack(fill="x", pady=(0, 6))
            award.pack(fill="x")

        btn = hover_button(area, "TAMPILKAN JAWABAN", YELLOW, "#5A4300", "#FFC400",
                           reveal, F(17), padx=32, pady=14)
        btn.pack(pady=26)

        try:
            dlg.wait_visibility()
            dlg.grab_set()
        except tk.TclError:
            pass

    def award(self, team, idx, dlg):
        dlg._close()
        self.done.add(idx)
        self.score[team] = min(MAX_SKOR, self.score[team] + 1)
        self.glow[team] = 36
        self.refresh_cards()
        self.start_animation()

    def no_winner(self, idx, dlg):
        dlg._close()
        self.done.add(idx)
        self.refresh_cards()

    # -------------------------------------------------------- PENGATURAN
    def rename(self, i):
        if self.winner is not None:
            return
        n = simpledialog.askstring("Ganti Nama", "Nama kelompok:",
                                   initialvalue=self.names[i], parent=self.root)
        if n and n.strip():
            self.names[i] = n.strip()[:12]
            self.draw_track()

    def minus(self, i):
        if self.winner is not None or self.score[i] <= 0:
            return
        if messagebox.askyesno("Koreksi Skor",
                               f"Kurangi skor {self.names[i]} sebanyak 1?",
                               parent=self.root):
            self.score[i] -= 1
            self.start_animation()

    def _reset_state(self):
        self._stop_winner()
        self.score = [0] * N
        self.cur = [0.0] * N
        self.glow = [0] * N
        self.done.clear()
        self.winner = None
        self.refresh_cards()
        self.draw_track()

    def reset(self):
        if messagebox.askyesno("Ulangi Lomba", "Reset semua skor dan soal?",
                               parent=self.root):
            self._reset_state()

    # --------------------------------------------------------- PEMENANG
    def check_winner(self):
        if self.winner is not None:
            return
        for i in range(N):
            if self.score[i] >= MAX_SKOR:
                self.winner = i
                self.show_winner(i)
                return

    def show_winner(self, i):
        self.overlay = tk.Canvas(self.root, bg="#FFF1B8", highlightthickness=0)
        self.overlay.place(x=0, y=0, relwidth=1, relheight=1)
        self.win_t = 0
        W = max(self.root.winfo_width(), 800)
        H = max(self.root.winfo_height(), 600)
        cols = RAINBOW + [YELLOW, WHITE]
        self.confetti = [[random.uniform(0, W), random.uniform(-H, 0),
                          random.uniform(1.5, 4.5), random.uniform(7, 14),
                          random.choice(cols), random.uniform(0, 6.28)]
                         for _ in range(150)]
        self.balloons = [[random.uniform(0.04, 0.96) * W, H + random.uniform(0, H),
                          random.uniform(1.2, 2.6), random.choice(RAINBOW),
                          random.uniform(0, 6.28), random.uniform(20, 32)]
                         for _ in range(16)]
        self.btn_again = hover_button(self.overlay, "↻  MAIN LAGI", GREEN, WHITE,
                                      "#23975A", self._reset_state, F(14), 28, 12)
        self.btn_close = hover_button(self.overlay, "LIHAT PAPAN", "#4D96FF", WHITE,
                                      "#3A7EE0", self._stop_winner, F(14), 28, 12)
        self.btn_again.place(relx=0.40, rely=0.93, anchor="center")
        self.btn_close.place(relx=0.60, rely=0.93, anchor="center")
        self._win_loop()

    def _win_loop(self):
        c = self.overlay
        if c is None or not c.winfo_exists():
            return
        t = self.win_t
        self.win_t += 1
        W, H = c.winfo_width(), c.winfo_height()
        u = H / 780.0
        c.delete("all")
        i = self.winner
        color, tint = TEAMS[i]
        cx, cy = W / 2, H * 0.36

        # sinar matahari berputar
        R = math.hypot(W, H)
        n_ray = 20
        base = t * 0.012
        for k in range(0, n_ray, 2):
            a1 = base + k * 2 * math.pi / n_ray
            a2 = a1 + math.pi / n_ray
            c.create_polygon(cx, cy, cx + R * math.cos(a1), cy + R * math.sin(a1),
                             cx + R * math.cos(a2), cy + R * math.sin(a2),
                             fill="#FFE680", outline="")

        # balon naik
        for b in self.balloons:
            b[1] -= b[2]
            if b[1] < -80:
                b[1] = H + 60
            bx = b[0] + math.sin(b[4] + t * 0.04) * 14
            by, rr = b[1], b[5]
            c.create_line(bx, by + rr * 1.3, bx + math.sin(t * 0.08 + b[4]) * 8,
                          by + rr * 3.2, fill="#8D99AE", width=2)
            c.create_oval(bx - rr, by - rr * 1.25, bx + rr, by + rr * 1.3,
                          fill=b[3], outline="")
            c.create_oval(bx - rr * 0.5, by - rr * 0.9, bx - rr * 0.15, by - rr * 0.45,
                          fill=WHITE, outline="", stipple="gray50")
            c.create_polygon(bx, by + rr * 1.3, bx - 5, by + rr * 1.55,
                             bx + 5, by + rr * 1.55, fill=darker(b[3]), outline="")

        # maskot juara melompat
        bounce = abs(math.sin(t * 0.13)) * 26 * u
        mr = 105 * u
        draw_mascot(c, MASCOTS[i], cx, cy - bounce, mr, "m", happy=True)
        # bintang berputar di sekeliling
        for k in range(6):
            a = t * 0.04 + k * math.pi / 3
            sx = cx + math.cos(a) * mr * 1.9
            sy = cy - bounce * 0.5 + math.sin(a) * mr * 1.0
            c.create_polygon(star_pts(sx, sy, 16 * u + 4, 7 * u + 2, a),
                             fill=RAINBOW[k], outline="")

        # piala
        draw_trophy(c, cx, H * 0.62, 62 * u * (1 + 0.04 * math.sin(t * 0.15)), "t")

        # confetti
        for p in self.confetti:
            p[1] += p[2]
            p[0] += math.sin(p[5] + t * 0.07) * 1.6
            if p[1] > H + 20:
                p[1] = -20
                p[0] = random.uniform(0, W)
            w = p[3] * (0.4 + abs(math.sin(p[5] + t * 0.15)))
            c.create_rectangle(p[0], p[1], p[0] + w, p[1] + p[3] * 0.6,
                               fill=p[4], outline="")

        # teks
        size = int(44 + 5 * math.sin(t * 0.15))
        c.create_text(cx + 3, H * 0.075 + 3, text="HOREEE! SELAMAT!", fill="#E0A800",
                      font=F(size))
        c.create_text(cx, H * 0.075, text="HOREEE! SELAMAT!", fill=color,
                      font=F(size))
        nm = self.names[i].upper()
        c.create_text(cx + 3, H * 0.76 + 3, text=nm, fill=WHITE, font=F(52))
        c.create_text(cx, H * 0.76, text=nm, fill=INK, font=F(52))
        c.create_text(cx, H * 0.84, text="JUARA CERDAS CERMAT MATEMATIKA",
                      fill="#E0457B", font=F(20))
        skor = "  |  ".join(f"{self.names[k]}: {self.score[k]}" for k in range(N))
        c.create_text(cx, H * 0.885, text="Skor akhir  -  " + skor, fill=SOFT,
                      font=F(12, "normal"))

        self.win_job = c.after(33, self._win_loop)

    def _stop_winner(self):
        if self.overlay is not None:
            try:
                if self.win_job:
                    self.overlay.after_cancel(self.win_job)
                self.overlay.destroy()
            except tk.TclError:
                pass
        self.overlay = None
        self.win_job = None


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
