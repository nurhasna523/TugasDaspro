dataSiswa = {
    'nabila': '123',
    'serly': '124',
    'hasna': '235',
    'safril': '224',
    'naiyla': '456',
    'laila': '1212',
    'manda': '116',
    'fika': '2023',
    'rizal': '2021',
    'titin': '2024'
}

def login_system():
    
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

   
    if username in dataSiswa:
       
        if dataSiswa[username] == password:
            print(f"Selamat Datang, {username}!")
        else:
            print("Data yang dimasukkan salah. Silahkan coba kembali.")
    else:
        print("Data yang dimasukkan salah. Silahkan coba kombali.")

login_system()
