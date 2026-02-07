import random
import os
import sys
import time

# ==========================================
# BAGIAN 1: FUNGSI BANTUAN (UTILITIES)
# ==========================================

def bersihkan_layar():
    """Membersihkan layar terminal agar tampilan rapi."""
    # Jika Windows pakai 'cls', jika Linux/Mac pakai 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def loading(durasi=1):
    """Efek loading sederhana."""
    print("\nMemproses...", end="", flush=True)
    time.sleep(durasi)
    print(" Selesai!\n")
    time.sleep(0.5)

# ==========================================
# BAGIAN 2: LOGIKA GAME (MODUL)
# ==========================================

def game_batu_gunting_kertas():
    bersihkan_layar()
    print("="*40)
    print("   GAME 1: BATU GUNTING KERTAS")
    print("="*40)
    print("Lawan komputer! Ketik 'x' untuk kembali.")
    
    pilihan = ["batu", "gunting", "kertas"]
    
    while True:
        komputer = random.choice(pilihan)
        user = input("\nPilih (batu/gunting/kertas): ").lower()
        
        if user == 'x':
            break
            
        if user not in pilihan:
            print(">> Typo? Masukkan: batu, gunting, atau kertas.")
            continue
            
        loading(0.5)
        print(f"Kamu: {user.upper()}  VS  Komputer: {komputer.upper()}")
        
        # Logika Menang/Kalah
        if user == komputer:
            print(">> HASIL: SERI!")
        elif (user == "batu" and komputer == "gunting") or \
             (user == "gunting" and komputer == "kertas") or \
             (user == "kertas" and komputer == "batu"):
            print(">> HASIL: MENANG! Hebat!")
        else:
            print(">> HASIL: KALAH... Coba lagi!")

def game_tebak_angka():
    bersihkan_layar()
    print("="*40)
    print("   GAME 2: TEBAK ANGKA MISTERIUS")
    print("="*40)
    print("Saya simpan angka 1 s.d 20. Kamu punya 5 nyawa.")
    
    angka_rahasia = random.randint(1, 20)
    nyawa = 5
    
    while nyawa > 0:
        print(f"\nSisa Nyawa: {nyawa}")
        try:
            tebakan = int(input("Tebakanmu (1-20): "))
            
            if tebakan == angka_rahasia:
                loading(0.5)
                print(f"\n>>> JACKPOT! Benar sekali angka {angka_rahasia}!")
                break
            elif tebakan < angka_rahasia:
                print(">> Terlalu KECIL.")
            else:
                print(">> Terlalu BESAR.")
            
            nyawa -= 1
            
        except ValueError:
            print(">> Masukkan ANGKA ya, bukan huruf!")
    
    if nyawa == 0:
        print(f"\nGAME OVER! Angka yang benar adalah: {angka_rahasia}")
    
    input("\nTekan Enter untuk kembali...")

def game_tictactoe():
    bersihkan_layar()
    print("="*40)
    print("   GAME 3: TIC TAC TOE (X vs O)")
    print("="*40)
    print("Mode: 2 Pemain (Bergantian)")
    print("Cara main: Pilih angka 1-9 untuk isi kotak.")

    # Membuat papan kosong (List berisi 9 spasi)
    board = [" " for _ in range(9)]

    # Fungsi lokal untuk menampilkan papan
    def print_board():
        print(f"\n {board[0]} | {board[1]} | {board[2]} ")
        print("---|---|---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---|---|---")
        print(f" {board[6]} | {board[7]} | {board[8]} \n")

    # Pola kemenangan (Baris, Kolom, Diagonal)
    winning_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Baris
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Kolom
        (0, 4, 8), (2, 4, 6)             # Diagonal
    ]

    giliran = "X"
    langkah = 0
    game_over = False

    print_board()

    while not game_over:
        try:
            # Input user dikurangi 1 karena index list mulai dari 0
            pilihan = int(input(f"Giliran {giliran} (pilih 1-9): ")) - 1
            
            # Validasi Input
            if pilihan < 0 or pilihan > 8:
                print(">> Angka harus 1 sampai 9!")
                continue
            if board[pilihan] != " ":
                print(">> Kotak sudah isi! Pilih lain.")
                continue

            # Isi papan
            board[pilihan] = giliran
            langkah += 1
            print_board()

            # Cek Kemenangan
            menang = False
            for a, b, c in winning_combos:
                if board[a] == board[b] == board[c] and board[a] != " ":
                    print(f"\n>>> SELAMAT! PEMAIN '{giliran}' MENANG! <<<")
                    menang = True
                    game_over = True
                    break
            
            # Cek Seri
            if not menang and langkah == 9:
                print("\n>>> PERMAINAN SERI (DRAW)! <<<")
                game_over = True

            # Ganti Giliran
            giliran = "O" if giliran == "X" else "X"

        except ValueError:
            print(">> Masukkan angka 1-9!")

    input("Tekan Enter untuk kembali...")

# ==========================================
# BAGIAN 3: SISTEM UTAMA
# ==========================================

def login_system():
    """Halaman Login Sederhana."""
    bersihkan_layar()
    print("########################################")
    print("#      SISTEM KEAMANAN GAME CENTER     #")
    print("########################################")
    
    limit = 3
    while limit > 0:
        user = input("Username : ") # Masukkan: admin
        pw   = input("Password : ") # Masukkan: 123
        
        if user == "admin" and pw == "123":
            print("\nLogin Berhasil! Akses diberikan.")
            loading(1)
            return True
        else:
            limit -= 1
            print(f">> Gagal! Sisa percobaan: {limit}\n")
    
    print("Sistem Terkunci. Jalankan ulang program.")
    return False

def menu_utama():
    """Menu Navigasi Utama."""
    while True:
        bersihkan_layar()
        print("="*40)
        print("    APLIKASI MINI GAME - KELOMPOK 8") 
        print("="*40)
        print("[1] Batu Gunting Kertas")
        print("[2] Tebak Angka Misterius")
        print("[3] Tic Tac Toe (X vs O)")
        print("[4] Keluar")
        print("="*40)
        
        pilihan = input("Pilih Menu (1-4): ")
        
        if pilihan == '1':
            game_batu_gunting_kertas()
        elif pilihan == '2':
            game_tebak_angka()
        elif pilihan == '3':
            game_tictactoe()
        elif pilihan == '4':
            print("\nTerima kasih. Sampai jumpa!")
            sys.exit()
        else:
            print("Pilihan tidak ada!")
            time.sleep(1)

# ==========================================
# BAGIAN 4: EKSEKUSI PROGRAM
# ==========================================

if __name__ == "__main__":
    if login_system():
        menu_utama()
