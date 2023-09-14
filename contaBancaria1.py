# Função para criar uma conta
def cria_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite,
        'tipo_conta': 'corrente'  # Você pode definir o tipo de conta aqui, por exemplo.
    }
    return conta

# Função para depositar dinheiro na conta
def deposita(conta, valor):
    conta['saldo'] += valor

# Função para sacar dinheiro da conta
def saca(conta, tipo_conta, valor):
    if tipo_conta == 'corrente':
        conta['saldo'] -= valor
    elif tipo_conta == 'poupanca':
        # Implemente a lógica para sacar da poupança aqui, se necessário
        pass
    else:
        print("Tipo de conta inválido")

# Função para imprimir o extrato da conta
def extrato(conta):
    print(f"Número da conta: {conta['numero']}")
    print(f"Saldo da conta: R${conta['saldo']:.2f}")

# Exemplo de uso das funções
minha_conta = cria_conta('12345', 'João', 1000.0, 2000.0)
extrato(minha_conta)

deposita(minha_conta, 500.0)
extrato(minha_conta)

saca(minha_conta, 'corrente', 200.0)
extrato(minha_conta)
