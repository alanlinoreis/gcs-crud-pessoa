# sistema.py
# CRUD de Pessoa em memória — Atividade GCS

pessoas = []
proximo_id = 1


def cadastrar():
    global proximo_id
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    pessoa = {"id": proximo_id, "nome": nome, "cpf": cpf, "telefone": telefone}
    pessoas.append(pessoa)
    proximo_id += 1
    print(f"\n✓ Pessoa cadastrada com ID {pessoa['id']}.")


def listar():
    if not pessoas:
        print("\nNenhuma pessoa cadastrada.")
        return
    print(f"\n{'ID':<5} {'Nome':<25} {'CPF':<15} {'Telefone':<15}")
    print("-" * 62)
    for p in pessoas:
        print(f"{p['id']:<5} {p['nome']:<25} {p['cpf']:<15} {p['telefone']:<15}")


def buscar():
    termo = input("Digite o nome ou CPF: ").strip().lower()
    resultados = [p for p in pessoas if termo in p["nome"].lower() or termo in p["cpf"]]
    if not resultados:
        print("\nNenhum resultado encontrado.")
        return
    for p in resultados:
        print(f"\nID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Telefone: {p['telefone']}")


def atualizar():
    try:
        id_ = int(input("ID da pessoa a atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for p in pessoas:
        if p["id"] == id_:
            print(f"Editando: {p['nome']} — deixe em branco para manter.")
            novo_nome = input(f"Novo nome [{p['nome']}]: ").strip()
            novo_cpf = input(f"Novo CPF [{p['cpf']}]: ").strip()
            novo_tel = input(f"Novo telefone [{p['telefone']}]: ").strip()
            if novo_nome: p["nome"] = novo_nome
            if novo_cpf: p["cpf"] = novo_cpf
            if novo_tel: p["telefone"] = novo_tel
            print("\n✓ Dados atualizados.")
            return
    print("Pessoa não encontrada.")


def remover():
    try:
        id_ = int(input("ID da pessoa a remover: "))
    except ValueError:
        print("ID inválido.")
        return
    for i, p in enumerate(pessoas):
        if p["id"] == id_:
            confirma = input(f"Confirmar remoção de '{p['nome']}'? (s/N): ").strip().lower()
            if confirma == "s":
                pessoas.pop(i)
                print("\n✓ Pessoa removida.")
            else:
                print("Operação cancelada.")
            return
    print("Pessoa não encontrada.")


def menu():
    opcoes = {
        "1": ("Cadastrar pessoa",  cadastrar),
        "2": ("Listar pessoas",    listar),
        "3": ("Buscar pessoa",     buscar),
        "4": ("Atualizar pessoa",  atualizar),
        "5": ("Remover pessoa",    remover),
    }
    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE CADASTRO DE PESSOAS")
        print("=" * 40)
        for k, (desc, _) in opcoes.items():
            print(f"  [{k}] {desc}")
        print("  [0] Encerrar sistema")
        print("-" * 40)
        opc = input("  Opção: ").strip()
        if opc == "0":
            print("\nSistema encerrado.")
            break
        elif opc in opcoes:
            opcoes[opc][1]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()