class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.set_ano(ano)
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Titulo: {self.__titulo} - Ano: {self.__ano} - Disponibilidade: {self.__disponivel}")

    def emprestar(self):
        if self.__disponivel == True:
            self.__disponivel = False
            print(f"O livro {self.__titulo} foi emprestado!")
        else:
            print(f"O livro {self.__titulo} não está disponível!")

    def devolver(self):
        if self.__disponivel == False:
            self.__disponivel = True
            print(f"O livro {self.__titulo} foi devolvido!")
        else:
            print(f"Não foi possível devolver o livro {self.__titulo}.")

    def set_ano(self, ano):
        if ano >= 0:
            self.__ano = ano
        else:
           raise ValueError ("Ano deve ser maior que zero.")
    
    def get_titulo(self, titulo):
        if self.__titulo.strip() != "":
            self.__titulo = titulo
        else:
            print("Título não pode ser vazio.")