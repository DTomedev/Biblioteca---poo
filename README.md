📚 Sistema de Biblioteca (POO em Python)








Sistema simples de gerenciamento de biblioteca desenvolvido em Python, utilizando Programação Orientada a Objetos (POO).

✨ Funcionalidades
📖 Cadastro de livros
📰 Cadastro de revistas
📋 Listagem de itens
📦 Empréstimo de itens por código
🔄 Devolução de itens por código
⚠️ Validação de entradas numéricas
🧱 Estrutura do Projeto
biblioteca-poo/
│
├── biblioteca.py        # Gerencia os itens
├── item_biblioteca.py   # Superclasse dos itens
├── livro.py             # Classe Livro
├── revista.py           # Classe Revista
├── main.py              # Menu interativo
└── README.md
🧠 Conceitos Utilizados
Programação Orientada a Objetos (POO)
Herança
Encapsulamento
Polimorfismo
Tratamento de exceções (try/except)
▶️ Como Executar
🔧 Pré-requisitos
Python 3 instalado
▶️ Execução
python main.py
💻 Exemplo de Uso

Ao executar o sistema, você verá:

1. Cadastrar Livro
2. Cadastrar Revista
3. Listar Itens
4. Emprestar Item (por código)
5. Devolver Item (por código)
6. Sair
📌 Regras do Sistema
Cada item possui um código único
Um item só pode ser emprestado se estiver disponível
Um item só pode ser devolvido se estiver emprestado
Entradas inválidas são tratadas para evitar erros

🔧 Melhorias Futuras
💾 Persistência de dados (arquivo ou banco)
🔍 Busca por título ou autor
👤 Sistema de usuários
📊 Histórico de empréstimos
🖥️ Interface gráfica
👨‍💻 Autor

Projeto desenvolvido para fins de estudo de POO em Python.