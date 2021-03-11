while True :
        Kalori      = float(input('Entrikan jumlah Kebutuhan Gizi Harian Anda : '))
        karbohidrat = Kalori*(60/100)
        protein     = Kalori*(20/100)
        lemak       = Kalori*(20/100)
        print ('Kebutuhan Gizi Harian Anda Sebesar ', Kalori,'kkal')
        print ('Pembagian kalori terdiri atas, ')
        print ('Karbohidrat sebanyak :', karbohidrat)
        print ('Protein sebanyak     :', protein)
        print ('Lemak sebanyak       :', lemak)
        print ('\n')
        print ('Jangan Lupa Untuk Selalu Menjaga Kesehatan :)')
        command      = str(input("Apakah anda ingin menginputkan data lagi?  [Y]/[T] :"))
        if   command == "Y" :       
            continue           
        elif command == "T" :       
            break