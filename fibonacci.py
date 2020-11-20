seq = []
n = 0
F = 0
nMax = int(input("Nejvyšší počítaná pozice v posloupnosti: "))
while n <= nMax:
    if n == 0:
        F = 0
    elif n == 1:
        F = 1
    else:
        F = seq[n - 1] + seq[n - 2]
    seq.append(F)
    print(str(F))
    n = len(seq)
