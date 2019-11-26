print("here is where i will type out the instructions")
import time 
var1 = " "
var2 = " "
var3 = " "
var4 = " "
var5 = " "
var6 = " "
var7 = " "
var8 = " "
var9 = " "
gamecounter = 0
wincondition = False
yourwincondition = False
while gamecounter != 9:
    print(var1,"|",var2,"|",var3)
    print("----------")
    print(var4,"|",var5,"|",var6)
    print("----------")
    print(var7,"|",var8,"|",var9)
    gamecounter += 1
    mark1 = input("imput your next mark: ")
    if mark1 == "1":
        var1 = "x"
        
    if mark1 == "2":
        var2 = "x"
        
    if mark1 == "3":
        var3 = "x"
        
    if mark1 == "4":
        var4 = "x"
        
    if mark1 == "5":
        var5 = "x"
        
    if mark1 == "6":
        var6 = "x"
        
    if mark1 == "7":
        var7 = "x"
        
    if mark1 == "8":
        var8 = "x"
        
    if mark1 == "9":
        var9 = "x"
        
    if var5 == "x":
        if var2 == "x":
            if var8 == "x":
                yourwincondition = True
                
    if var3 == "x":
        if var6 == "x":
            if var9 == "x":
                yourwincondition = True
    if var1 == "x":
        if var4 == "x":
            if var7 == "x":
                yourwincondition = True                
    if var1 == "x":
        if var2 == "x":
            if var3 == "x":
                yourwincondition = True
    if var4 == "x":
        if var5 == "x":
            if var6 == "x":
                yourwincondition = True
    if var7 == "x":
        if var8 == "x":
            if var9 == "x":
                yourwincondition = True
    if var1 == "x":
        if var5 == "x":
            if var9 == "x":
                yourwincondition = True
    if var3 == "x":
        if var5 == "x":
            if var7 == "x":
                yourwincondition = True

                
    if var5 == "o":
        if var2 == "o":
            if var8 == "o":
                wincondition = True
                
    if var3 == "o":
        if var6 == "o":
            if var9 == "o":
                wincondition = True
    if var1 == "o":
        if var4 == "o":
            if var7 == "o":
                wincondition = True                
    if var1 == "o":
        if var2 == "o":
            if var3 == "o":
                wincondition = True
    if var4 == "o":
        if var5 == "o":
            if var6 == "o":
                wincondition = True
    if var7 == "o":
        if var8 == "o":
            if var9 == "o":
                wincondition = True
    if var1 == "o":
        if var5 == "o":
            if var9 == "o":
                wincondition = True
    if var3 == "o":
        if var5 == "o":
            if var7 == "o":
                wincondition = True
    if wincondition == True:
        break
    time.sleep(1)
    if var5 == " ":
        var5 = "o"
    else:
        if var1 == " ":
            var1 = "o"
        else:
            if var3 == " ":
                var3 = "o"
            else:
                if var9 == " ":
                    var9 = "o"
                else:
                    if var7 == " ":
                        var7 = "o"
                    else:
                       if var8 == " ":
                            var8 = "o"
                       else:
                            if var6 == " ":
                                var6 = "o"
                            else:
                                if var2 == " ":
                                    var2 = "o"
                                else:
                                    if var4 == " ":
                                        var4 = "o"
                                    else:
                                        gamecounter = 9
                                        print(var1,"|",var2,"|",var3)
                                        print("----------")
                                        print(var4,"|",var5,"|",var6)
                                        print("----------")
                                        print(var7,"|",var8,"|",var9)
                                        print("welp i guess the game now over...")


if wincondition == True:
    print("-\|/-")
    print("--0--")
    print("_/|\_")
    print("it looks like you didn't win!")

if yourwincondition == True:
    print("-\|/-")
    print("--0--")
    print("_/|\_")
    print("you won! conglaturalitaionas")
