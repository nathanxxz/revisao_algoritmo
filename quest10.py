notificacao = {
    'remetente': 'Gojo',
    'destinatario': 'Toji',
    'mensagem': 'Voce é fraco',
    'status': 'Ignorado'
}


def marcar_como_lida(notificacao: dict):
    notificacao['status'] = 'Lida'
    print('Notificação marcada como lida.')
    print(notificacao)

marcar_como_lida(notificacao)