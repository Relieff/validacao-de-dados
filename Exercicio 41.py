from datetime import date, datetime
nome = (input('Olá, por favor digite seu nome: '))
ano = int(input('Por favor, digite sua data de nascimento: '))
data = date.today().year
nasc = data - ano

if nasc <= 9:
    print('Voce tem {} anos'.format(nasc))
    print('Olá novamente {}, você está classificado para a categria mirim'.format(nome))
elif nasc > 9 and  nasc <= 14:
    print('Voce tem {} anos'.format(nasc))
    print('Olá novamente {}, você está classificado para a categria infantil'.format(nome))
elif nasc > 14 and nasc <= 19:
    print('Voce tem {} anos'.format(nasc))
    print('Olá novamente {}, você está classificado para a categria junior'.format(nome))
elif nasc > 19 and nasc <= 20:
    print('Voce tem {} anos'.format(nasc))
    print('Olá novamente {}, você está classificado para a categria senior'.format(nome))
else:
    print('Voce tem {} anos'.format(nasc))
    print('Olá novamente {}, você está classificado para a categria master'.format(nome))