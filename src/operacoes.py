from models import Emprestimo
from datetime import datetime

def registrar_emprestimo(db):
    print("\n--- NOVO EMPRÉSTIMO ---")
    livro_input = input("ID do Livro: ").strip()
    usuario_input = input("ID do Usuário: ").strip()
    try:
        livro_id = int(livro_input)
        usuario_id = int(usuario_input)
    except ValueError:
        print("ID do Livro e ID do Usuário devem ser números.")
        return

    # Verifica se o livro existe
    query_check_book = "SELECT ID FROM Livro WHERE ID = %s"
    if not db.execute_query(query_check_book, (livro_id,)):
        print("Livro com o ID informado não existe.")
        return

    # Verifica se o usuário existe
    query_check_user = "SELECT ID FROM Usuario WHERE ID = %s"
    if not db.execute_query(query_check_user, (usuario_id,)):
        print("Usuário com o ID informado não existe.")
        return

    data_devolucao_input = input("Data Devolução (dd/mm/aaaa): ").strip()
    try:
        data_devolucao_dt = datetime.strptime(data_devolucao_input, "%d/%m/%Y")
        hoje = datetime.today()
        if data_devolucao_dt <= hoje:
            print("A data de devolução deve ser posterior à data atual.")
            return
        data_devolucao_sql = data_devolucao_dt.strftime("%Y-%m-%d")
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa.")
        return
    
    emprestimo = Emprestimo(livro_id, usuario_id, data_devolucao_sql)
    query = """
        INSERT INTO Emprestimo (Livro_ID, Usuario_ID, Data_Devolucao)
        VALUES (%s, %s, %s)
    """
    db.execute_query(query, (emprestimo.livro_id, emprestimo.usuario_id, emprestimo.data_devolucao))
    print("\nEmpréstimo registrado!")

def atualizar_livro(db):
    print("\n--- ATUALIZAR LIVRO ---")
    livro_id_input = input("ID do Livro para atualizar: ").strip()
    try:
        livro_id = int(livro_id_input)
    except ValueError:
        print("ID do Livro deve ser um número.")
        return

    query_check_book = "SELECT Titulo, Autor, ISBN FROM Livro WHERE ID = %s"
    livro_existente = db.execute_query(query_check_book, (livro_id,))
    if not livro_existente:
        print("Livro não encontrado!")
        return

    titulo_atual, autor_atual, isbn_atual = livro_existente[0]
    print("\nDeixe em branco para manter o valor atual")
    novo_titulo = input(f"Novo Título [{titulo_atual}]: ").strip() or titulo_atual
    novo_autor = input(f"Novo Autor [{autor_atual}]: ").strip() or autor_atual
    novo_isbn = input(f"Novo ISBN [{isbn_atual}]: ").strip() or isbn_atual

    query_update = """
        UPDATE Livro 
        SET Titulo = %s, Autor = %s, ISBN = %s 
        WHERE ID = %s
    """
    db.execute_query(query_update, (novo_titulo, novo_autor, novo_isbn, livro_id))
    print("\nLivro atualizado!")

def excluir_livro(db):
    print("\n--- EXCLUIR LIVRO ---")
    livro_id_input = input("ID do Livro para excluir: ").strip()
    try:
        livro_id = int(livro_id_input)
    except ValueError:
        print("ID do Livro deve ser um número.")
        return

    query_check_book = "SELECT ID FROM Livro WHERE ID = %s"
    if not db.execute_query(query_check_book, (livro_id,)):
        print("Livro com o ID informado não existe. Operação abortada.")
        return

    confirmacao = input("Tem certeza que deseja excluir este livro? (S/N): ").strip().upper()
    if confirmacao != "S":
        print("Operação cancelada!")
        return

    query = "DELETE FROM Livro WHERE ID = %s"
    db.execute_query(query, (livro_id,))
    print("\nLivro excluído!")

def atualizar_usuario(db):
    print("\n--- ATUALIZAR USUÁRIO ---")
    user_id_input = input("ID do Usuário para atualizar: ").strip()
    try:
        user_id = int(user_id_input)
    except ValueError:
        print("ID do Usuário deve ser um número.")
        return

    query_check_user = "SELECT Nome, Email, Telefone FROM Usuario WHERE ID = %s"
    user_data = db.execute_query(query_check_user, (user_id,))
    if not user_data:
        print("Usuário não encontrado!")
        return

    nome_atual, email_atual, telefone_atual = user_data[0]
    print("\nDeixe em branco para manter o valor atual")
    novo_nome = input(f"Novo Nome [{nome_atual}]: ").strip() or nome_atual
    novo_email = input(f"Novo Email [{email_atual}]: ").strip() or email_atual
    novo_telefone = input(f"Novo Telefone [{telefone_atual if telefone_atual else 'None'}]: ").strip() or telefone_atual

    query_update = "UPDATE Usuario SET Nome = %s, Email = %s, Telefone = %s WHERE ID = %s"
    db.execute_query(query_update, (novo_nome, novo_email, novo_telefone, user_id))
    print("\nUsuário atualizado!")

def excluir_usuario(db):
    print("\n--- EXCLUIR USUÁRIO ---")
    user_id_input = input("ID do Usuário para excluir: ").strip()
    try:
        user_id = int(user_id_input)
    except ValueError:
        print("ID do Usuário deve ser um número.")
        return

    query_check_user = "SELECT ID FROM Usuario WHERE ID = %s"
    if not db.execute_query(query_check_user, (user_id,)):
        print("Usuário com o ID informado não existe. Operação abortada.")
        return

    confirmacao = input("Tem certeza que deseja excluir este usuário? (S/N): ").strip().upper()
    if confirmacao != "S":
        print("Operação cancelada!")
        return

    query = "DELETE FROM Usuario WHERE ID = %s"
    db.execute_query(query, (user_id,))
    print("\nUsuário excluído!")
