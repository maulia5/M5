
class Music:
    def _init_(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def display(self):
        print(f"Judul: {self.judul}, Penyanyi: {self.penyanyi}, Genre: {self.genre}")


lagu_Indonesia = [
    Music("Melawan restu", "Mahalini", "P-Song"),
    Music("Orang yang sama", "Virgoun", "P-Song"),
    Music("Komang", "Raim Laodo", "P-Song"),
    Music("Tak Segampang itu", "Anggi Marito", "P-Song"),
    Music("Pesan Terakhir", "Lyodra", "P-Song")
]

lagu_English = [
    Music("Shape Of You", "Ed Sheeran", "P-Song"),
    Music("Love", "Taylor Swift", "P-Song"),
    Music("Fix You", "Coldplay", "P-Song"),
    Music("As It Was", "Harry Styles", "P-Song"),
    Music("Glimpse Of Us", "Joji", "P-Song")
]

lagu_Arab = [
    Music("Albi Ya Albi", "Nancy Ajram", "P-Song"),
    Music("Nasini El Donya", "Ragheb Alama", "P-Song"),
    Music("Shabary Alil", "Sherine", "P-Song"),
    Music("Yali Yalili", "Sherine", "P-Song"),
    Music("Eh eh", "Sherine", "P-Song")
]

class MusicManager:
    def _init_(self, lagu_list):
        self.lagu_list = lagu_list

    def list_song(self):
        print("\n>>> Daftar Lagu:")
        for music in self.lagu_list:
            music.display()

    def add_song(self):
        judul = input("Masukkan judul lagu: ")
        penyanyi = input("Masukkan nama penyanyi: ")
        genre = input("Masukkan genre: ")
        music = Music(judul, penyanyi, genre)
        self.lagu_list.append(music)
        print(f"Lagu '{judul}' berhasil ditambahkan!")

    def delete_song(self):
        judul = input("Masukkan judul lagu yang ingin dihapus: ")
        for music in self.lagu_list:
            if music.judul == judul:
                self.lagu_list.remove(music)
                print(f"Lagu '{judul}' berhasil dihapus!")
                return
        print(f"Lagu dengan judul '{judul}' tidak ditemukan.")


class Cari:
    def search_penyanyi(lagu_list):
        penyanyi = input("Masukkan nama penyanyi: ")
        found = False
        for music in lagu_list:
            if music.penyanyi == penyanyi:
                music.display()
                found = True
        if not found:
            print(f"Tidak ada lagu dari penyanyi '{penyanyi}'.")


def tampilanmenu():
    indo_manager = MusicManager(lagu_Indonesia)
    english_manager = MusicManager(lagu_English)
    arab_manager = MusicManager(lagu_Arab)

    while True:
        print("\n" + "="*10 + " Playlist Music " + "="*10)
        print("1. Indonesia Song")
        print("2. English Song")
        print("3. Arab Song")
        print("4. Search Music by Singer")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan 0/1/2/3/4: ")

        if pilihan == '1':
            while True:
                print("\n" + "="*10 + " Indonesia Song " + "="*10)
                print("1. Display Song")
                print("2. Add Song")
                print("3. Delete Song")
                print("0. Kembali")
                pilih = input("Masukkan pilihan 0/1/2/3: ")

                if pilih == '1':
                    indo_manager.list_song()
                elif pilih == '2':
                    indo_manager.add_song()
                elif pilih == '3':
                    indo_manager.delete_song()
                elif pilih == '0':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '2':
            while True:
                print("\n" + "="*10 + " English Song " + "="*10)
                print("1. Display Song")
                print("2. Add Song")
                print("3. Delete Song")
                print("0. Kembali")
                pilih = input("Masukkan pilihan 0/1/2/3: ")

                if pilih == '1':
                    english_manager.list_song()
                elif pilih == '2':
                    english_manager.add_song()
                elif pilih == '3':
                    english_manager.delete_song()
                elif pilih == '0':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '3':
            while True:
                print("\n" + "="*10 + " Arab Song " + "="*10)
                print("1. Display Song")
                print("2. Add Song")
                print("3. Delete Song")
                print("0. Kembali")
                pilih = input("Masukkan pilihan 0/1/2/3: ")

                if pilih == '1':
                    arab_manager.list_song()
                elif pilih == '2':
                    arab_manager.add_song()
                elif pilih == '3':
                    arab_manager.delete_song()
                elif pilih == '0':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '4':
            print("\n=== Cari Musik ===")
            genre_choice = input("Cari di playlist mana? (1: Indonesia, 2: English, 3: Arab): ")
            if genre_choice == '1':
                Cari.search_penyanyi(lagu_Indonesia)
            elif genre_choice == '2':
                Cari.search_penyanyi(lagu_English)
            elif genre_choice == '3':
                Cari.search_penyanyi(lagu_Arab)
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '0':
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

tampilanmenu()
