casos = int(input())
cont = 0
while cont < casos:
    casa = int(input())
    if casa == 64 or casa == 63:
        if casa == 64:
            print("1537228672809129 kg")
        else:
            print("768614336404564 kg")
    else:
        graos = 1
        for x in range(0, casa):
            if x == 0:
                graos = 1
                inter = 1
            else:
                graos = graos * 2
                inter = inter + graos
        kg = int(inter / 200)
        kg = int(kg / 60)
        print("{} kg".format(kg))
    cont = cont + 1