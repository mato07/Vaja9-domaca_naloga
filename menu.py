# -*- coding: utf-8 -*-

predjedi = []
glavne_jedi = []
sladice = []

while True:
    predjed = raw_input("Vpiši ime predjedi: ")
    c_predjed = raw_input("Vpiši ceno predjedi -%s- s številko v €: " % predjed)
    glavna_jed = raw_input("Vpiši ime glavne jedi: ")
    c_glavna_jed = raw_input("Vpiši ceno glavne jedi -%s- s številko v €: " % glavna_jed)
    sladica = raw_input("Vpiši ime sladice: ")
    c_sladica = raw_input("Vpiši ceno sladice -%s- s številko v €: " % sladica)

    predjedi.append([predjed,c_predjed])
    glavne_jedi.append([glavna_jed, c_glavna_jed])
    sladice.append([sladica, c_sladica])

    pogoj = raw_input("Želiš vnesti še kakšen meni (da/ne): ")

    if pogoj.lower() == "ne":
        break

jedi=[predjedi,glavne_jedi,sladice]
print jedi

menu_file = open("Menu.txt", "w+")

menu_file.write("Danes nudimo naslednje dnevne menije:\n")
menu_file.write("\n")

for i in range(len(predjedi)):
    cena = int(jedi[0][i][1]) + int(jedi[1][i][1]) + int(jedi[2][i][1])
    print "Meni " + str(i+1) + ":\n"
    menu_file.write("Meni " + str(i+1) + ":\n")
    print "Predjed: %s ..... %s€" % (jedi[0][i][0], jedi[0][i][1])
    menu_file.write("Predjed: %s ..... %s€" % (jedi[0][i][0], jedi[0][i][1]) + "\n")
    print "Glavna jed: %s ..... %s€" % (jedi[1][i][0], jedi[1][i][1])
    menu_file.write("Glavna jed: %s ..... %s€" % (jedi[1][i][0], jedi[1][i][1]) + "\n")
    print "Sladica: %s ..... %s€" % (jedi[2][i][0], jedi[2][i][1])
    menu_file.write("Sladica: %s ..... %s€" % (jedi[2][i][0], jedi[2][i][1]) + "\n")
    print "Cena menija %s ..... %s€\n" % (str(i+1), cena)
    menu_file.write("Cena menija %s ..... %s€" % (str(i+1), cena) + "\n")
    menu_file.write("\n")




