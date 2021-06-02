#tamrin mashin hesab
print("salam be mashin hesab mobina khosh amadid ^_^")

adad_aval = float(input("lotfan adad avval ra vared konid \n"))
adad_dovom = float(input("hala adad dovvom ra vared konid \n"))
amaliaat = input("khoob hala chikareshon konam?  + jame  - tafriq  * zarb  \
/ taqsim  ** tavan\n")

if amaliaat == "+":
    print("mishe" , adad_aval + adad_dovom)

elif amaliaat == "-":
    print("mishe" ,adad_aval - adad_dovom)

elif amaliaat == "*":
    print("mishe" ,adad_aval * adad_dovom)

elif amaliaat == "/":
    if adad_dovom != 0:
      print("mishe" ,adad_aval / adad_dovom)
    else :
        print("adad taqsim bar 0? :)")

elif amaliaat == "**":
    print("mishe" ,adad_aval % adad_dovom)

else :
    print("motasefam doostam ino balad nistam:(")
print("          'try me again if you want' ")
