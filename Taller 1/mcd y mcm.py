n1 = int(input("ingrese el primer valor: "))
n2 = int(input("ingrese el segundo valor: "))

mcd = 0
mcm = 0

if n1 % 2 == 0 and n2 % 2 == 0:
    if n1 < n2:
        for i in range(1, n1 + 1, 1):
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
    else:
        if n1 > n2:
            i = 1            
            while i <= n2:
                if n1 % i == 0 and n2 % i == 0:
                    mcd = i
                    i = i + 1
        else:
            mcd = n1
    print(mcd)

if n1 % 2 != 0 and n2 % 2 != 0:
    if n1 < n2:
        for i in range(1, n1 + 1, 1):
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
    else:
        if n1 > n2:
            i = 1
            while i <= n2:
                if n1 % i == 0 and n2 % i == 0:
                    mcd = i
                i = i + 1
        else:
            mcd = n1
    print(mcd)

if n1 % 2 != 0 and n2 % 2 == 0:
    if n1 < n2:
        for i in range(n1 * n2, n1 - 1, -1):
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
    else:
        if n1 > n2:
            for i in range(n1 * n2, n2 - 1, -1):
                if i % n1 == 0 and i % n2 == 0:
                    mcm = i
        else:
            mcm = n2
    print(mcm)

if n1 % 2 == 0 and n2 % 2 != 0:
    if n1 < n2:
        for i in range(n1 * n2, n1 - 1, -1):
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
    else:
        if n1 > n2:
            for i in range(n1 * n2, n2 - 1, -1):
                if i % n1 == 0 and i % n2 == 0:
                    mcm = i
        else:
            mcm = n2
    print(mcm)