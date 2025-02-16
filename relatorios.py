def relatorio_atrasados(db):
    query = """
        SELECT 
            U.Nome AS Usuario,
            L.Titulo AS Livro,
            E.Data_Devolucao AS "Data Limite",
            AGE(CURRENT_DATE, E.Data_Devolucao) AS "Dias de Atraso"
        FROM Emprestimo E
        JOIN Usuario U ON E.Usuario_ID = U.ID
        JOIN Livro L ON E.Livro_ID = L.ID
        WHERE E.Data_Devolucao < CURRENT_DATE
        ORDER BY E.Data_Devolucao
    """
    resultados = db.execute_query(query)
    if resultados:
        print("\n--- LIVROS ATRASADOS ---")
        print("=" * 70)
        print(f"{'Usuário':<20} {'Livro':<25} {'Data Limite':<15} {'Atraso':<10}")
        print("-" * 70)
        for linha in resultados:
            usuario = linha[0]
            livro = linha[1]
            data_limite = linha[2]
            dias_atraso = linha[3]
            try:
                formatted_data_limite = data_limite.strftime("%d/%m/%Y")
            except AttributeError:
                formatted_data_limite = str(data_limite)
            print(f"{usuario:<20} {livro:<25} {formatted_data_limite:<15} {str(dias_atraso):<10}")
        print("=" * 70)
    else:
        print("\nNenhum atraso registrado!")
    
def relatorio_emprestimos_por_categoria(db):
    query = """
        SELECT C.Nome AS Categoria, COUNT(E.ID) AS Total_Emprestimos
        FROM Emprestimo E
        JOIN Livro L ON E.Livro_ID = L.ID
        JOIN Categoria C ON L.Categoria_ID = C.ID
        GROUP BY C.Nome
        ORDER BY Total_Emprestimos DESC;
    """
    resultados = db.execute_query(query)
    if resultados:
        print("\n--- EMPRÉSTIMOS POR CATEGORIA ---")
        print("=" * 70)
        print(f"{'Categoria':<25} {'Total Empréstimos':<20}")
        print("-" * 70)
        for linha in resultados:
            print(f"{linha[0]:<25} {linha[1]:<20}")
        print("=" * 70)
    else:
        print("\nℹ️ Nenhum empréstimo encontrado para categorias!")
    
def relatorio_livros_mais_emprestados(db):
    query = """
        SELECT L.Titulo AS Livro, COUNT(E.ID) AS Total_Emprestimos
        FROM Emprestimo E
        JOIN Livro L ON E.Livro_ID = L.ID
        GROUP BY L.Titulo
        ORDER BY Total_Emprestimos DESC
        LIMIT 10;
    """
    resultados = db.execute_query(query)
    if resultados:
        print("\n--- LIVROS MAIS EMPRESTADOS ---")
        print("=" * 70)
        print(f"{'Livro':<40} {'Total Empréstimos':<20}")
        print("-" * 70)
        for linha in resultados:
            print(f"{linha[0]:<40} {linha[1]:<20}")
        print("=" * 70)
    else:
        print("\nℹ️ Nenhum empréstimo registrado!")
