import os
import pyodbc
import pandas as pd
def limpar_tela():
    os.system("cls")
def conectar_banco():
    server = 'localhost'
    database = 'petshop'
    username = 'sa'
    password = '*123456HAS*'
    return pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

def cadastrar_pet(cursor, conn):
    tipo = input("Tipo do pet: ")
    nome = input("Nome do pet: ")
    idade = int(input("Idade do pet: "))
    query = "INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES (?, ?, ?)"
    cursor.execute(query, (tipo, nome, idade))
    conn.commit()
    print("Pet cadastrado com sucesso!")
    input("Pressione Enter para continuar...")

def listar_pets(cursor):
    cursor.execute("SELECT * FROM petshop")
    data = cursor.fetchall()
    if not data:
        print("Não há pets cadastrados.")
    else:
        df = pd.DataFrame.from_records(data, columns=["Id", "Tipo", "Nome", "Idade"], index="Id")
        print(df)
    input("Pressione Enter para continuar...")

def modificar_pet(cursor, conn):
    listar_pets(cursor)
    id_pet = int(input("Digite o ID do pet a ser modificado: "))
    tipo = input("Novo tipo do pet: ")
    nome = input("Novo nome do pet: ")
    idade = int(input("Nova idade do pet: "))
    query = "UPDATE petshop SET tipo_pet = ?, nome_pet = ?, idade = ? WHERE id = ?"
    cursor.execute(query, (tipo, nome, idade, id_pet))
    conn.commit()
    print("Pet modificado com sucesso!")
    input("Pressione Enter para continuar...")

def deletar_pet(cursor, conn):
    listar_pets(cursor)
    id_pet = int(input("Digite o ID do pet a ser deletado: "))
    query = "DELETE FROM petshop WHERE id = ?"
    cursor.execute(query, (id_pet,))
    conn.commit()
    print("Pet deletado com sucesso!")
    input("Pressione Enter para continuar...")

def excluir_todos_pets(cursor, conn):
    cursor.execute("DELETE FROM petshop")
    conn.commit()
    print("Todos os pets foram excluídos com sucesso!")
    input("Pressione Enter para continuar...")

def menu():
    limpar_tela()
    print("""
    PETSHOP
    0 - Sair
    1 - Cadastrar pet
    2 - Listar pets
    3 - Modificar pet
    4 - Deletar pet
    5 - Excluir todos os pets
    """)
    return int(input("Insira a opção: "))

def main():
    limpar_tela()
    conn = conectar_banco()
    cursor = conn.cursor()
    while True:
        escolha = menu()
        limpar_tela()

        match escolha:
            case 0:
                print("Saindo do sistema...")
                break
            case 1:
                cadastrar_pet(cursor, conn)
            case 2:
                listar_pets(cursor)
            case 3:
                modificar_pet(cursor, conn)
            case 4:
                deletar_pet(cursor, conn)
            case 5:
                excluir_todos_pets(cursor, conn)
            case _:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

    conn.close()
    print("Conexão encerrada.")


main()
