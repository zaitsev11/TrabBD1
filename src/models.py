class Livro:
    def __init__(self, titulo, autor, isbn, categoria_id, ano_publicacao=None):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.categoria_id = categoria_id
        self.ano_publicacao = ano_publicacao

class Usuario:
    def __init__(self, nome, email, telefone=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Emprestimo:
    def __init__(self, livro_id, usuario_id, data_devolucao):
        self.livro_id = livro_id
        self.usuario_id = usuario_id
        self.data_devolucao = data_devolucao

class Categoria:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Multa:
    STATUS_PERMITIDOS = ['Pendente', 'Pago', 'Cancelado']
    
    def __init__(self, emprestimo_id, valor, status='Pendente'):
        self.emprestimo_id = emprestimo_id
        self.valor = valor
        self.status = status if status in self.STATUS_PERMITIDOS else 'Pendente'

    def validar_status(self):
        if self.status not in self.STATUS_PERMITIDOS:
            raise ValueError(f"Status inválido. Valores permitidos: {', '.join(self.STATUS_PERMITIDOS)}")

    def __str__(self):
        return f"Multa: R${self.valor:.2f} - Status: {self.status}"
