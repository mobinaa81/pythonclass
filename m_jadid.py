tool= int(input("tool ra vared kon\n"))
arz= int(input("arz ra vared kon\n"))
amaliat= input("mohitesh ro mikhay ya masahat?\n")
def mostatil(tool, arz, amaliat):
    if amaliat == "masahat":
      masahat= tool * arz
      return masahat

    elif amaliat == "mohit":
        mohit= (tool + arz) * 2
        return mohit

javab= mostatil(tool, arz, amaliat)
print(javab)
