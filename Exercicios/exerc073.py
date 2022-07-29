# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Palmeiras.

times = ('Palmeiras', 'Corinthias', 'Fluminense', 'Atlético Mineiro', 'Atlético-PR', 'Flamengo',
         'Internacional', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Ceará', 'Coritiba',
         'Goiás', 'América-MG', 'Avaí', 'Cuiabá', 'Atlético Goianiense', 'Juventude', 'Fortaleza')

print(f'Os 5 primeiros times: {times[0:5]}')
print(f'Os últimos 4 colocados: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'Palmeiras está na {times.index("Palmeiras")+1}º posição.')
