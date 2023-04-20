import json

estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []

def main():
    while True:
        print("Menu Principal")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")
        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == "1":
            print("Você escolheu a opção Estudantes.")
            menu_operacoes_estudantes()
        elif opcao_principal == "2":
            print("Você escolheu a opção Disciplinas.")
            menu_operacoes_disciplinas()
        elif opcao_principal == "3":
            print("Você escolheu a opção Professores.")
            menu_operacoes_professores()
        elif opcao_principal == "4":
            print("Você escolheu a opção Turmas.")
            menu_operacoes_turmas()
        elif opcao_principal == "5":
            print("Você escolheu a opção Matrículas.")
            menu_operacoes_matriculas()
        elif opcao_principal == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_operacoes_estudantes():
    while True:
        print("\nMenu de Operações - Estudantes")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao_operacoes = input("\nEscolha uma opção: ")

        if opcao_operacoes == "1":
            incluir_estudante()
        elif opcao_operacoes == "2":
            listar_estudantes()
        elif opcao_operacoes == "3":
            atualizar_estudante()
        elif opcao_operacoes == "4":
            excluir_estudante()
        elif opcao_operacoes == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


def incluir_estudante():
    codigo = int(input("\nDigite o código do estudante: "))
    nome = input("\nDigite o nome do estudante: ")
    cpf = input("\nDigite o CPF do estudante: ")
    estudantes = recuperar_estudantes()
    estudantes.append({"codigo": codigo, "nome": nome, "cpf": cpf})
    salvar_estudantes(estudantes)
    print(f"Estudante {nome} incluído com sucesso!")


def listar_estudantes():
    estudantes = recuperar_estudantes()
    if len(estudantes) == 0:
        print("\nNão há estudantes cadastrados.")
    else:
        print("\nEstudantes cadastrados:")
        for estudante in estudantes:
            print(f"- Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")


def atualizar_estudante():
    codigo = int(input("\nDigite o código do estudante que deseja atualizar: "))
    estudantes = recuperar_estudantes()
    for estudante in estudantes:
        if estudante["codigo"] == codigo:
            novo_codigo = int(input("\nDigite o novo código do estudante: "))
            novo_nome = input("\nDigite o novo nome do estudante: ")
            novo_cpf = input("\nDigite o novo CPF do estudante: ")
            estudante["codigo"] = novo_codigo
            estudante["nome"] = novo_nome
            estudante["cpf"] = novo_cpf
            salvar_estudantes(estudantes)
            print(f"Estudante {codigo} atualizado com sucesso!")
            return
    print(f"Estudante com código {codigo} não encontrado.")




def excluir_estudante():
    codigo = int(input("\nDigite o código do estudante que deseja excluir: "))
    estudantes = recuperar_estudantes()
    for i, estudante in enumerate(estudantes):
        if estudante["codigo"] == codigo:
            del estudantes[i]
            salvar_estudantes(estudantes)
            print(f"Estudante {codigo} excluído com sucesso!")
            return
    print(f"Estudante com código {codigo} não encontrado.")


def salvar_estudantes(estudantes):
    with open('estudantes.json', 'w') as f:
        json.dump(estudantes, f)


def recuperar_estudantes():
    try:
        with open('estudantes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def menu_operacoes_professores():
    while True:
        print("\nMenu de Operações - Professores")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao_operacoes = input("\nEscolha uma opção: ")

        if opcao_operacoes == "1":
            incluir_professor()
        elif opcao_operacoes == "2":
            listar_professores()
        elif opcao_operacoes == "3":
            atualizar_professor()
        elif opcao_operacoes == "4":
            excluir_professor()
        elif opcao_operacoes == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


def incluir_professor():
    codigo = int(input("\nDigite o código do professor: "))
    nome = input("\nDigite o nome do professor: ")
    cpf = input("\nDigite o CPF do professor: ")
    professores = recuperar_professores()
    professores.append({"codigo": codigo, "nome": nome, "cpf": cpf})
    salvar_professores(professores)
    print(f"Professor {nome} incluído com sucesso!")


def listar_professores():
    professores = recuperar_professores()
    if len(professores) == 0:
        print("\nNão há professores cadastrados.")
    else:
        print("\nProfessores cadastrados:")
        for professor in professores:
            print(f"- Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")


def atualizar_professor():
    codigo = int(input("\nDigite o código do professor que deseja atualizar: "))
    professores = recuperar_professores()
    for professor in professores:
        if professor["codigo"] == codigo:
            novo_codigo = int(input("\nDigite o novo código do professor: "))
            novo_nome = input("\nDigite o novo nome do professor: ")
            novo_cpf = input("\nDigite o novo CPF do professor: ")
            professor["codigo"] = novo_codigo
            professor["nome"] = novo_nome
            professor["cpf"] = novo_cpf
            salvar_professores(professores)
            print(f"Professor {codigo} atualizado com sucesso!")
            return
    print(f"Professor com código {codigo} não encontrado.")


def excluir_professor():
    codigo = int(input("\nDigite o código do professor que deseja excluir: "))
    professores = recuperar_professores()
    for i, professor in enumerate(professores):
        if professor["codigo"] == codigo:
            del professores[i]
            salvar_professores(professores)
            print(f"Professor {codigo} excluído com sucesso!")
            return
    print(f"Professor com código {codigo} não encontrado.")


def salvar_professores(professores):
    with open('professores.json', 'w') as f:
        json.dump(professores, f)


def recuperar_professores():
    try:
        with open('professores.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []



def menu_operacoes_disciplinas():
    while True:
        print("\nMenu de Operações - Disciplinas")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao_operacoes = input("\nEscolha uma opção: ")

        if opcao_operacoes == "1":
            incluir_disciplina()
        elif opcao_operacoes == "2":
            listar_disciplinas()
        elif opcao_operacoes == "3":
            atualizar_disciplina()
        elif opcao_operacoes == "4":
            excluir_disciplina()
        elif opcao_operacoes == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


def incluir_disciplina():
    codigo = int(input("\nDigite o código da disciplina: "))
    nome = input("\nDigite o nome da disciplina: ")
    disciplinas = recuperar_disciplinas()
    disciplinas.append({"codigo": codigo, "nome": nome})
    salvar_disciplinas(disciplinas)
    print(f"Disciplina {nome} incluída com sucesso!")


def listar_disciplinas():
    disciplinas = recuperar_disciplinas()
    if len(disciplinas) == 0:
        print("\nNão há disciplinas cadastradas.")
    else:
        print("\nDisciplinas cadastradas:")
        for disciplina in disciplinas:
            print(f"- Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")


def atualizar_disciplina():
    codigo = int(input("\nDigite o código da disciplina que deseja atualizar: "))
    disciplinas = recuperar_disciplinas()
    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo:
            novo_codigo = int(input("\nDigite o novo código da disciplina: "))
            novo_nome = input("\nDigite o novo nome da disciplina: ")
            disciplina["codigo"] = novo_codigo
            disciplina["nome"] = novo_nome
            salvar_disciplinas(disciplinas)
            print(f"Disciplina {codigo} atualizada com sucesso!")
            return
    print(f"Disciplina com código {codigo} não encontrada.")


def excluir_disciplina():
    codigo = int(input("\nDigite o código da disciplina que deseja excluir: "))
    disciplinas = recuperar_disciplinas()
    for i, disciplina in enumerate(disciplinas):
        if disciplina["codigo"] == codigo:
            del disciplinas[i]
            salvar_disciplinas(disciplinas)
            print(f"Disciplina {codigo} excluída com sucesso!")
            return
    print(f"Disciplina com código {codigo} não encontrada.")


def salvar_disciplinas(disciplinas):
    with open('disciplinas.json', 'w') as f:
        json.dump(disciplinas, f)


def recuperar_disciplinas():
    try:
        with open('disciplinas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def menu_operacoes_turmas():
    while True:
        print("\nMenu de Operações - Turmas")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao_operacoes = input("\nEscolha uma opção: ")

        if opcao_operacoes == "1":
            incluir_turma()
        elif opcao_operacoes == "2":
            listar_turmas()
        elif opcao_operacoes == "3":
            atualizar_turma()
        elif opcao_operacoes == "4":
            excluir_turma()
        elif opcao_operacoes == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")



def incluir_turma():
    codigo = int(input("\nDigite o código da turma: "))
    codigo_professor = int(input("\nDigite o código do professor: "))
    codigo_disciplina = int(input("\nDigite o código da disciplina: "))
    
    professores = recuperar_professores()
    if not any(professor["codigo"] == codigo_professor for professor in professores):
        print(f"Professor com código {codigo_professor} não encontrado.")
        return

    disciplinas = recuperar_disciplinas()
    if not any(disciplina["codigo"] == codigo_disciplina for disciplina in disciplinas):
        print(f"Disciplina com código {codigo_disciplina} não encontrada.")
        return

    turmas = recuperar_turmas()
    turmas.append({"codigo": codigo, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina})
    salvar_turmas(turmas)
    print(f"Turma {codigo} incluída com sucesso!")


def listar_turmas():
    turmas = recuperar_turmas()
    if len(turmas) == 0:
        print("\nNão há turmas cadastradas.")
    else:
        print("\nTurmas cadastradas:")
        for turma in turmas:
            print(f"- Código: {turma['codigo']}, Código do Professor: {turma['codigo_professor']}, Código da Disciplina: {turma['codigo_disciplina']}")


def atualizar_turma():
    codigo = int(input("\nDigite o código da turma que deseja atualizar: "))
    turmas = recuperar_turmas()
    for turma in turmas:
        if turma["codigo"] == codigo:
            novo_codigo = int(input("\nDigite o novo código da turma: "))
            novo_codigo_professor = int(input("\nDigite o novo código do professor: "))
            novo_codigo_disciplina = int(input("\nDigite o novo código da disciplina: "))

            professores = recuperar_professores()
            if not any(professor["codigo"] == novo_codigo_professor for professor in professores):
                print(f"Professor com código {novo_codigo_professor} não encontrado.")
                return

            disciplinas = recuperar_disciplinas()
            if not any(disciplina["codigo"] == novo_codigo_disciplina for disciplina in disciplinas):
                print(f"Disciplina com código {novo_codigo_disciplina} não encontrada.")
                return

            turma["codigo"] = novo_codigo
            turma["codigo_professor"] = novo_codigo_professor
            turma["codigo_disciplina"] = novo_codigo_disciplina
            salvar_turmas(turmas)
            print(f"Turma {codigo} atualizada com sucesso!")
            return
    print(f"Turma com código {codigo} não encontrada.")


def excluir_turma():
    codigo = int(input("\nDigite o código da turma que deseja excluir: "))
    turmas = recuperar_turmas()
    for i, turma in enumerate(turmas):
        if turma["codigo"] == codigo:
            del turmas[i]
            salvar_turmas(turmas)
            print(f"Turma {codigo} excluída com sucesso!")
            return
    print(f"Turma com código {codigo} não encontrada.")


def salvar_turmas(turmas):
    with open('turmas.json', 'w') as f:
        json.dump(turmas, f)


def recuperar_turmas():
    try:
        with open('turmas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []



def menu_operacoes_matriculas():
    while True:
        print("\nMenu de Operações - Matrículas")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao_operacoes = input("\nEscolha uma opção: ")

        if opcao_operacoes == "1":
            incluir_matricula()
        elif opcao_operacoes == "2":
            listar_matriculas()
        elif opcao_operacoes == "3":
            atualizar_matricula()
        elif opcao_operacoes == "4":
            excluir_matricula()
        elif opcao_operacoes == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


def incluir_matricula():
    codigo_turma = int(input("\nDigite o código da turma: "))
    codigo_estudante = int(input("\nDigite o código do estudante: "))

    turmas = recuperar_turmas()
    if not any(turma["codigo"] == codigo_turma for turma in turmas):
        print(f"Turma com código {codigo_turma} não encontrada.")
        return

    estudantes = recuperar_estudantes()
    if not any(estudante["codigo"] == codigo_estudante for estudante in estudantes):
        print(f"Estudante com código {codigo_estudante} não encontrado.")
        return

    matriculas = recuperar_matriculas()
    matriculas.append({"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante})
    salvar_matriculas(matriculas)
    print(f"Matrícula na turma {codigo_turma} incluída com sucesso!")


def listar_matriculas():
    matriculas = recuperar_matriculas()
    if len(matriculas) == 0:
        print("\nNão há matrículas cadastradas.")
    else:
        print("\nMatrículas cadastradas:")
        for matricula in matriculas:
            print(f"- Código da Turma: {matricula['codigo_turma']}, Código do Estudante: {matricula['codigo_estudante']}")


def atualizar_matricula():
    codigo_turma = int(input("\nDigite o código da turma da matrícula que deseja atualizar: "))
    codigo_estudante = int(input("\nDigite o código do estudante da matrícula que deseja atualizar: "))
    matriculas = recuperar_matriculas()
    for matricula in matriculas:
        if matricula["codigo_turma"] == codigo_turma and matricula["codigo_estudante"] == codigo_estudante:
            novo_codigo_turma = int(input("\nDigite o novo código da turma: "))
            novo_codigo_estudante = int(input("\nDigite o novo código do estudante: "))

            turmas = recuperar_turmas()
            if not any(turma["codigo"] == novo_codigo_turma for turma in turmas):
                print(f"Turma com código {novo_codigo_turma} não encontrada.")
                return

            estudantes = recuperar_estudantes()
            if not any(estudante["codigo"] == novo_codigo_estudante for estudante in estudantes):
                print(f"Estudante com código {novo_codigo_estudante} não encontrado.")
                return

            matricula["codigo_turma"] = novo_codigo_turma
            matricula["codigo_estudante"] = novo_codigo_estudante
            salvar_matriculas(matriculas)
            print(f"Matrícula na turma {codigo_turma} atualizada com sucesso!")
            return
    print(f"Matrícula na turma {codigo_turma} com estudante de código {codigo_estudante} não encontrada.")



def excluir_matricula():
    codigo_turma = int(input("\nDigite o código da turma da matrícula que deseja excluir: "))
    codigo_estudante = int(input("\nDigite o código do estudante da matrícula que deseja excluir: "))
    matriculas = recuperar_matriculas()
    for i, matricula in enumerate(matriculas):
        if matricula["codigo_turma"] == codigo_turma and matricula["codigo_estudante"] == codigo_estudante:
            del matriculas[i]
            salvar_matriculas(matriculas)
            print(f"Matrícula na turma {codigo_turma} excluída com sucesso!")
            return
    print(f"Matrícula na turma {codigo_turma} com estudante de código {codigo_estudante} não encontrada.")


def salvar_matriculas(matriculas):
    with open('matriculas.json', 'w') as f:
        json.dump(matriculas, f)


def recuperar_matriculas():
    try:
        with open('matriculas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    main()

