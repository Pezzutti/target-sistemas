n = int(input("Digite o número a ser testado: "))
curr = 1
prev = 0
aux = 0
seq = [0,1]

while curr < n:
    aux = curr
    curr = prev + curr
    prev = aux
    seq.append(curr)

print(seq)

if n in seq:
    print(f"{n} faz parte da sequência.")
else:
    print(f"{n} não faz parte da sequência.")