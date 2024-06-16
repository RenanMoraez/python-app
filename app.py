import os

restaurantes = [{'nome':'Praça', 'categoria': 'japonesa', 'ativo':False},
{'nome':'pizza suprema', 'categoria':'Piza','ativo':True},
{'nome':'Cantina', 'categoria':'Italiana','ativo':False}]

def menu_principal():
    print("""
 (             (      (                     (          )              )   (      (            (      (         )   
 )\ )          )\ )   )\ )                  )\ )    ( /(           ( /(   )\ )   )\ )         )\ )   )\ )   ( /(   
(()/(    (    (()/(  (()/(   (   (    (    (()/(    )\())    (     )\()) (()/(  (()/(   (    (()/(  (()/(   )\())  
 /(_))   )\    /(_))  /(_))  )\  )\   )\    /(_))  ((_)\     )\   ((_)\   /(_))  /(_))  )\    /(_))  /(_)) ((_)\   
(_))_   ((_)  (_))   (_))   ((_)((_) ((_)  (_))   __ ((_)   ((_)  __((_) (_))   (_))   ((_)  (_))   (_))     ((_)  
 |   \  | __| | |    |_ _|  \ \ / /  | __| | _ \  \ \ / /   | __| \ \/ / | _ \  | _ \  | __| / __|  / __|   / _ \  
 | |) | | _|  | |__   | |    \ V /   | _|  |   /   \ V /    | _|   >  <  |  _/  |   /  | _|  \__ \  \__ \  | (_) | 
 |___/  |___| |____| |___|    \_/    |___| |_|_\    |_|     |___| /_/\_\ |_|    |_|_\  |___| |___/  |___/   \___/  
                                                                                                                   
""")

def sub_titulos(texto):
    """
    Esta função faz com que apareça os titulos nas telas que chamamos de HEAD
    """
    os.system("cls")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def listas_de_opcoes():
    """
    Esta função faz com que apareça os menus
    """
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternando o estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    """
    Esta função faz com que termine a sua aplicação
    
    """
    sub_titulos('Finalizando app')

def alternar_estado_restaurante():
    """
    Esta função faz com que você altere o ativo para desativado
    """
    sub_titulos('Alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    volta_menu()
    
def opcao_invalida():
    """
    Esta função faz com que apareça uma mensagem de erro na sua tela 
    """
    print("opção invalida\n")
    volta_menu()

def volta_menu():
    """
    Esta função faz com que você volte para o menu principal
    """
    input("Para voltar ao menu digite qualquer tecla")
    main()

def cadastrar_novo_restaurante():
    """
    Esta função faz com que você cadastre um novo restaurante 
    """
    sub_titulos("Cadastrar Restaurantes")
    nome_do_restaurante = input("Qual é o nome do seu restaurante: ")
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nParabéns! O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n")
    volta_menu()

def listar_restaurantes():
    """
    Esta função faz com que os restaurantes ja cadastrados apareçam para você
    """
    sub_titulos("Listando Restaurantes")

    print(f"{'Nome do restautante'.ljust(22)} | {'Categoria'.ljust(20)} | Estatus")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    volta_menu()

def escolhas_das_listas():
    """
    Esta função é uma regra de negocio para suas opções dentro do menu
    """
    try:
        opcao_escolher = int(input("Qual sua opção? "))

        if opcao_escolher == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolher == 2:
            listar_restaurantes()
        elif opcao_escolher == 3:
            alternar_estado_restaurante()
        elif opcao_escolher == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
        
def main():
    """
    Esta função é a principal
    """
    os.system('cls')
    menu_principal()
    listas_de_opcoes()
    escolhas_das_listas()

if __name__ == '__main__':
    main()