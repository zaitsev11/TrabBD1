import psycopg2

class DatabaseHandler:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="NovaSenha123!"
        )
        self.conn.autocommit = True
        # Configura o encoding para UTF-8
        self.conn.set_client_encoding('UTF8')
        self.cursor = self.conn.cursor()
        # Define o schema "biblioteca"
        self.cursor.execute("SET search_path TO biblioteca;")
    
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
            # Se a query tem RETURNING, retorna o resultado (apenas uma linha)
            if "RETURNING" in query.upper():
                return self.cursor.fetchone()
            # Se for SELECT, retorna todas as linhas
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print(f"Erro: {e}")
            return None
    
    def close(self):
        self.cursor.close()
        self.conn.close()
