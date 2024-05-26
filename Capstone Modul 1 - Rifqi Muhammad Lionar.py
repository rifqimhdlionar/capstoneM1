# Data Siswa Agak Laen
students = [
    {"Student ID": "2405001", "Name": "Bene Dion", "Gender": "pria", "Math": 98, "Bahasa Indonesia": 90, "English": 85, "Science": 85},
    {"Student ID": "2405002", "Name": "Boris Bokir", "Gender": "pria", "Math": 85, "Bahasa Indonesia": 88, "English": 90, "Science": 80},
    {"Student ID": "2405003", "Name": "Indra Jegel", "Gender": "pria", "Math": 80, "Bahasa Indonesia": 95, "English": 85, "Science": 85},
    {"Student ID": "2405004", "Name": "Oki Rengga", "Gender": "pria", "Math": 80, "Bahasa Indonesia": 90, "English": 85, "Science": 85},
    {"Student ID": "2405005", "Name": "Naomi", "Gender": "wanita", "Math": 95, "Bahasa Indonesia": 90, "English": 90, "Science": 90}
]

# Menghitung rata-rata nilai masing-masing siswa
def calculate_average(student):  
    subjects = ["Math", "Bahasa Indonesia", "English", "Science"]
    total = sum(student[subject] for subject in subjects)
    return total / len(subjects)

# Menghitung rata-rata nilai siswa dan nilai rata-rata di ranking
def update_rank(students):
    for student in students: 
        student["Average"] = calculate_average(student)
    students.sort(key=lambda x: x["Average"], reverse=True)
    for i, student in enumerate(students, 1):
        student["Rank"] = i

# 1) Menu Create - Membuat data siswa baru
def create_student():
    while True:
        option = input("\nMembuat Data Siswa Baru \n(1) Masukan Data Siswa Baru \n(2) Kembali ke Menu Utama \n\nSilakan Pilih Menu yang diinginkan (1-2): ")
        if option == "2":
            break
        elif option == "1":
            new_student = {}
            while True:
                student_id = input("Masukan Nomor Induk Siswa (7 digit): ")
                if student_id.isdigit() and len(student_id) == 7:
                    new_student["Student ID"] = student_id
                    break
                else:
                    print("Nomor Induk Siswa harus berupa angka 7 digit.")
            
            new_student["Name"] = input("Masukan Nama Siswa: ")

            while True:
                gender = input("Masukan Jenis Kelamin Siswa (pria/wanita): ").lower()
                if gender in ["pria", "wanita"]:
                    new_student["Gender"] = gender
                    break
                else:
                    print("Jenis kelamin harus pria atau wanita.")

            for subject in ["Math", "Bahasa Indonesia", "English", "Science"]:
                while True:
                    try:
                        score = int(input(f"Masukan Nilai {subject} Siswa (1-100): "))
                        if 1 <= score <= 100:
                            new_student[subject] = score
                            break
                        else:
                            print(f"Nilai {subject} harus antara 1 dan 100.")
                    except ValueError:
                        print(f"Nilai {subject} harus berupa angka.")

            print("Berikut Data Siswa baru:")
            for key, value in new_student.items():
                print(f"{key}: {value}")

            confirm = input("Apakah Anda yakin data siswa tersebut sudah benar? (y/n): ")
            if confirm.lower() == 'y':
                students.append(new_student)
                update_rank(students)
                print("Data siswa tersebut sudah ditambahkan.")

            add_more = input("\nApakah Anda ingin menambahkan data siswa lagi? (y/n): ")
            if add_more.lower() != 'y':
                break
        else:
            print("Pilihan tidak valid, silakan pilih 1 atau 2.")
            create_student()

# 2) Menu Read - sub menu option Menampilkan daftar nilai siswa, Menampilkan Daftar seorang siswa, rata-rata nilai siswa, dan ranking siswa
def read_students():
    option = input("\nMenampilkan Daftar Nilai Siswa \n\n(1) Menampilkan Daftar Nilai Seluruh Siswa Agak Laen \n(2) Menampilkan Daftar Nilai Seorang Siswa \n(3) Menampilkan Rangking Siswa Agak Laen \n(4) Kembali ke Menu Utama \n\nSilakan pilih menu yang diinginkan (1-4) :")
    if option == "1":
        print("\nDaftar Siswa Agak Laen:")
        for student in students:
            print(student)

    elif option == "2":
        student_id = input("\nMasukkan Nomor Induk Siswa: ")
        for student in students:
            if student ["Student ID"] == student_id :
                print(student)
                return
        print(f"Siswa dengan Nomor Induk {student_id} tidak ditemukan.")

    elif option == "3":
        print("\nBerikut Ranking Siswa Agak Laen")
        for student in students:
            print(f"Student ID: {student['Student ID']}, Name: {student['Name']}, Average: {student['Average']}, Rank: {student['Rank']}")

    elif option == "4":
        main()
    else :
        print("Pilihan yang diinput salah, silahkan pilih kembali!")
        read_students()

# 3) Menu Update - Melakukan perbaharuan nilai siswa berdasarkan student_id
def update_student():
    print("\nMengubah Data Nilai Siswa")
    student_id = input("\nMasukan Nomor Induk Siswa yang ingin diperbaharui: ")
    student = next((s for s in students if s["Student ID"] == student_id), None)
    if student:
        while True:
            option = input("Pilih opsi pembaruan nilai:\n   (1) Ubah salah satu nilai mata pelajaran siswa\n   (2) Ubah semua nilai mata pelajaran siswa\n\nSilakan pilih menu yang diinginkan (1-2) : ")
            if option == "1":
                key = input("Pilih mata pelajaran yang akan diubah (Math, Bahasa Indonesia, English, Science): ")
                if key in ["Math", "Bahasa Indonesia", "English", "Science"]:
                    new_value = input(f"Input nilai baru untuk {key} (1-100): ")
                    try:
                        new_value_int = int(new_value)
                        if 1 <= new_value_int <= 100:
                            student[key] = new_value_int
                            print(f"Nilai {key} telah diperbaharui.")
                        else:
                            print(f"Nilai untuk {key} harus antara 1 dan 100. Nilai tidak diubah.")
                    except ValueError:
                        print(f"Nilai untuk {key} harus berupa angka. Nilai tidak diubah.")
                else:
                    print("Mata pelajaran tidak valid.")
                break
            elif option == "2":
                for key in ["Math", "Bahasa Indonesia", "English", "Science"]:
                    new_value = input(f"Input nilai baru untuk {key} (kosongkan jika tidak ada nilai yang diubah): ")
                    if new_value:
                        try:
                            new_value_int = int(new_value)
                            if 1 <= new_value_int <= 100:
                                student[key] = new_value_int
                            else:
                                print(f"Nilai untuk {key} harus antara 1 dan 100. Nilai tidak diubah.")
                        except ValueError:
                            print(f"Nilai untuk {key} harus berupa angka. Nilai tidak diubah.")
                print(f"Semua nilai siswa {student_id} telah diperbaharui.")
                break
            else:
                print("Pilihan yang diinput salah, silahkan pilih kembali!.")
    else:
        print("Siswa dengan Nomor Induk tersebut tidak ditemukan.")
        update_student()


# 4) Menu Delete - Melakukan penghapusan data satu siswa berdasarkan student_id dan hapus semua data siswa
def delete_student():
    print("\nMenghapus Daftar Data Siswa")
    option = input("\n   (1) Menghapus Data Seorang Siswa\n   (2) Menghapus Data Semua Siswa\n   (3) Kembali ke Menu Utama\n\nSilakan pilih menu yang diinginkan (1-2) :")
    if option == '1':
        student_id = input("Masukan Nomor Induk Siswa yang akan dihapus: ")
        global students
        students = [s for s in students if s["Student ID"] != student_id]
        update_rank(students)
        print("Data Siswa tersebut telah dihapus")
    elif option == '2':
        students.clear()
        print("Semua Data Siswa telah dihapus.")
    elif option == '3' :
        main()
    else:
        print("Pilihan salah, Silahkan input kembali!")

# Menu Aplikasi
def main():
    while True:
        print("\nSelamat Datang di Daftar Nilai Siswa Agak Laen \n\nMain Menu: ")
        print("1. Membuat Data Siswa")
        print("2. Menampilkan Daftar Nilai Siswa")
        print("3. Mengubah Data Nilai Siswa")
        print("4. Menghapus Daftar Data Siswa")
        print("5. Keluar dari Aplikasi Daftar Data Siswa")
        
        choice = input("\nSilakan pilih menu yang diinginkan (1-5): ")
        if choice == '1':
            create_student()
        elif choice == '2':
            read_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Keluar dari Aplikasi Daftar Data Siswa.")
            break
        else:
            print("Pilihan Menu Salah, Silahkan pilih kembali!")

if __name__ == "__main__":
    update_rank(students)
    main()