# 📚 Sistema de Biblioteca (POO em Python)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![POO](https://img.shields.io/badge/paradigma-POO-purple)

Sistema simples de gerenciamento de biblioteca desenvolvido em Python, utilizando **Programação Orientada a Objetos (POO)**.

---

## ✨ Funcionalidades

- 📖 Cadastro de livros  
- 📰 Cadastro de revistas  
- 📋 Listagem de itens  
- 📦 Empréstimo de itens por código  
- 🔄 Devolução de itens por código  
- ⚠️ Validação de entradas numéricas  

---

## 🧱 Estrutura do Projeto

```bash
biblioteca-poo/
│
├── biblioteca.py        # Gerencia os itens
├── item_biblioteca.py   # Superclasse dos itens
├── livro.py             # Classe Livro
├── revista.py           # Classe Revista
├── main.py              # Menu interativo
└── README.md