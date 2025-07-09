import random
print("=== Bem-vindo ao Restaurante===")

nome = input("Por favor, informe seu nome: ")
cpf = input("Por favor, informe seu CPF (11 dígitos): ")

quantidade_pessoas = input("Quantas pessoas estarão na reserva? ")
data_reserva = input("Para qual data deseja reservar? (ex: 08/07/2025): ")
horario_reserva = input("Qual horário deseja reservar? (ex: 19:30): ")



numero_mesas = random.randint (1,69)


print (" O valor da reserva é R$ 80,00")
print (" ====Selecione a forma de pagamento====")
print ("1- Cartão de débito")
print ("2- Cartão de crédito")
print ("3- Pix")
opcao = input("Escolha um método de pagamento acima: ")
if opcao == 1:
    print ("Sua reserva foi confirmada com sucesso!")
elif opcao == 2:
    print("Sua reserva foi confirmada com sucesso!")
else:
    print("Sua reserva foi confirmada com sucesso!")


print("Responsável pela reserva:", nome)
print("CPF do responsável:", cpf)
print(f"Número de pessoas: {quantidade_pessoas}")
print(f"Data: {data_reserva}")
print(f"Horário: {horario_reserva}")
print("\n.")

