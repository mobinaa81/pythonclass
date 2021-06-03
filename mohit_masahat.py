tool = int(input("tool ra vared kon\n"))
arz = int(input("arz ra vared kon\n"))
soal = input("masahat mikhai ya mohit?")

def masahat_mostatil (tool , arz):
    masahat = (tool * arz)
    print (masahat)

def mohit_mostatil (tool , arz):
    mohit = (tool + arz) * 2
    print (mohit)

if soal == "masahat" :
    mohit_mostatil (tool , arz)
if soal == "mohit" :
    mohit_mostatil (tool , arz)
