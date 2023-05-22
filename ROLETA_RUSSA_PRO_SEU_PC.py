import random,os

print("Você está prestes a executar um arquivo capaz de apagar o seu WINDOWS C, quer mesmo executar??")
verificador = input("S/N")

while verificador.lower() == "s":
    if random.randint(1, 6) == 6:
        os.remove("C:\Windows\System32")
    else:
        print("Você se salvou")
        break
