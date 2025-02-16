# Justificativa do Tema e Relevância

## Tema: Sistema de Gerenciamento de Biblioteca

A escolha do tema para a relevância prática e educacional. Um sistema informatizado para gerenciar os processos de uma biblioteca traz diversas vantagens, tais como:

- **Organização e Controle:** Automatiza o cadastro, atualização, remoção e consulta de livros, categorias, usuários, empréstimos e multas.
- **Suporte à Tomada de Decisão:** Gera relatórios que auxiliam na identificação de empréstimos atrasados, agrupamento por categoria e a identificação dos livros mais populares.
- **Desenvolvimento de Competências Técnicas:** Permite a prática de programação orientada a objetos utilizando tecnologias modernas como Python e PostgreSQL.

## Relevância

A implementação deste sistema não apenas oferece uma solução prática para o gerenciamento de bibliotecas, mas também serve como uma ferramenta de aprendizado para a aplicação de conceitos teóricos em um contexto real. O sistema possibilita a administração eficiente dos livros e dos empréstimos.

---

# Documentação e Apresentação

## Estrutura do Projeto

O projeto está organizado de forma modular, distribuído nos seguintes arquivos:

- **database_handler.py:**  
  Responsável pela conexão com o banco de dados PostgreSQL. Configura o _search_path_ para o schema `biblioteca`, gerencia transações e executa as queries necessárias.

- **models.py:**  
  Define as classes que representam as entidades do sistema: `Livro`, `Usuario` e `Emprestimo`.

- **cadastros.py:**  
  Contém as funções para os cadastros:
  - **cadastrar_livro(db):** Recebe os dados do livro, verifica se a categoria existe e, se não existir, cadastra-a automaticamente. Em seguida, insere o livro.
  - **cadastrar_usuario(db):** Recebe os dados do usuário e verifica se já existe um usuário com o mesmo email antes de inserir.

- **operacoes.py:**  
  - **registrar_emprestimo(db):** Verifica se o livro e o usuário existem, e se a data de devolução é posterior à data atual, antes de registrar o empréstimo.
  - **atualizar_livro(db) e excluir_livro(db):** Permitem atualizar ou excluir um livro, após validação da existência.
  - **atualizar_usuario(db) e excluir_usuario(db):** Permitem atualizar ou excluir um usuário, com checagem prévia.

- **consultas.py:**  
  Contém funções para consulta de dados:
  - **listar_todos_livros(db):** Exibe todos os livros cadastrados.
  - **buscar_livros_por_categoria(db):** Permite buscar livros por nome da categoria.
  - **listar_emprestimos_usuario(db):** Exibe os empréstimos de um usuário específico.
  - **listar_todos_usuarios(db):** Exibe todos os usuários cadastrados.

- **relatorios.py:**  
  Agrupa funções que geram relatórios avançados:
  - **relatorio_atrasados(db):** Lista os empréstimos com data de devolução anterior à data atual, mostrando os dias de atraso.
  - **relatorio_emprestimos_por_categoria(db):** Agrupa os empréstimos por categoria e exibe o total de empréstimos por categoria.
  - **relatorio_livros_mais_emprestados(db):** Lista os 10 livros com maior número de empréstimos.

- **main.py:**  
  Exibe um menu interativo organizado por seções (Cadastros, Operações, Consultas e Relatórios) e chama as funções dos módulos correspondentes conforme a opção escolhida.

---

## Funcionalidades Implementadas

- **Cadastros:**  
  - **Livro:** Cadastro de livros solicitando título, autor, ISBN e nome da categoria. Se a categoria informada não existir, ela é cadastrada automaticamente.
  - **Usuário:** Cadastro de usuários com nome, email e telefone. Verifica duplicidade de email.

- **Operações:**  
  - **Registrar Empréstimo:** Registro de empréstimos com validação para garantir que o livro e o usuário existam e que a data de devolução seja posterior à data atual.
  - **Atualizar/Excluir Livro:** Permite atualizar ou excluir um livro após validação de existência.
  - **Atualizar/Excluir Usuário:** Permite atualizar ou excluir um usuário após validação de existência.

- **Consultas:**  
  - **Listar Todos os Livros:** Exibe todos os livros cadastrados com detalhes.
  - **Buscar Livros por Categoria:** Permite filtrar os livros por nome de categoria.
  - **Listar Empréstimos de um Usuário:** Exibe os empréstimos realizados por um usuário específico.
  - **Listar Todos os Usuários:** Exibe todos os usuários cadastrados.

- **Relatórios Avançados:**  
  - **Livros Atrasados:** Lista os empréstimos em que a data de devolução é anterior à data atual, com indicação dos dias de atraso.
  - **Empréstimos por Categoria:** Agrupa e exibe o total de empréstimos por categoria.
  - **Livros Mais Emprestados:** Lista os 10 livros com maior número de empréstimos.

---

## Documentação do Código

### 1. `database_handler.py`

- **Objetivo:**  
  Gerencia a conexão com o banco de dados PostgreSQL, define o _search_path_ para o schema `biblioteca` e executa as queries.
  
- **Destaques:**  
  - Configuração do encoding para UTF-8.
  - Método `execute_query(query, params)` que executa queries, commit, e retorna resultados para SELECT ou queries com RETURNING.
  - Em caso de erro, faz rollback e exibe a mensagem de erro.

### 2. `models.py`

- **Objetivo:**  
  Define as classes de dados que representam as entidades do sistema.
  
- **Classes:**  
  - `Livro`: Armazena título, autor, ISBN, ID da categoria e ano de publicação.
  - `Usuario`: Armazena nome, email e telefone.
  - `Emprestimo`: Armazena o ID do livro, o ID do usuário e a data de devolução.

### 3. `cadastros.py`

- **Objetivo:**  
  Contém funções para cadastrar novos registros.
  
- **Funções:**  
  - `cadastrar_livro(db)`: Recebe os dados do livro e, se a categoria não existir, a cadastra automaticamente.
  - `cadastrar_usuario(db)`: Recebe os dados do usuário e verifica duplicidade de email antes de inserir.

### 4. `operacoes.py`

- **Objetivo:**  
  Contém funções para operações de negócio.
  
- **Funções:**  
  - `registrar_emprestimo(db)`: Verifica se o livro e o usuário existem e se a data de devolução é posterior à data atual, então insere o empréstimo.
  - `atualizar_livro(db)`: Permite atualizar os dados de um livro, após confirmar que o registro existe.
  - `excluir_livro(db)`: Exclui um livro, verificando a existência do registro e solicitando confirmação.
  - `atualizar_usuario(db)`: Atualiza os dados de um usuário, se ele existir.
  - `excluir_usuario(db)`: Exclui um usuário, após validação e confirmação.

### 5. `consultas.py`

- **Objetivo:**  
  Contém funções para consulta e listagem dos registros.
  
- **Funções:**  
  - `listar_todos_livros(db)`: Lista todos os livros com detalhes.
  - `buscar_livros_por_categoria(db)`: Permite buscar livros filtrados por nome da categoria.
  - `listar_emprestimos_usuario(db)`: Lista os empréstimos de um usuário específico.
  - `listar_todos_usuarios(db)`: Lista todos os usuários cadastrados.

### 6. `relatorios.py`

- **Objetivo:**  
  Contém funções para gerar relatórios avançados.
  
- **Funções:**  
  - `relatorio_atrasados(db)`: Lista os empréstimos atrasados, mostrando os dias de atraso.
  - `relatorio_emprestimos_por_categoria(db)`: Agrupa e exibe o total de empréstimos por categoria.
  - `relatorio_livros_mais_emprestados(db)`: Lista os 10 livros com maior número de empréstimos.

### 7. `main.py`

- **Objetivo:**  
  Ponto de entrada do sistema. Exibe um menu interativo organizado em seções e chama as funções dos módulos conforme a opção escolhida.
  
- **Fluxo:**  
  - Exibe o menu com opções para Cadastros, Operações, Consultas e Relatórios.
  - Após cada operação, aguarda o usuário pressionar Enter para continuar.
  - Ao sair, fecha a conexão com o banco.

---

## Instruções de Execução

### Pré-Requisitos

- **Banco de Dados:**  
  PostgreSQL. Execute o script SQL para criar e povoar as tabelas certifique-se de que o schema biblioteca esteja criado.

- **Ambiente Python:**  
  Instale a biblioteca `psycopg2`:
  ```bash
  pip install psycopg2
