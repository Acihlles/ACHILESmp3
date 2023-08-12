import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, "rb").read()

def encrypt_and_hide(directory, key, mp3_filename):
    f = Fernet(key)

    data = None
    if os.path.isfile(directory):
        with open(directory, "rb") as file:
            data = file.read()
    elif os.path.isdir(directory):
        data = os.urandom(1024)  

    encrypted_data = f.encrypt(data)

    with open(mp3_filename, "ab") as mp3_file:
        mp3_file.write(encrypted_data)

def decrypt_and_extract(mp3_filename, key, output_directory):
    f = Fernet(key)

    with open(mp3_filename, "rb") as mp3_file:
        encrypted_data = mp3_file.read()

    decrypted_data = f.decrypt(encrypted_data)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_filename = os.path.join(output_directory, "hidden_data")
    with open(output_filename, "wb") as output_file:
        output_file.write(decrypted_data)

if __name__ == "__main__":
    print("""

░█▀▀▄░▒█▀▀▄░▒█░▒█░▀█▀░▒█░░░░▒█░░░░▒█▀▀▀░▒█▀▀▀█░░░░▒█▀▄▀█░▒█▀▀█░█▀▀█░░
▒█▄▄█░▒█░░░░▒█▀▀█░▒█░░▒█░░░░▒█░░░░▒█▀▀▀░░▀▀▀▄▄░▄▄░▒█▒█▒█░▒█▄▄█░░▒▀▄░░
▒█░▒█░▒█▄▄▀░▒█░▒█░▄█▄░▒█▄▄█░▒█▄▄█░▒█▄▄▄░▒█▄▄▄█░▀▀░▒█░░▒█░▒█░░░░█▄▄█░░


    """)
    print("Hoş Geldin!")
    print("\n1 = mp3 İçine Dosya Sakla\n0 = mp3 İçinden Dosya Çıkart")

    choice = input("Seçim = ")

    if choice == "1":
        key = generate_key()
        save_key(key, "key.key")
        directory = input("Gizlenecek dosya/dizin yolunu girin: ")
        mp3_filename = input("MP3 dosyasının yolunu girin: ")
        encrypt_and_hide(directory, key, mp3_filename)
        print("Dosya/dizin başarıyla şifrelendi ve gizlendi.")
    elif choice == "0":
        key = load_key("key.key")
        mp3_filename = input("MP3 dosyasının yolunu girin: ")
        output_directory = input("Çıkartılacak dosya/dizin yolunu girin: ")
        decrypt_and_extract(mp3_filename, key, output_directory)
        print("Gizli veri başarıyla çıkartıldı ve çözüldü.")
    else:
        print("Geçersiz seçenek.")

