import os;


def Header():
    print("==============================")
    print("===== APLIKASI KUIS ESAY =====")
    print("========== By Noname ==========")
    print("==============================")
    print("")
    print("Menu :")
    print("[1] Mulai Kuis Esay")
    print("[2] Tentang Program")
    print("[3] Keluar Program")


def Kuis():
    score = 0
    score = int(score)
    benar = 0
    benar = int(benar)
    salah = 0
    salah = int(salah)

    print("==============================")
    print("========= Kuis Esay ==========")
    print("==============================")
    name = input("Masukkan nama kamu :")
    name = name.title()
    os.system("cls")

    print("==============================")
    print("========= Kuis Esay ==========")
    print("==============================")
    #Pertanyaan1
    print("1. Indonesiaku ?")

    jawaban1 = "indonesiaku"
    Inputjawaban1 = input("Jawab :")


    if (Inputjawaban1 != jawaban1):
        print("Maaf Jawaban Kamu Salah. Jawaban yang benar adalah " + jawaban1)
        salah = salah + 1
    else:
        print("Selamat Jawaban Kamu Benar")
        score = score + 20
        benar = benar + 1
    

    #Pertanyaan2
    print("2. Indonesiaku ?")

    jawaban2 = "indonesiaku"
    Inputjawaban2 = input("Jawab :")

    if (Inputjawaban2 != jawaban2):
        print("Maaf Jawaban Kamu Salah. Jawaban yang benar adalah " + jawaban2)
        salah = salah + 1
    else:
        print("Selamat Jawaban Kamu Benar")
        score = score + 20
        benar = benar + 1


     #Pertanyaan3
    print("3. Indonesiaku ?")

    jawaban3 = "indonesiaku"
    Inputjawaban3 = input("Jawab :")

    if (Inputjawaban3 != jawaban3):
        print("Maaf Jawaban Kamu Salah. Jawaban yang benar adalah " + jawaban3)
        salah = salah + 1
    else:
        print("Selamat Jawaban Kamu Benar")
        score = score + 20
        benar = benar + 1

    
     #Pertanyaan4
    print("4. Indonesiaku ?")

    jawaban4 = "indonesiaku"
    Inputjawaban4 = input("Jawab :")

    if (Inputjawaban4 != jawaban4):
        print("Maaf Jawaban Kamu Salah. Jawaban yang benar adalah " + jawaban4)
        salah = salah + 1
    else:
        print("Selamat Jawaban Kamu Benar")
        score = score + 20
        benar = benar + 1

    
     #Pertanyaan2
    print("5. Indonesiaku ?")

    jawaban5 = "indonesiaku"
    Inputjawaban5 = input("Jawab :")

    if (Inputjawaban5 != jawaban5):
        print("Maaf Jawaban Kamu Salah. Jawaban yang benar adalah " + jawaban5)
        salah = salah + 1
    else:
        print("Selamat Jawaban Kamu Benar")
        score = score + 20
        benar = benar + 1

    print("====================")
    os.system("cls")

    print("==============================")
    print("========== Selesai ===========")
    print("==============================")
    print("Player : "+name)
    print("Benar : "+str(benar))
    print("Salah : "+str(salah))
    print("Skor : "+str(score))
    print("Keterangan :")
    while score >= 70 :
        print("Selamat nilai kamu telah memenuhi KKM")
        break
    while score <=70 :
        print("Tingkatkan lagi belajarmu yaaa")
        break
    print("==============================")

def Tentangprogram():
    print("==============================")
    print("======= Tentang Program ======")
    print("==============================")
    print("")
    ClickKembali = input("Kembali ke menu utama? (Y/T) : ") 
    os.system("cls")
    if (ClickKembali == "Y"):
        Header()
    elif (ClickKembali == "T"):
        print("Keluar")

Header()

InputMenu = int(input("Masukkan pilihan 1/2/3 :"))
os.system("cls")

if (InputMenu == 1):
    Kuis()
elif (InputMenu == 2):
    Tentangprogram()
elif (InputMenu ==3):
    print("Menu3")

