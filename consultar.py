import pymssql

server = 'dns_do_server'
username = 'user'
password = 'password'

opcao = input("Onde deseja realizar a consulta? Digite X ou Y: ")

if opcao.upper() == 'X':
    database = 'bdX'
    tabela = 'tableX'
elif opcao.upper() == 'Y':
    database = 'bdY'
    tabela = 'tableY'
else:
    print("Opção inválida.")
    exit()

conn = pymssql.connect(server=server, database=database, user=username, password=password)

cursor = conn.cursor()

numBordero = input("Digite o número do bordero: ")

consulta = f"""
SELECT DISTINCT sc.codigo, sc.nome
FROM cadastro sc
JOIN {tabela} sf ON sc.codigo = sf.sacado
WHERE sf.bordero = '{numBordero}'
  AND (sc.fone IS NULL OR sc.fone = '')
  AND (sc.celular IS NULL OR sc.celular = '')
"""

cursor.execute(consulta)

rows = cursor.fetchall()

nome_arquivo = 'relatorio.txt'
with open(nome_arquivo, 'w') as arquivo:
    for row in rows:
        linha = ' | '.join(str(col) for col in row)
        arquivo.write(linha + '\n')

cursor.close()
conn.close()

print('\n\n')

import time

def loading_bar():
    while True:
        for i in range(1, 51):
            print(f"\rCarregando... {i * 2}% [{'|' * i + ' ' * (50 - i)}]", end='')
            time.sleep(0.01) 
        break

loading_bar()


input("\n\n\n\nPressione Enter para sair...")
