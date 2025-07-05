import funcoes_crud as crud
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='-',
    password='-',
    database='crud-basico'
)

cursor = conexao.cursor()

#programa principal
while True:
    print('Cadastro de Clientes')
    print('1 - Cadastrar novo cliente.')
    print('2 - Mostrar lista de clientes.')
    print('3 - Atualizar cadastro de cliente.')
    print('4 - Deletar cadastro de cliente.')
    print('5 - Encerrar programa.')
    opcao = int(input('Escolha: '))

    if opcao == 1:
        crud.cadastrar_cliente()
    elif opcao == 2:
        crud.mostrar_cliente()
    elif opcao == 3:
        crud.atualizar_cliente()
    elif opcao == 4:
        crud.deletar_cliente()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")

cursor.close()
conexao.close()