# Documentação do Diagrama de Relacionamento (DBML)

Este documento descreve o diagrama de relacionamento para o sistema de biblioteca, incluindo as tabelas e os relacionamentos com nomes definidos.

## Tabelas

### Categoria
- **ID**: `serial` (Chave Primária)
- **Nome**: `varchar(50)` (Único e não nulo)

### Livro
- **ID**: `serial` (Chave Primária)
- **Titulo**: `varchar(100)` (Não nulo)
- **Autor**: `varchar(50)`
- **ISBN**: `varchar(20)` (Único)
- **Categoria_ID**: `int` (Não nulo)  
  - Chave estrangeira referenciando `Categoria.ID`
- **Ano_Publicacao**: `int`

### Usuario
- **ID**: `serial` (Chave Primária)
- **Nome**: `varchar(50)` (Não nulo)
- **Email**: `varchar(50)` (Não nulo, Único)
- **Telefone**: `varchar(15)`

### Emprestimo
- **ID**: `serial` (Chave Primária)
- **Livro_ID**: `int` (Não nulo)  
  - Chave estrangeira referenciando `Livro.ID`
- **Usuario_ID**: `int` (Não nulo)  
  - Chave estrangeira referenciando `Usuario.ID`
- **Data_Emprestimo**: `date` (Padrão: `CURRENT_DATE`)
- **Data_Devolucao**: `date` (Não nulo)  
  - *Restrição*: Deve ser maior que a `Data_Emprestimo`

### Multa
- **ID**: `serial` (Chave Primária)
- **Emprestimo_ID**: `int` (Não nulo, Único)  
  - Chave estrangeira referenciando `Emprestimo.ID`
- **Valor**: `decimal(10,2)` (Padrão: `0.0`)
- **Status**: `varchar(10)` (Padrão: `'Pendente'`)  
  - *Restrição*: Valores permitidos: `'Pendente'`, `'Pago'`, `'Cancelado'`

## Relacionamentos

Os relacionamentos entre as tabelas estão definidos da seguinte forma, com nomes personalizados para facilitar o entendimento:

- **Pertence a**  
  - **Definição**: Relaciona `Livro.Categoria_ID` com `Categoria.ID`
  - **Descrição**: Cada livro pertence a uma única categoria.

- **Empresta**  
  - **Definição**: Relaciona `Emprestimo.Livro_ID` com `Livro.ID`
  - **Descrição**: Cada empréstimo está associado a um livro.

- **Realizado por**  
  - **Definição**: Relaciona `Emprestimo.Usuario_ID` com `Usuario.ID`
  - **Descrição**: Cada empréstimo é realizado por um usuário.

- **Gera**  
  - **Definição**: Relaciona `Multa.Emprestimo_ID` com `Emprestimo.ID`
  - **Descrição**: Cada multa é gerada por um único empréstimo (relação 1:1).

## Código DBML

Você pode utilizar o código abaixo no [dbdiagram.io](https://dbdiagram.io/) para visualizar o diagrama com os relacionamentos nomeados:

```dbml
Table Categoria {
  ID serial [pk, increment]
  Nome varchar(50) [not null, unique]
}

Table Livro {
  ID serial [pk, increment]
  Titulo varchar(100) [not null]
  Autor varchar(50)
  ISBN varchar(20) [unique]
  Categoria_ID int [not null]
  Ano_Publicacao int
}

Table Usuario {
  ID serial [pk, increment]
  Nome varchar(50) [not null]
  Email varchar(50) [not null, unique]
  Telefone varchar(15)
}

Table Emprestimo {
  ID serial [pk, increment]
  Livro_ID int [not null]
  Usuario_ID int [not null]
  Data_Emprestimo date [default: `CURRENT_DATE`]
  Data_Devolucao date [not null] // CHECK: Data_Devolucao > Data_Emprestimo
}

Table Multa {
  ID serial [pk, increment]
  Emprestimo_ID int [not null, unique]
  Valor decimal(10,2) [default: 0.0]
  Status varchar(10) [default: 'Pendente'] // CHECK: Status IN ('Pendente', 'Pago', 'Cancelado')
}

// Relacionamentos com nomes
Ref: Livro.Categoria_ID > Categoria.ID [name: "Pertence a"]
Ref: Emprestimo.Livro_ID > Livro.ID [name: "Empresta"]
Ref: Emprestimo.Usuario_ID > Usuario.ID [name: "Realizado por"]
Ref: Multa.Emprestimo_ID > Emprestimo.ID [name: "Gera"]
