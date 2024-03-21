x = int(input("Masukkan angka: "))

###DESIMAL###
print("Angka dalam bentuk desimal:", x)

###BINER###
convert = bin(x)[2:]
explot = convert.zfill(8)
print("Angka dalam bentuk biner:", explot)

###OKTAL###
convert = oct(x)[2:].zfill(3)
print("Angka dalam bentuk oktal:", convert)

###HEKSADESIMAL####
convert = hex(x)[2:].zfill(2).upper()
print("Angka dalam bentuk heksadesimal:", convert)

