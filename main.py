import sqlite3
from datetime import datetime
import requests

URL = 'https://api.hgbrasil.com/finance?key=02c3ebfb'
resposta = requests.get(URL)
dolar = float(resposta.json()['results']['currencies']['USD']['buy'])
euro = float(resposta.json()['results']['currencies']['EUR']['buy'])


data_hora = str(datetime.now())

today = datetime.today().strftime('%Y-%m-%d')

con = sqlite3.connect("data/cotacoes.db")
cur = con.cursor()
data = (dolar, euro, data_hora)
data_banco = cur.execute("SELECT dataHora FROM cotacao").fetchone()
date = data_banco[0].split(' ')[0]

if today != date:
    cur.execute("INSERT INTO cotacao VALUES(?, ?, ?, null)", data)
    con.commit()
dolar_banco = cur.execute("SELECT dolar FROM cotacao").fetchone()
dolar_banco_float = float('.'.join(str(elem) for elem in dolar_banco))
euro_banco = cur.execute("SELECT euro FROM cotacao").fetchone()
dolar_euro_float = float('.'.join(str(elem) for elem in dolar_banco))
real = float(input('Digite um valor em real:'))
usd_dolar = float(real / dolar_banco_float)
eur_euro = float(real / dolar_euro_float)
print(f'Dolar: {usd_dolar:.2f} \n Euro: {eur_euro:.2f}')

