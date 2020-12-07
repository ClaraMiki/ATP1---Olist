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
            print("\n\n########### SUB MENU LISTAGEM ###########\n")
            print("1 - Sem filtro")
            print("2 - Com filtro")
            choice_option = int(input("Digite a sua escolha: "))

            if choice_option == 1:
                print("\n\n########### LISTAGEM DE PRODUTOS ###########\n")
                for product in products:
                    product.show_all()
                    print("------------------------------------\n")
            else:
                print("\n\n########### SUB MENU FILTROS ###########\n")
                print("0 - Posição")
                print("1 - Nome")
                print("2 - Preço")
                print("3 - Quantidade")
                print("4 - Descrição")
                choice_filter = int(input("Digite a sua escolha: "))

                if choice_filter == 0:
                    filter_position = int(input("\nFiltre por posição: "))
                    if filter_position > len(products) or filter_position < 0:
                        print("\n\n########### ERRO ###########")
                        print("     Posição inexistente     ")
                        print("############################\n\n")
                    else:
                        print("\n########### FILTRO - Posição: ", filter_position, " ###########\n")
                        products[filter_position].show_all()
                elif choice_filter == 1:
                    filter_name = input("\nFiltre por nome: ")
                    print("\n########### FILTRO - Nome: ", filter_name, " ###########\n")
                    for product in products:
                        if product.get_name() == filter_name:
                            product.show_all()
                            print("------------------------------------\n")
                elif choice_filter == 2:
                    filter_price = input("\nFiltre por preço: ")
                    print("\n########### FILTRO - Preço: ", filter_price, " ###########\n")
                    for product in products:
                        if product.get_price() == filter_price:
                            product.show_all()
                            print("------------------------------------\n")
                elif choice_filter == 2:
                    filter_quantity = input("\nFiltre por quantidade: ")
                    print("\n########### FILTRO - Quantidade: ", filter_quantity, " ###########\n")
                    for product in products:
                        if product.get_quantity() == filter_quantity:
                            product.show_all()
                            print("------------------------------------\n")
                elif choice_filter == 2:
                    filter_description = input("\nFiltre por descrição: ")
                    print("\n########### FILTRO - Descrição: ", filter_description, " ###########\n")
                    for product in products:
                        if product.get_description() == filter_description:
                            product.show_all()
                            print("------------------------------------\n")
                

    elif choice_option == 2:
        print("\n\n########### CADASTRO DE UM NOVO PRODUTO ###########\n")
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
            print("\n\n########### ALTERAÇÃO DE PRODUTO ###########\n")
            product_position = int(input("Digite a posição do produto que deseja alterar: "))
            if product_position > len(products) or product_position < 0:
                print("\n\n########### ERRO ###########")
                print("     Posição inexistente     ")
                print("############################\n\n")
            else:
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
            print("\n\n########### EXCLUSÃO DE PRODUTO ###########\n")
            product_position = int(input("Digite a posição do produto que deseja excluir: "))

            if product_position > len(products) or product_position < 0:
                print("\n\n########### ERRO ###########")
                print("     Posição inexistente     ")
                print("############################\n\n")
            else:
                products.pop(product_position)
                print("\nExcluído com sucesso!\n")