print("Exemplo continue")
for v in range(1, 10):
    if(v == 8):
        continue
    print("Valor: " + str(v))

print("===============")
print("Exemplo break")    
for v in range(1, 10):
    if(v == 8):
        break
    print("Valor: " + str(v))    