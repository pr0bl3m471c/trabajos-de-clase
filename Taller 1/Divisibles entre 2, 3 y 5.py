n = int(input("inserte un número entero: "))

div2 = False
div3 = False
div5 = False

for i in range(1, n+1):
    
    if i % 2 == 0:
        div2 = True
    
    if i % 3 == 0:
        div3 = True
    
    if i % 5 == 0:
        div5 = True
    
    
    
    if div2:
        
        if div3 and div5:
            print(str(i) + " - divisible entre 2, 3 y 5")
            
        elif div3:
            print(str(i) + " - divisble entre 2 y 3")
            
        elif div5:
            print(str(i) + " - divisble entre 2 y 5")
            
        else:
            print(str(i) + " - divisible entre 2")
    
    elif div3:
            
        if div5:
            print(str(i) + " - divisble entre 3 y 5")
            
        else:
            print(str(i) + " - divisible entre 3")
            
    elif div5:
        print(str(i) + " - divisble entre 5")
        
    else:
        print(str(i) + " - ")
    
    
    div2 = False
    div3 = False
    div5 = False            