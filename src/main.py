from database_handler import DatabaseHandler
from cadastro import cadastrar_livro, cadastrar_usuario
from operacoes import (
    registrar_emprestimo, atualizar_livro, excluir_livro,
    atualizar_usuario, excluir_usuario
)
from consultas import (
    listar_todos_livros, buscar_livros_por_categoria,
    listar_emprestimos_usuario, listar_todos_usuarios
)
from relatorios import (
    relatorio_atrasados, relatorio_emprestimos_por_categoria,
    relatorio_livros_mais_emprestados
)

def exibir_menu():
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("\n--- CADASTROS ---")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    
    print("\n--- OPERAÇÕES ---")
    print("3. Registrar Empréstimo")
    print("4. Atualizar Livro")
    print("5. Excluir Livro")
    print("6. Atualizar Usuário")
    print("7. Excluir Usuário")
    
    print("\n--- CONSULTAS ---")
    print("8. Listar Todos os Livros")
    print("9. Buscar Livros por Categoria")
    print("10. Listar Empréstimos de um Usuário")
    print("11. Listar Todos os Usuários")
    
    print("\n--- RELATÓRIOS ---")
    print("12. Relatório de Livros Atrasados")
    print("13. Relatório de Empréstimos por Categoria")
    print("14. Relatório dos Livros Mais Emprestados")
    
    print("\n0. Sair")
    return input("Escolha uma opção: ")

def main():
    db = DatabaseHandler()
    try:
        while True:
            opcao = exibir_menu()
            if opcao == "1":
                cadastrar_livro(db)
            elif opcao == "2":
                cadastrar_usuario(db)
            elif opcao == "3":
                registrar_emprestimo(db)
            elif opcao == "4":
                atualizar_livro(db)
            elif opcao == "5":
                excluir_livro(db)
            elif opcao == "6":
                atualizar_usuario(db)
            elif opcao == "7":
                excluir_usuario(db)
            elif opcao == "8":
                listar_todos_livros(db)
            elif opcao == "9":
                buscar_livros_por_categoria(db)
            elif opcao == "10":
                listar_emprestimos_usuario(db)
            elif opcao == "11":
                listar_todos_usuarios(db)
            elif opcao == "12":
                relatorio_atrasados(db)
            elif opcao == "13":
                relatorio_emprestimos_por_categoria(db)
            elif opcao == "14":
                relatorio_livros_mais_emprestados(db)
            elif opcao == "0":
                print("\n🚪 Sistema encerrado!")
                break
            else:
                print("\n❌ Opção inválida!")
            input("\nPressione Enter para continuar...")
    finally:
        db.close()

if __name__ == "__main__":
    main()
