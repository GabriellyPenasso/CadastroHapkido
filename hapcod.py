# Lista de usuários
usuarios = []

# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Criar Aluno")
    print("2. Criar Instrutor")
    print("3. Criar Professor")
    print("4. Listar usuários")
    print("5. Atualizar usuário")
    print("6. Deletar usuário")
    print("7. Sair")

# Função para criar um novo Aluno
def criar_aluno():
    nome = input("Digite o Nome do Aluno: ")
    idade = input("Digite a Idade do Aluno: ")
    graduacao = input("Digite a Graduação do Aluno: ")
    genero = input("Digite o Gênero do Aluno: ")
    cpf = input("Digite o CPF do Aluno: ")
    email = input("Digite o Email do Aluno: ")
    endereco = input("Digite o Endereço do Aluno: ")
    usuario = {'Tipo': 'Aluno', 'Nome': nome, 'Idade': idade, 'Graduação': graduacao, 'Gênero': genero, 'CPF': cpf, 'Email': email, 'Endereço': endereco}
    usuarios.append(usuario)
    print("Aluno criado com sucesso!")

# Função para criar um novo Instrutor
def criar_instrutor():
    nome = input("Digite o Nome do Instrutor: ")
    idade = input("Digite a Idade do Instrutor: ")
    graduacao = input("Digite a Graduação do Instrutor: ")
    genero = input("Digite o Gênero do Instrutor: ")
    cpf = input("Digite o CPF do Instrutor: ")
    email = input("Digite o Email do Instrutor: ")
    endereco = input("Digite o Endereço do Instrutor: ")
    usuario = {'Tipo': 'Instrutor', 'Nome': nome, 'Idade': idade, 'Graduação': graduacao, 'Gênero': genero, 'CPF': cpf, 'Email': email, 'Endereço': endereco}
    usuarios.append(usuario)
    print("Instrutor criado com sucesso!")

# Função para criar um novo Professor
def criar_professor():
    nome = input("Digite o Nome do Professor: ")
    idade = input("Digite a Idade do Professor: ")
    graduacao = input("Digite a Graduação do Professor: ")
    genero = input("Digite o Gênero do Professor: ")
    cpf = input("Digite o CPF do Professor: ")
    email = input("Digite o Email do Professor: ")
    endereco = input("Digite o Endereço do Professor: ")
    usuario = {'Tipo': 'Professor', 'Nome': nome, 'Idade': idade, 'Graduação': graduacao, 'Gênero': genero, 'CPF': cpf, 'Email': email, 'Endereço': endereco}
    usuarios.append(usuario)
    print("Professor criado com sucesso!")

# Função para listar todos os usuários em formato de tabela
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    headers = ["Tabela", "Nome", "Idade", "Graduação", "Gênero", "CPF", "Email", "Endereço"]
    print(f"\n{' | '.join(headers)}")
    print("-" * (len(headers) * 15))
    
    for usuario in usuarios:
        linha = [usuario['Tipo'], usuario['Nome'], usuario['Idade'], usuario['Graduação'], usuario['Gênero'], usuario['CPF'], usuario['Email'], usuario['Endereço']]
        print(f"{' | '.join(linha)}")

# Função para atualizar um usuário
def atualizar_usuario():
    cpf = input("Digite o CPF do usuário que deseja atualizar: ")
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            usuario['Nome'] = input("Novo nome do usuário: ")
            usuario['Idade'] = input("Nova idade do usuário: ")
            usuario['Graduação'] = input("Nova Graduação do usuário: ")
            usuario['Email'] = input("Novo email do usuário: ")
            usuario['Endereço'] = input("Novo endereço do usuário: ")
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

# Função para deletar um usuário
def deletar_usuario():
    cpf = input("Digite o CPF do usuário que deseja deletar: ")
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            usuarios.remove(usuario)
            print("Usuário deletado com sucesso!")
            return
    print("Usuário não encontrado.")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        criar_aluno()
    elif opcao == '2':
        criar_instrutor()
    elif opcao == '3':
        criar_professor()
    elif opcao == '4':
        listar_usuarios()
    elif opcao == '5':
        atualizar_usuario()
    elif opcao == '6':
        deletar_usuario()
    elif opcao == '7':
        print("Saindo!")
        break
    else:
        print("Opção inválida. Tente novamente.")