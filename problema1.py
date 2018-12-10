import funcoes

# definição do modelo da urna
urna = funcoes.cross('W', '12345678') | funcoes.cross('B', '123456') | funcoes.cross('R', '123456789')

# possibilidades de resultados/escolhas com 6 bolas
U6 = funcoes.combos(urna , 6)


red6 = {s for s in U6 if s.count('R') == 6}

result = funcoes.ProbDist(sexo_f=1, sexo_m=1)

print(result)
DK = funcoes.ProbDist(GG=121801, GB=126840, BG=127123, BB=135138)
print(DK)

def primeiro_menina(r): return r[0] == 'G'
def primeiro_menino(r): return r[0] == 'B'
def segundo_menina(r): return r[1] == 'G'
def segundo_menino(r): return r[1] == 'B'
def duas_meninas(r): return r == 'GG'
def dois_meninos(r): return r == 'BB'

print(funcoes.P(segundo_menina,funcoes.tal_que(primeiro_menina, DK)))
print(funcoes.P(segundo_menina,funcoes.tal_que(primeiro_menino, DK)))

def sexo_m(r):return 'Sexo_M' in r
def sexo_f(r):return 'Sexo_F' in r


PDSexo = funcoes.ProbDist(
Sexo_M=31,
Sexo_F=52
)
print("A probabilidade é:",funcoes.P(sexo_m , PDSexo))
