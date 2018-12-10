import funcoes
from fractions import Fraction

arq = open('TrabalhosAcadêmicos.csv', 'r', encoding="utf-8")
espaco = arq.readlines()
"""
R1: Considerando o espaço amostral de 72 pessoas e que 1 dessas tem de ser do 
sexo masculino, fazemos a divisão de 1 para 72, o que resulta em 0.14 ou 14%.
"""
evento = {'sexo_m'}

prob1_M = float(Fraction(len(evento), len(espaco) - 1))

print("Probabilidade é de: %.1f%%" % (prob1_M * 100),
      ".Por tanto a possibilidade de que 1 dessas 72 pessoas ser homem é de 1.4%")

print("\n")

print(
    "Dado que uma pessoa indique que sua formação acadêmica é Ensino Superior Incompleto qual a probabilidade de ela ter problemas com Criar\n referências, Fazer citações ou Numeração de páginas?")


def ensSupInc(r): return 'pessoasEnsiSupInc' in r


def dificuldades(r): return 'dificuldades' in r

pEsi = list(i.split(',')[0].count('Ensino Superior Incompleto') for i in espaco).count(1)

PDEnsiSupeInc = funcoes.ProbDist(
    restante=(len(espaco) - 1)-pEsi,
    pessoasEnsiSupInc=pEsi

)

fazerCita = list(i.split(',')[3].split(';').count('Fazer citações') for i in espaco).count(1)
numPag = list(i.split(',')[3].split(';').count('Fazer citações') for i in espaco).count(1)
criarRef = list(i.split(',')[3].split(';').count('Fazer citações') for i in espaco).count(1)

difi = max(fazerCita, numPag, criarRef)
PDDificuldades = funcoes.ProbDist(
    restante=(len(espaco) - 1)-difi,
    dificuldades=difi
)

PDEnsiSupeIncDif = funcoes.joint(PDEnsiSupeInc, PDDificuldades)

PA = funcoes.P(ensSupInc, PDEnsiSupeIncDif)

PE = funcoes.P(dificuldades, PDEnsiSupeIncDif)

probQt2 = PA * PE / PE
print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print('\n')

print("3. Dado que uma pessoa indique que utiliza o ambiente Word qual a probabilidade de que o problema na edição de trabalhos acadêmicos seja Criação de sumários?")


def utilizaWord(r): return 'usaWord' in r


def difcuSumario(r): return 'dificuSumario' in r

utW = list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)

PDUtilizaWord = funcoes.ProbDist(
    restante=(len(espaco) - 1)-utW,
    usaWord=list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)

)

difi = list(i.split(',')[3].split(';').count('Criação de sumários') for i in espaco).count(1)


PDDificuldades = funcoes.ProbDist(
    restante=(len(espaco) - 1) - difi,
    dificuSumario=difi
)



PEUtilizaWordDificuSumario = funcoes.joint(PDUtilizaWord, PDDificuldades)


PA = funcoes.P(utilizaWord, PEUtilizaWordDificuSumario)

PE = funcoes.P(difcuSumario, PEUtilizaWordDificuSumario)

probQt2 = PA * PE / PE
print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print('\n')
print("4. Dado que uma pessoa indique que utiliza o ambiente Word e seu problema de edição de trabalhos acadêmicos seja Criação de sumários qual a probabilidade de que ela gostaria\n que uma ferramenta de edição fornecesse como ajuda a Criação automática de sumários?")


def utilizaWord(r): return 'usaWord' in r


def difcuSumario(r): return 'dificuSumario' in r

def criaSumAuto(r): return 'criaSumarioAuto' in r


utW = list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)

cSAuto = list(i.split(',')[4].split(';').count('Criação automática de sumários') for i in espaco).count(1)

difi = list(i.split(',')[3].split(';').count('Criação de sumários') for i in espaco).count(1)

PDUtilizaWord = funcoes.ProbDist(
    restante=(len(espaco) - 1)-utW,
    usaWord=list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)

)

PDDificuldades = funcoes.ProbDist(
    restante=(len(espaco) - 1) - difi,
    dificuSumario=difi
)



PEUtilizaWordDificuSumario = funcoes.joint(PDUtilizaWord, PDDificuldades)


PA = funcoes.P(utilizaWord, PEUtilizaWordDificuSumario)

PE = funcoes.P(difcuSumario, PEUtilizaWordDificuSumario)

probQt2 = PA * PE / PE
print("Probabilidade é de: %.1f%%" % (probQt2 * 100))