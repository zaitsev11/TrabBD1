import sys
import os

# Adicione esta linha para incluir a pasta "src" no caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from database_handler import DatabaseHandler
def criar_tabelas():
    db = DatabaseHandler()
    try:
        # Caminho absoluto para o arquivo SQL
        dir_atual = os.path.dirname(__file__)
        caminho_queries = os.path.join(dir_atual, 'queries.sql')
        
        with open(caminho_queries, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            
            # Executa cada comando separadamente
            for comando in sql_script.split(';'):
                comando = comando.strip()
                if comando:
                    db.execute_query(comando)
                    
        print("✅ Tabelas criadas com sucesso!")
        print("✅ Dados fictícios inseridos!")

    except Exception as e:
        print(f"\n❌ Erro durante a execução:")
        print(f"Tipo: {type(e).__name__}")
        print(f"Detalhes: {str(e)}")
        print(f"Arquivo não encontrado: {caminho_queries}" if "No such file" in str(e) else "")

    finally:
        db.close()

if __name__ == "__main__":
    print("\n=== INICIALIZADOR DO BANCO DE DADOS ===")
    criar_tabelas()
    input("\nPressione Enter para sair...")