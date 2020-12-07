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
        if len(products) == 0:
           print("\n\nNão há produtos cadastrados ainda!")
        else:
            print("\n\n########### LISTAGEM DE PRODUTOS ###########\n\n")
            for product in products:
                product.show_all()
                print("------------------------------------\n")

    elif choice_option == 2:
        print("\n\n########### CADASTRO DE UM NOVO PRODUTO ###########")
        product_name = input("Digite o nome do produto: ")
        product_price = input("Digite o preço do produto: ") 
        product_quantity = input("Digite a quantidade de estoque do produto: ")
        product_description = input("Digite a descrição do produto: ")

        products.append(product.Product(name = product_name, price = product_price, quantity = product_quantity, description = product_description))
        print("\nCadastro concluído com sucesso!")
    elif choice_option == 3:
        if len(products) == 0:
            print("\n\nNão há produtos cadastrados ainda!")
        else:
            print("\n\n########### ALTERAÇÃO DE PRODUTO ###########")
            product_position = int(input("Digite a posição do produto que deseja alterar: "))
            products[product_position].show_all()

            name = input("Digite o novo nome: ")
            price = input("Digite o novo preço: ")
            quantity = input("Digite a nova quantidade: ")
            description = input("Digite a nova descrição: ")

            products[product_position].set_name(name)
            products[product_position].set_price(price)
            products[product_position].set_quantity(quantity)
            products[product_position].set_description(description)

            print("\n\nAlteração feita com sucesso!\n\n")
    elif choice_option == 4:
        if len(products) == 0:
            print("\n\nNão há produtos cadastrados ainda!")
        else:
            print("\n\n########### EXCLUSÃO DE PRODUTO ###########")
            product_position = int(input("Digite a posição do produto que deseja excluir: "))

            if product_position > len(products):
                print("\n\n########### ERRO ###########")
                print("     Posição inexistente     ")
                print("############################\n\n")
            else:
                products.pop(product_position)
                print("Excluído com sucesso!\n")