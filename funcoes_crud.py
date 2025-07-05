import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='-',
    password='-',
    database='crud-basico'
)

cursor = conexao.cursor()


#funcoes CRUD
def cadastrar_cliente():
    nome = (input("Nome do cliente: "))
    cpf = (input("CPF (apenas números): "))
    telefone = (input("Telefone (ex: 11945865236): "))

    comando = 'INSERT INTO clientes (nome, cpf, telefone) VALUES (%s, %s, %s)'
    valores = (nome, cpf, telefone)
    cursor.execute(comando, valores)
    conexao.commit()
    print("Cliente cadastrado com sucesso.")


def mostrar_cliente():
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()
    print("Lista de clientes:")
    for cliente in resultado:
        print(f'ID: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]} | Telefone: {cliente[3]}')


def atualizar_cliente():
    id_cliente = input("Digite o ID do cliente que deseja atualizar: ")
    novo_nome = (input("Novo nome do cliente: "))
    novo_cpf = (input("Novo CPF (apenas números): "))
    novo_telefone = (input("Novo telefone (ex: 11945865236): "))

    comando = 'UPDATE clientes SET nome=%s, cpf=%s, telefone=%s WHERE id=%s'
    valores = (novo_nome, novo_cpf, novo_telefone, id_cliente)
    cursor.execute(comando, valores)
    conexao.commit()
    print("Cliente atualizado com sucesso!")


def deletar_cliente():
    id_cliente = input("Digite o ID do cliente que deseja deletar: ")
    comando = ('DELETE FROM clientes WHERE id=%s')
    valores = (id_cliente, )
    cursor.execute(comando, valores)
    conexao.commit()

    #verifica se houve alteracao no BD
    if cursor.rowcount == 0:
        print("Nenhum cliente encontrado com esse ID.")
    else:
        print("Cliente removido.")