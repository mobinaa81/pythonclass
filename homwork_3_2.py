print("be mashin hesab khosh amadid ^_^")
adad1 = float(input("lotfan adad avval ra vared konid \n"))
adad2 = float(input("hala adad dovvom ra vared konid \n"))
amaliat = input("khoob hala chikareshon konam?  + jame  - tafriq  * zarb  \
/ taqsim  ** tavan\n")
#______________________________________________________________
def amaliaat (adad1 , adad2 , amaliat):
    if amaliat == "+":
        return adad1 + adad2
    elif amaliat == "-":
        return adad1 - adad2
    elif amaliat == "*":
        return adad1 * adad2
    elif amaliat == "/":
        return adad1 / adad2
    elif amaliat == "**":
        return adad1 ** adad2
    else :
        print("balad nistam:(")
#___________________________________________________________________
javab = amaliaat(adad1, adad2 ,amaliat)
print(f"pasokh amaliat shoma ={javab}")
