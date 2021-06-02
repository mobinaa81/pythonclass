#mohasebe BMI
print("salam be mohasebegar BMI khosh amadid ^_^")
qad = float(input("lotfan ghad khod ra vared konid(m)\n"))
vazn = float(input("lotfan vazn khod ra vared konid(kg)\n"))
BMI = vazn/(qad**2)

if BMI < 18.5 :
    print("BMI shoma =" ,BMI)
    print("shoma kambood vazn darid :(")

if 18.5 <= BMI <= 24.9 :
    print("BMI shoma =" ,BMI)
    print("shoma vazn monaseb darid :D")

if 24.9 < BMI <= 29.9 :
    print("BMI shoma =" ,BMI)
    print("shoma kami ezafe vann darid :(")
if BMI > 29.9 :
    print("BMI shoma =" ,BMI)
    print("shoma ezafe vazn  shadid darid :O")
