dic = {}
while True:
    print("===== MENU =====")
    print("1 - Cadastrar ")
    print("2 - Buscar ")
    print("3 - Excluir ")
    print("4 - Listar ")
    print("5 - Sair ")
    op = input("Escolha uma opção: ")
    if op == "1":
        print("==== CADASTRAR CONTATO ====")
        nome = input("Digite o nome: ")
        # se já existe
        if nome in dic:
            print("Contato já existe!")
            print(f"Nome: {nome}")
            print(f"Telefone atual: {dic[nome]['telefone']}")
            atualizar = input("Deseja atualizar este número? (s/n): ")
            if atualizar == "s":
                novo_telefone = input("Digite o novo telefone: ")
                dic[nome]["telefone"] = novo_telefone
                print("Telefone atualizado com sucesso!")
            elif atualizar == "n":
                print("Nenhuma alteração realizada.")
            else:
                print("Comando inválido!")
     # se não existe
        else:
            telefone = input("Digite o telefone: ")
            dic[nome] = {"telefone": telefone}
            print("Contato cadastrado com sucesso!")
    elif op == "2":
        print("===== BUSCAR =====")
        nome = input("Digite o nome do contato desejado: ")
        if nome in dic:
            print(f"O contato de {nome} já foi cadastrado. Telefone: {dic[nome]['telefone']}")
        else:
            print("O contato não foi encontrado. Por favor, faça o cadastro!")
    elif op == "3":
        print("===== EXCLUIR CONTATO =====")
        nome = input("Digite o nome do contato que deseja excluir: ")
 
        if nome in dic:
            print(f"Nome: {nome}")
            print(f"Telefone: {dic[nome]['telefone']}")
 
            confirmar = input("Tem certeza que deseja excluir? (s/n): ")
 
            if confirmar == "s":
                del dic[nome]
                print("Contato excluído com sucesso!")
            elif confirmar == "n":
                print("Exclusão cancelada.")
            else:
                print("Comando inválido!")
        else:
            print("Contato não encontrado.")
    elif op == "4":
        print("===== LISTAR =====")
        for nome, dados in dic.items():
            print(f"Nome: {nome} | Telefone: {dados['telefone']}")
    elif op == "5":
        print("Saindo do programa...")
        break
    else:
        print("Valor inválido!")