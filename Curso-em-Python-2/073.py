times = ('Flamengo','Palmeiras','Cruzeiro','Mirassol','Botafogo','Fluminense','Bahia','São Paulo','Corinthians','Grêmio','Vasco','Bragantino','Atlético-MG','Ceará','Vitória','Santos','Internacional','Fortaleza','Juventude','Sport')
print(times)
print(f'{times[0:6]}')
print(f'{times[16]}, {times[17]}, {times[18]}, {times[19]}')
times_ordenados = tuple(sorted(times))
print(times_ordenados)
print(f' O Maior time do do mundo esta na posição {times.index("Flamengo")+1} da tabela' )







