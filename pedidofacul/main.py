
nome = str(input('Como você se chama?'))
print('Olá {}.Seja bem-vindo(a) a nossa loja de sorvetes!'.format(nome))



#acumulador dos valores
valor_total = 0

#código principal
while True:
    #enquanto o usuário não digitar o sabor exigido,o loop continua
    sabor = str(input('Qual sabor você deseja?(AC)-Açaí ou (CP)-Capuaçu:'))
    if sabor not in ['AC', 'CP']:
        print('Sabor,inválido.Tente novamente!')
        continue
    tamanho = str(input('Qual tamanho você deseja?(P),(M) ou (G):'))
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido.Tente novamente!')
        continue
   #se o usuario escolher os sabores certos,o pedido segue.
    if sabor == 'AC':
        if tamanho == 'P':
            valor_total += 11.00
            print('Você pediu um Açãí no tamanho P: R$11.00')
        elif tamanho == 'M':
            valor_total += 16.00
            print('Você pediu um Açãí no tamanho M: R$16.00')
        elif tamanho == 'G':
            valor_total += 20.00
            print('Você pediu um Açãí no tamanho G: R$20.00')
    elif sabor == "CP":
        if tamanho == 'P':
            valor_total += 9.00
            print('Você pediu um Capuaçu no tamanho P: R$9.00')
        elif tamanho == 'M':
            valor_total += 14.00
            print('Você pediu um Capuaçu no tamanho M: R$14.00')
        elif tamanho == 'G':
            valor_total += 18.00
            print('Você pediu um Capuaçu no tamanho G: R$18.00')

    pedir_mais = str(input('Deseja pedir mais alguma coisa?(S)-Sim (N)Não:'))
    if pedir_mais != 'S':
        break

print('Pedido finalizado!')
print('Total do pedido:R${}'.format(valor_total))











