SET search_path TO biblioteca;

-- Criação das tabelas com restrições
CREATE TABLE Categoria (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Livro (
    ID SERIAL PRIMARY KEY,
    Titulo VARCHAR(100) NOT NULL,
    Autor VARCHAR(50),
    ISBN VARCHAR(20) UNIQUE,
    Categoria_ID INT NOT NULL REFERENCES Categoria(ID) ON DELETE CASCADE,
    Ano_Publicacao INT
);

CREATE TABLE Usuario (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE NOT NULL,
    Telefone VARCHAR(15)
);

CREATE TABLE Emprestimo (
    ID SERIAL PRIMARY KEY,
    Livro_ID INT NOT NULL REFERENCES Livro(ID) ON DELETE CASCADE,
    Usuario_ID INT NOT NULL REFERENCES Usuario(ID) ON DELETE CASCADE,
    Data_Emprestimo DATE DEFAULT CURRENT_DATE,
    Data_Devolucao DATE NOT NULL CHECK (Data_Devolucao > Data_Emprestimo)
);

-- Tabela Multa
CREATE TABLE Multa (
    ID SERIAL PRIMARY KEY,
    Emprestimo_ID INT NOT NULL UNIQUE,-- Relação 1:1 com empréstimo
    Valor DECIMAL(10, 2) DEFAULT 0.0,
    Status VARCHAR(10) DEFAULT 'Pendente',
    CONSTRAINT fk_emprestimo
        FOREIGN KEY (Emprestimo_ID)
        REFERENCES Emprestimo(ID)
        ON DELETE CASCADE,
    CONSTRAINT check_status
        CHECK (Status IN ('Pendente', 'Pago', 'Cancelado'))  -- Valores permitidos
);

-- Dados fictícios
INSERT INTO Categoria (Nome) VALUES 
    ('Ficção'), ('Técnico'), ('Biografia');

INSERT INTO Livro (Titulo, Autor, ISBN, Categoria_ID, Ano_Publicacao) VALUES 
    ('1984', 'George Orwell', '978-0451524935', 1, 1949),
    ('Clean Code', 'Robert C. Martin', '978-0132350884', 2, 2008);

INSERT INTO Usuario (Nome, Email, Telefone) VALUES 
    ('João Silva', 'joao@email.com', '(11) 9999-8888'),
    ('Maria Souza', 'maria@email.com', '(11) 7777-6666');