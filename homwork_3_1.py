print("salam be mohasebegar man khosh amadid.. \n")

shekl = input("ba kodom shekl hendesi kar dari? (moraba , mostatil ,\
 mosalas , dayere)\n")

amaliat = input(f"mikhay mohit ya masahate {shekl} ro be dast biari?\n")

#_________________________________________________________________________

def entekhab(shekl, amaliat):
    if shekl == "mostatil" and amaliat == "mohit":
        tool_mostatil = int(input("tol mostatil chand ast?\n"))
        arz_mostatil = int(input("arz mostatil chand ast?"))
        mohit = (tool_mostatil+arz_mostatil)*2
        return mohit
    elif shekl == "mostatil" and amaliat == "masahat":
        tool_mostatil = input("tol mostatil chand ast?\n")
        arz_mostatil = input("arz mostatil chand ast?\n")
        masahat = tool_mostatil * arz_mostatil
        return masahat
        # -------------------------
    elif shekl == "moraba" and amaliat == "mohit":
        zele_moraba = int(input("andaze zele moraba chand ast?\n"))
        mohit = zele_moraba * 4
        return mohit
    elif shekl == "moraba" and amaliat == "masahat":
        zele_moraba = int(input("andaze zele moraba chand ast?\n"))
        masahat = zele_moraba * zele_moraba
        return masahat
        # ---------------------------
    elif shekl == "mosalas" and amaliat == "mohit":
        zele1 = int(input("meghdar zele aval?\n"))
        zele2 = int(input("meghdar zele davom?\n"))
        zele3 = int(input("meghdar zele sevom?\n"))
        mohit = zele1 + zele2 + zele3
        return mohit
    elif shekl == "mosalas" and amaliat == "masahat":
        ghaede = int(input("meghdar ghaede chand ast?\n"))
        ertefa = int(input("meghdar ertefa chand ast?\n"))
        masahat = (ertefa * ghaede) / 2
        return masahat
        #-------------------------------
    elif shekl == "dayere" and amaliat == "mohit":
        qotr = int(input("meghdar ghotr dayere chand ast?\n"))
        mohit = qotr * 3.14
        return mohit
    elif shekl == "dayere" and amaliat == "masahat":
        shoa = int(input("meghdar shoa chand ast?\n"))
        masahat = shoa * shoa * 3.14
        return masahat
#_____________________________________________________________________

javab= entekhab(shekl, amaliat)
print(""" \

************* javab shoma = """, javab)
