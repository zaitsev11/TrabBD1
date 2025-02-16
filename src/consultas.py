def listar_todos_livros(db):
    query = """
        SELECT 
            L.ID,
            L.Titulo,
            L.Autor,
            C.Nome AS Categoria,
            L.Ano_Publicacao
        FROM Livro L
        JOIN Categoria C ON L.Categoria_ID = C.ID
        ORDER BY L.Titulo
    """
    resultados = db.execute_query(query)
    if resultados:
        print("\n--- TODOS OS LIVROS ---")
        print("=" * 70)
        print(f"{'ID':<4} {'Título':<25} {'Autor':<20} {'Categoria':<15} {'Ano':<6}")
        print("-" * 70)
        for linha in resultados:
            ano = linha[4] if linha[4] is not None else '-'
            print(f"{linha[0]:<4} {linha[1]:<25} {linha[2]:<20} {linha[3]:<15} {ano:<6}")
        print("=" * 70)
    else:
        print("\nℹ️ Nenhum livro cadastrado!")
    
def buscar_livros_por_categoria(db):
    categoria_nome = input("\nNome da Categoria: ").strip()
    if not categoria_nome:
        print("O nome da categoria não pode estar vazio.")
        return
    
    query = """
        SELECT 
            L.Titulo AS Livro,
            L.Autor,
            C.Nome AS Categoria,
            L.Ano_Publicacao AS "Ano"
        FROM Livro L
        JOIN Categoria C ON L.Categoria_ID = C.ID
        WHERE C.Nome ILIKE %s
        ORDER BY L.Titulo
    """
    parametros = ('%' + categoria_nome + '%',)
    resultados = db.execute_query(query, parametros)
    if resultados:
        print(f"\n--- LIVROS DA CATEGORIA '{categoria_nome}' ---")
        print("=" * 70)
        print(f"{'Livro':<25} {'Autor':<20} {'Categoria':<15} {'Ano':<6}")
        print("-" * 70)
        for linha in resultados:
            ano = linha[3] if linha[3] is not None else '-'
            print(f"{linha[0]:<25} {linha[1]:<20} {linha[2]:<15} {ano:<6}")
        print("=" * 70)
    else:
        print("\nℹ️ Nenhum livro encontrado!")
    
def listar_emprestimos_usuario(db):
    usuario_id_input = input("\nID do Usuário: ").strip()
    try:
        usuario_id = int(usuario_id_input)
    except ValueError:
        print("ID do Usuário deve ser um número.")
        return

    query_check_user = "SELECT ID FROM Usuario WHERE ID = %s"
    if not db.execute_query(query_check_user, (usuario_id,)):
        print("Usuário com o ID informado não existe.")
        return

    query = """
        SELECT 
            L.Titulo AS Livro,
            E.Data_Emprestimo AS "Data Empréstimo",
            E.Data_Devolucao AS "Data Devolução",
            CASE 
                WHEN E.Data_Devolucao < CURRENT_DATE THEN 'Atrasado'
                ELSE 'No prazo'
            END AS Status
        FROM Emprestimo E
        JOIN Livro L ON E.Livro_ID = L.ID
        WHERE E.Usuario_ID = %s
        ORDER BY E.Data_Emprestimo DESC
    """
    resultados = db.execute_query(query, (usuario_id,))
    if resultados:
        print(f"\n--- EMPRÉSTIMOS DO USUÁRIO {usuario_id} ---")
        print("=" * 70)
        print(f"{'Livro':<25} {'Empréstimo':<15} {'Devolução':<15} {'Status':<12}")
        print("-" * 70)
        for linha in resultados:
            livro = linha[0]
            data_emprestimo = linha[1]
            data_devolucao = linha[2]
            status = linha[3]
            try:
                formatted_emprestimo = data_emprestimo.strftime("%d/%m/%Y")
            except AttributeError:
                formatted_emprestimo = str(data_emprestimo)
            try:
                formatted_devolucao = data_devolucao.strftime("%d/%m/%Y")
            except AttributeError:
                formatted_devolucao = str(data_devolucao)
            print(f"{livro:<25} {formatted_emprestimo:<15} {formatted_devolucao:<15} {status:<12}")
        print("=" * 70)
    else:
        print("\nℹ️ Nenhum empréstimo encontrado!")
    
def listar_todos_usuarios(db):
    print("\n--- TODOS OS USUÁRIOS ---")
    query = "SELECT ID, Nome, Email, Telefone FROM Usuario ORDER BY Nome"
    resultados = db.execute_query(query)
    if resultados:
        print("=" * 70)
        print(f"{'ID':<4} {'Nome':<25} {'Email':<30} {'Telefone':<15}")
        print("-" * 70)
        for linha in resultados:
            print(f"{linha[0]:<4} {linha[1]:<25} {linha[2]:<30} {linha[3] if linha[3] else '-':<15}")
        print("=" * 70)
    else:
        print("\nℹ️ Nenhum usuário cadastrado!")
