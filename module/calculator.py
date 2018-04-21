def kalkulator () :
    print("__"*10)
    a = input ("masukan nilai a :")
    b = input ("masukan nilai b :")
    print ("Program Kalkulator Sederhana")
    print ("################")
    print ("1. Penjumlahan")
    print ("2. Pengurangan")
    print ("3. Perkalian")
    print ("4. Pembagian")
    print ("################")
    print ("silahkan pilih 1-4")
    pil = raw_input ("Masukkan pilihan : ")
    if pil == '1':
        a=a+b
        print(a)
    elif pil == '2':
        a=a-b
        print(a)
    elif pil == '3':
        a=a*b
        print(a)
    elif pil == '4':
        a=a/b
        print(a)
    else:
        print("salah")
    

