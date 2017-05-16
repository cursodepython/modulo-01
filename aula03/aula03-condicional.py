idade = int(input("Digite a idade"))

if idade < 16 :
    print("não pode votar")
elif idade >= 16 and idade < 18:
    print("pode votar (não é obrigatório)")
elif idade >= 18 and idade < 70:
    print("pode votar (é obrigatório)")
else:
    print("pode votar (não é obrigatório)")