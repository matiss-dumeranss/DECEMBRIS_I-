#a=int(input("Ievadi pulksteņa laiku Veselos skaitļos..."))

#if a>6 and a<12:
 #   print("Labrīt!")
#elif a>12 and a<18:
 #   print("Labdien!")
#elif a>18 and a<24:
#    print("Labvakar!")

a=str(input("Norādi dienas laiku (ja pulkstens ir no 6 līdz 12 raksti rits,ja pulkstens ir no 12 līdz 18 raksti diena un ja pulkstens ir no 18 līdz 24 raksti vakars )..."))

if a=="rits":
    print("Labrīt!")
elif a=="diena":
    print("Labdien!")
elif a=="vakars":
    print("Labvakar!")
    

