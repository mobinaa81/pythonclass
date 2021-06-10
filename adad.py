adad = 0
while adad <= 1000 :
    print (adad)
    command = input("bishtaresh konam ya kamtar?\n")
    if command == "bishtar" :
        adad +=1
    elif command == "kamtar" :
        adad -=1
    else :
        print("bye")
