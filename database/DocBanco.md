# Documentação do Banco de Dados "Biblioteca"

Este documento descreve a estrutura do banco de dados **Biblioteca**, incluindo tabelas, relacionamentos e restrições. Em seguida, é apresentado o diagrama no formato compatível com o [dbdiagram.io](https://dbdiagram.io).

---

## Sumário

1. [Tabelas](#tabelas)
   - [Categoria](#tabela-categoria)
   - [Livro](#tabela-livro)
   - [Usuario](#tabela-usuario)
   - [Emprestimo](#tabela-emprestimo)
   - [Multa](#tabela-multa)
2. [Inserções de Dados (Exemplos)](#insercoes-de-dados)
3. [Diagrama (dbdiagram.io)](#diagrama-dbdiagramio)

---

## Tabelas

### Tabela: Categoria
- **Nome:** `Categoria`
- **Descrição:** Armazena as diferentes categorias de livros.
- **Colunas:**
  - `ID` (SERIAL, PRIMARY KEY): Identificador único da categoria.
  - `Nome` (VARCHAR(50) NOT NULL UNIQUE): Nome da categoria (ex: Ficção, Técnico, etc.).

### Tabela: Livro
- **Nome:** `Livro`
- **Descrição:** Contém informações sobre os livros do acervo.
- **Colunas:**
  - `ID` (SERIAL, PRIMARY KEY): Identificador único do livro.
  - `Titulo` (VARCHAR(100) NOT NULL): Título do livro.
  - `Autor` (VARCHAR(50)): Nome do autor do livro.
  - `ISBN` (VARCHAR(20) UNIQUE): Código ISBN único do livro.
  - `Categoria_ID` (INT NOT NULL REFERENCES Categoria(ID) ON DELETE CASCADE): Chave estrangeira que relaciona o livro à tabela **Categoria**. 
    - **Restrição:** Se uma categoria for excluída, todos os livros dessa categoria também serão excluídos (ON DELETE CASCADE).
  - `Ano_Publicacao` (INT): Ano de publicação do livro.

**Relacionamento:**  
- Uma **Categoria** pode ter **muitos** (**1:N**) livros (um para muitos).  
- Um **Livro** pertence a **uma** categoria.

### Tabela: Usuario
- **Nome:** `Usuario`
- **Descrição:** Contém os dados dos usuários que realizam empréstimos.
- **Colunas:**
  - `ID` (SERIAL, PRIMARY KEY): Identificador único do usuário.
  - `Nome` (VARCHAR(50) NOT NULL): Nome do usuário.
  - `Email` (VARCHAR(50) UNIQUE NOT NULL): Endereço de email único do usuário.
  - `Telefone` (VARCHAR(15)): Telefone de contato do usuário.

**Relacionamento:**  
- Um **Usuario** pode realizar **muitos** (**1:N**) empréstimos.

### Tabela: Emprestimo
- **Nome:** `Emprestimo`
- **Descrição:** Registra os empréstimos realizados, relacionando livros e usuários.
- **Colunas:**
  - `ID` (SERIAL, PRIMARY KEY): Identificador único do empréstimo.
  - `Livro_ID` (INT NOT NULL REFERENCES Livro(ID) ON DELETE CASCADE): Chave estrangeira para a tabela **Livro**.
    - **Restrição:** Se um livro for excluído, os empréstimos relacionados também são excluídos (ON DELETE CASCADE).
  - `Usuario_ID` (INT NOT NULL REFERENCES Usuario(ID) ON DELETE CASCADE): Chave estrangeira para a tabela **Usuario**.
    - **Restrição:** Se um usuário for excluído, seus empréstimos também são excluídos (ON DELETE CASCADE).
  - `Data_Emprestimo` (DATE DEFAULT CURRENT_DATE): Data em que o empréstimo foi feito.
  - `Data_Devolucao` (DATE NOT NULL CHECK (Data_Devolucao > Data_Emprestimo)): Data em que o livro deve ser devolvido.
    - **Restrição:** A data de devolução deve ser maior que a data de empréstimo.

**Relacionamentos:**
- Um **Livro** pode estar em **muitos** (**1:N**) empréstimos.
- Um **Usuario** pode ter **muitos** (**1:N**) empréstimos.

### Tabela: Multa
- **Nome:** `Multa`
- **Descrição:** Armazena as multas associadas aos empréstimos.
- **Colunas:**
  - `ID` (SERIAL, PRIMARY KEY): Identificador único da multa.
  - `Emprestimo_ID` (INT NOT NULL UNIQUE): Chave estrangeira para a tabela **Emprestimo**.
    - **Restrição:** Relação **1:1** com **Emprestimo**. Cada empréstimo tem no máximo uma multa.
    - Definida como `UNIQUE` para garantir que não exista mais de uma multa para o mesmo empréstimo.
  - `Valor` (DECIMAL(10, 2) DEFAULT 0.0): Valor da multa.
  - `Status` (VARCHAR(10) DEFAULT 'Pendente'): Status da multa.
    - **Restrição:** Só pode assumir os valores `'Pendente'`, `'Pago'` ou `'Cancelado'`.

**Relacionamento:**  
- Um **Emprestimo** pode ter **no máximo uma** multa (relação **1:1**).

---

## Inserções de Dados

```sql
-- Inserindo dados fictícios na tabela Categoria
INSERT INTO Categoria (Nome) VALUES 
    ('Ficção'), 
    ('Técnico'), 
    ('Biografia');

-- Inserindo dados fictícios na tabela Livro
INSERT INTO Livro (Titulo, Autor, ISBN, Categoria_ID, Ano_Publicacao) VALUES 
    ('1984', 'George Orwell', '978-0451524935', 1, 1949),
    ('Clean Code', 'Robert C. Martin', '978-0132350884', 2, 2008);

-- Inserindo dados fictícios na tabela Usuario
INSERT INTO Usuario (Nome, Email, Telefone) VALUES 
    ('João Silva', 'joao@email.com', '(11) 9999-8888'),
    ('Maria Souza', 'maria@email.com', '(11) 7777-6666');
