import classes

def cls():
    print("\n" * 100)

choice_option = 1
products = []
categories = []

def get_index_category_by_id(value):
    for position in range(len(categories)):
        print(position)
        if categories[position].get_identifier() == value:
            return position
        position += 1
    return -1

def separate_comma_blankspace(value):
    string = value.strip()
    string_separated = string.split(",")
    return string_separated

while choice_option != 8:
    print("\n\n################# Menu #####################")
    print("#                                          #")
    print("#     0 - Listar as categorias             #")
    print("#     1 - Cadastrar uma categoria ou sub   #")
    print("#                                          #")
    print("#     2 - Listar as sub categoria          #")
    print("#                                          #")
    print("#     4 - Listar os produtos               #")
    print("#     5 - Cadastrar um produto             #")
    print("#     6 - Alterar um produto               #")
    print("#     7 - Excluir um produto               #")
    print("#                                          #")
    print("#     8 - Sair                             #\n")
    choice_option = int(input("Digite a operação que deseja fazer: "))

    if choice_option not in [0,1,2,3,4,5,6,7,8]:
        print("\n\n########### Por favor, digite uma opção válida! ###########")
    elif choice_option == 8:
        break
    elif choice_option == 0:
        cls()
        if len(categories) == 0:
           print("\n\nNão há categorias cadastradas ainda!")
        else:
            print("\n\n########## LISTAGEM DE CATEGORIAS #########\n")
            for category in categories:
                category.show_all()
                print("-----------------------------------------\n")
    elif choice_option == 1:
        cls()
        print("\n\n######### CADASTRO DE UMA NOVA CATEGORIA #########")
        print("#                                                #")
        category_id = input("# Digite a identificação: ")
        category_desc = input("# Digite a descrição da categoria: ")
        print("\n# 1 - Sim")
        print("# 2 - Não")
        if_sub = int(input("Esta categoria é uma sub categoria? "))
        if if_sub == 1:
            category_type = "sub"
        else:
            category_type = "main"

        categories.append(classes.Category(identifier = category_id, description = category_desc, category_type = category_type))
        if if_sub == 1:
            category_parent = input("Qual categoria pai ela está vinculada? ")
            categories_size = len(categories) - 1
            categories[categories_size].set_sub_category(category_parent)
        print("\nCadastro concluído com sucesso!")

    elif choice_option == 2:
        cls()
        if len(categories) == 0:
           print("\n\nNão há categorias cadastradas ainda!")
        else:
            print("\n\n########## LISTAGEM DE SUB CATEGORIAS #########\n")
            for category in categories:
                print("- ", category.get_sub_category())
    elif choice_option == 4:
        if len(products) == 0:
           print("\n\nNão há produtos cadastrados ainda!")
        else:
            cls()
            print("\n\n########### SUB MENU LISTAGEM ###########")
            print("#                                       #")
            print("#            1 - Sem filtro             #")
            print("#            2 - Com filtro             #\n")
            choice_option = int(input("Digite a sua escolha: "))

            if choice_option == 1:
                print("\n\n########## LISTAGEM DE PRODUTOS #########\n")
                for product in products:
                    product.show_all()
                    print("-----------------------------------------\n")
            else:
                print("\n\n########### SUB MENU FILTROS ###########")
                print("#                                      #")
                print("#            0 - Posição               #")
                print("#            1 - Nome                  #")
                print("#            2 - Preço                 #")
                print("#            3 - Quantidade            #")
                print("#            4 - Descrição             #\n")
                choice_filter = int(input("Digite a sua escolha: "))

                cls()
                
                if choice_filter == 0:
                    filter_position = int(input("\nFiltre por posição: "))
                    if filter_position > len(products) or filter_position < 0:
                        print("\n\n########### ERRO ###########")
                        print("#    Posição inexistente    #")
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
                

    elif choice_option == 5:
        cls()
        print("\n\n######### CADASTRO DE UM NOVO PRODUTO #########")
        print("#                                             #")
        product_name = input("# Digite o nome do produto: ")
        product_price = input("# Digite o preço do produto: ") 
        product_quantity = input("# Digite a quantidade de estoque do produto: ")
        product_description = input("# Digite a descrição do produto: ")
        if len(product_description) < 20:
            print("\nDescrição mínima de 20 caracteres!\n")
        else:
            products.append(classes.Product(name = product_name, price = product_price, quantity = product_quantity, description = product_description))
            print("\nCadastro concluído com sucesso!")
            cls()
            print("# 1 - Sim")
            print("# 2 - Não")
            register_category = int(input("\n# Deseja cadastrar uma categoria ao produto? "))
            if register_category == 1:
                if len(categories) == 0:
                    print("\nNão há categorias cadastradas ainda!\n")
                else:
                    print("\n\n######### LISTAGEM DAS CATEGORIAS #########\n")
                    for category in categories:
                        print("Identificador: ", category.get_identifier())
                        print("Descrição: ", category.get_description())
                        print("\n---------------------------------------\n")
                    category_choosen = input("Escolha as categoria pelo seu identificador, separadas por virgulas: ")
                    separate_comma_blankspace(category_choosen)
                    product_size = len(products) - 1
                    products[product_size].set_category(category_choosen)
                    print("\nCadastro concluído com sucesso!")

                    cls()
                    print("# 1 - Sim")
                    print("# 2 - Não")
                    register_sub_category = int(input("\n# Deseja cadastrar uma sub categoria ao produto? "))
                    if register_sub_category == 1:
                        index_category = get_index_category_by_id(category_choosen)
                        if index_category != -1:
                            sub_categories = categories[index_category].get_sub_category()
                            print("\n\n######### LISTAGEM DAS SUB CATEGORIAS #########\n")
                            for sub in sub_categories:
                                print("# ", sub)
                        else:
                            print("\n\n#################### ERRO ########################")
                            print("   O sistema não conseguiu identificar a categoria    ")
                            print("##################################################\n\n")

    elif choice_option == 6:
        if len(products) == 0:
            print("\n\nNão há produtos cadastrados ainda!")
        else:
            cls()
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
    elif choice_option == 7:
        if len(products) == 0:
            print("\n\nNão há produtos cadastrados ainda!")
        else:
            cls()
            print("\n\n########### EXCLUSÃO DE PRODUTO ###########\n")
            product_position = int(input("Digite a posição do produto que deseja excluir: "))

            if product_position > len(products) or product_position < 0:
                print("\n\n########### ERRO ###########")
                print("     Posição inexistente     ")
                print("############################\n\n")
            else:
                products.pop(product_position)
                print("\nExcluído com sucesso!\n")