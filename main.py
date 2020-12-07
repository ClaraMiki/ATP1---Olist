import product

choice_option = 1
products = []

while choice_option != 5:
    print("\n\n########### Menu ###########")
    print("1 - Listar os produtos")
    print("2 - Cadastrar um novo produto")
    print("3 - Alterar um produto")
    print("4 - Excluir um produto")
    print("5 - Sair\n")
    choice_option = int(input("Digite a operação que deseja fazer: "))

    if choice_option not in [1,2,3,4,5]:
        print("\n\n########### Por favor, digite uma opção válida! ###########")
    elif choice_option == 5:
        break
    elif choice_option == 1:
        print("\n\n########### LISTAGEM DE PRODUTOS ###########")
        for product in products:
            print("Nome: ", product.get_name())
            print("Preço: ", product.get_price())
            print("Quantidade: ", product.get_quantity())
            print("Descrição: ", product.get_description())
            print("\n------------------------------------\n")

    elif choice_option == 2:
        print("\n\n########### CADASTRO DE UM NOVO PRODUTO ###########")
        product_name = input("Digite o nome do produto: ")
        product_price = input("Digite o preço do produto: ") 
        product_quantity = input("Digite a quantidade de estoque do produto: ")
        product_description = input("Digite a descrição do produto: ")

        products.append(product.Product(name = product_name, price = product_price, quantity = product_quantity, description = product_description))
        print("\nCadastro concluído com sucesso!")
    elif choice_option == 3:
        print("\n\n########### ALTERAÇÃO DE PRODUTO ###########")
        product_position = int(input("Digite a posição do produto que deseja alterar: "))
    elif choice_option == 4:
        print("\n\n########### EXCLUSÃO DE PRODUTO ###########")
        product_position = int(input("Digite a posição do produto que deseja excluir: "))
        #if product_position > products.length:
        #   print("Posição inexistente")
        #else:
        #   products.index(product_position)
        #comentado para nao dar erro