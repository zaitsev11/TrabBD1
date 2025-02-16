from models import Livro, Usuario

def cadastrar_livro(db):
    print("\n--- NOVO LIVRO ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    isbn = input("ISBN: ").strip()

    categoria_nome = input("Nome da Categoria: ").strip()
    if not categoria_nome:
        print("O nome da categoria não pode estar vazio.")
        return

    query_category = "SELECT ID FROM Categoria WHERE LOWER(Nome) = LOWER(%s)"
    resultado = db.execute_query(query_category, (categoria_nome,))
    if resultado and len(resultado) > 0:
        categoria_id = resultado[0][0]
    else:
        insert_category = "INSERT INTO Categoria (Nome) VALUES (%s) RETURNING ID"
        res = db.execute_query(insert_category, (categoria_nome,))
        if res:
            categoria_id = res[0]
            print(f"Categoria '{categoria_nome}' cadastrada automaticamente.")
        else:
            print("Erro ao cadastrar nova categoria.")
            return

    ano_publicacao_input = input("Ano Publicação (opcional): ").strip()
    try:
        ano_publicacao = int(ano_publicacao_input) if ano_publicacao_input else None
    except ValueError:
        print("O ano de publicação deve ser um número.")
        return

    livro = Livro(titulo, autor, isbn, categoria_id, ano_publicacao)
    query = """
        INSERT INTO Livro (Titulo, Autor, ISBN, Categoria_ID, Ano_Publicacao)
        VALUES (%s, %s, %s, %s, %s)
    """
    db.execute_query(query, (livro.titulo, livro.autor, livro.isbn, livro.categoria_id, livro.ano_publicacao))
    print("\nLivro cadastrado!")

def cadastrar_usuario(db):
    print("\n--- NOVO USUÁRIO ---")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    telefone = input("Telefone (opcional): ").strip() or None

    query_check = "SELECT ID FROM Usuario WHERE Email = %s"
    if db.execute_query(query_check, (email,)):
        print("Já existe um usuário com esse e-mail.")
        return

    query = """
        INSERT INTO Usuario (Nome, Email, Telefone)
        VALUES (%s, %s, %s)
    """
    db.execute_query(query, (nome, email, telefone))
    print("\nUsuário cadastrado!")
