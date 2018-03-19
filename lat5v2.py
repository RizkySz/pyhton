i=0
nama = []
nim = []
tugas = []
uts = []
uas = []
akhir= []
while True  :
    na = raw_input("Nama\t\t: ")
    nama.append(na)
    ni = raw_input ("NIM\t\t: ")
    nim.append(ni)
    tu = input("Nilai Tugas\t: ")
    tugas.append(tu)
    us = input("Nilai UTS\t: ")
    uts.append(us)
    ua = input("Nilai UAS\t: ")
    uas.append(ua)
    akhiri = (tu+us+ua)/3
    akhir.append (akhiri)

    tambah = ''
    while tambah!='y' and tambah!='t':
        tambah = raw_input("Tambah Data (y/t)? ")
    i+=1
    if(tambah == "t"):
        break
      

print "******************************************************************"
print " No |    Nama    |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir  |"
print "******************************************************************"
for u in range(i):
    #print " ",u+1, "| ", nama[u], " | ", nim[u], " | ", tugas[u], " | ", uts[u], " | ", uas[u], " | ", akhir[u], " "
    print " {u:2d} | {nama:10s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:7.2f} |".format(nama=nama[u], nim=nim[u], tugas=uts[u], uts=uts[u], uas=uas[u], akhir=akhir[u], u=u+1) 
