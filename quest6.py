conta_bancaria = {
    'nome_titular': 'Eren',
    'numero_conta': '66666',
    'saldo': 1500
}


def depositar(conta: dict, valor: float):
    if(valor > 0):
        conta['saldo'] += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')
    else:
        print('Valor de depósito inválido. O valor deve ser maior que zero.')


def sacar(conta: dict, valor: float) -> bool:
    if(valor > 0):
        if(conta['saldo'] >= valor):
            conta['saldo'] -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
            return True
        else:
            print(f'Saldo insuficiente para realizar o saque de R$:{valor}.')
            return False
    else:
        print('Valor de saque inválido. O valor deve ser maior que zero')
        return False


print(f'Saldo inicial: {conta_bancaria['saldo']}')

depositar(conta_bancaria, 500.00)
print('Saldo após depósito:', conta_bancaria['saldo'])

sucesso_saque = sacar(conta_bancaria, 300.00)
print('Saldo após saque:', conta_bancaria['saldo'])

sucesso_saque = sacar(conta_bancaria, 2000.00)
print('Saldo após tentativa de saque:', conta_bancaria['saldo'])