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

print("1. Probabilidade é de: %.1f%%" % (prob1_M * 100),
      ".Por tanto a possibilidade de que 1 dessas 72 pessoas ser homem é de 1.4%")

print("\n")

print("2. Dado que uma pessoa indique que sua formação acadêmica é Ensino Superior Incompleto qual a probabilidade de ela ter problemas com Criar\n referências, Fazer citações ou Numeração de páginas?")


def ensSupInc(r): return 'pessoasEnsiSupInc' in r

def dificuldades(r): return 'dificuldades' in r

pEsi = list(i.split(',')[0].count('Ensino Superior Incompleto') for i in espaco).count(1)

PDEnsiSupeInc = funcoes.ProbDist(
    restante=(len(espaco) - 1) - pEsi,
    pessoasEnsiSupInc=pEsi

)

fazerCitaNumPagCriaRef = list(i.split(',')[3].split(';').count('Fazer citações') or i.split(',')[3].split(';').count('Numeração de páginas') or i.split(',')[3].split(';').count('Criar referências') for i in espaco).count(1)



PDDificuldades = funcoes.ProbDist(
    restante=(len(espaco) - 1) - fazerCitaNumPagCriaRef,
    dificuldades=fazerCitaNumPagCriaRef
)

PDEnsiSupeIncDif = funcoes.joint(PDEnsiSupeInc, PDDificuldades)

probQt2 = funcoes.P(dificuldades, funcoes.tal_que(ensSupInc, PDEnsiSupeIncDif))

print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print('\n')

print("3. Dado que uma pessoa indique que utiliza o ambiente Word qual a probabilidade de que o problema na edição de trabalhos acadêmicos seja Criação de sumários?")


def utilizaWord(r): return 'usaWord' in r


def difcuSumario(r): return 'dificuSumario' in r


utW = list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)
difi = list(i.split(',')[3].split(';').count('Criação de sumários') for i in espaco).count(1)

PDUtilizaWord = funcoes.ProbDist(
    restante=(len(espaco) - 1) - utW,
    usaWord=list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)
)

PDDificuldades = funcoes.ProbDist(
    restante=(len(espaco) - 1) - difi,
    dificuSumario=difi
)

PEUtilizaWordDificuSumario = funcoes.joint(PDUtilizaWord, PDDificuldades)


probQt2 = funcoes.P(difcuSumario, funcoes.tal_que(utilizaWord, PEUtilizaWordDificuSumario))
print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print('\n')

print("4. Dado que uma pessoa indique que utiliza o ambiente Word e seu problema de edição de trabalhos acadêmicos seja Criação de sumários qual a probabilidade de que ela gostaria\n que uma ferramenta de edição fornecesse como ajuda a Criação automática de sumários?")


def utilizaWordDifcuSumario(r): return 'usaWordDificuSumari' in r

def criaSumAuto(r): return 'criaAutoSumario' in r


utWcriaSAuto = list(i.split(',')[2].split(';').count('Word') and i.split(',')[3].split(';').count('Criação de sumários') for i in espaco).count(1)

difi = list(i.split(',')[3].split(';').count('Criação de sumários') for i in espaco).count(1)

PDUtilizaWordECriaSum = funcoes.ProbDist(
    restante=(len(espaco) - 1)- utWcriaSAuto,
    usaWordDificuSumari=utWcriaSAuto,
)
PDCriaSum = funcoes.ProbDist(
    restante=(len(espaco) - 1) - difi,
    criaAutoSumario=difi
)

PEUtilizaWordDificuSumPDCriaSum = funcoes.joint(PDUtilizaWordECriaSum, PDCriaSum)

probQt2 = funcoes.P(utilizaWordDifcuSumario, funcoes.tal_que(criaSumAuto, PEUtilizaWordDificuSumPDCriaSum))
print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print('\n')

print("5. Dado que uma pessoa indique que sua formação acadêmica é Ensino Fundamental Completo qual a probabilidade de ela utilizar Google Docs ou Word como ambiente de edição de trabalhos?")


def ensiFundamental(r): return 'ensFunda' in r


def utlDocsWord(r): return 'docsOUword' in r


utWordOuDocs = list(i.split(',')[2].split(';').count('Word') or i.split(',')[2].split(';').count('Google Docs') for i in espaco).count(1)
pEsi = list(i.split(',')[0].count('Ensino Fundamental Completo') for i in espaco).count(1)

PDUtilizaWordOuDocs = funcoes.ProbDist(
    restante=(len(espaco) - 1) - utWordOuDocs,
    docsOUword=utWordOuDocs
)
PDEnsiFundaCom = funcoes.ProbDist(
    restante=(len(espaco) - 1) - pEsi,
    ensFunda=pEsi
)
PDEnsiFundaComPDUtilizaWordOuDocs = funcoes.joint(PDUtilizaWordOuDocs, PDEnsiFundaCom)

probQt2 = funcoes.P(ensiFundamental, funcoes.tal_que(utlDocsWord, PDEnsiFundaComPDUtilizaWordOuDocs))

print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print('\n')

print("6. Dado que uma pessoa indique que sua formação acadêmica é Ensino Superior Incompleto ou Ensino Superior Completo qual a probabilidade de ela não utilizar nem Google Docs e nem Word?")


def ensSupIncOUCompleto(r): return 'ensSupIncOUComp' in r


def nUtiDocsNemWord(r): return 'docsNemWord' in r


utWord = list(i.split(',')[2].split(';').count('Word') for i in espaco).count(0)
utDocs = list(i.split(',')[2].split(';').count('Google Docs') for i in espaco).count(0)

pEsiSupCom = list(i.split(',')[0].count('Ensino Superior Completo') for i in espaco).count(1)
pEsiSupInc = list(i.split(',')[0].count('Ensino Superior Incompleto') for i in espaco).count(1)

PDEnsiSupIncOUCom = funcoes.ProbDist(
    restante=(len(espaco) - 1) - max(pEsiSupCom, pEsiSupInc),
    ensSupIncOUComp=max(pEsiSupCom, pEsiSupInc)
)
PDNaoUtWordNemDocs = funcoes.ProbDist(
    restante=(len(espaco) - 1) - max(utDocs, utWord),
    docsNemWord=max(utDocs, utWord)
)

PDEnsiSupIncOUComPDNaoUtWordNemDocs = funcoes.joint(PDEnsiSupIncOUCom, PDNaoUtWordNemDocs)


probQt2 = funcoes.P(nUtiDocsNemWord, funcoes.tal_que(ensSupIncOUCompleto, PDEnsiSupIncOUComPDNaoUtWordNemDocs))
print("Probabilidade é de: %.1f%%" % (probQt2 * 100))

print("7. Dado que uma pessoa indique que utilize o ambiente Word qual os dois problemas com maiores probabilidades -- e quais seriam elas?")

utWord = list(i.split(',')[2].split(';').count('Word') for i in espaco).count(1)

difSum = list(i.split(',')[3].split(';').count('Criação de sumários') for i in espaco).count(1)
difLisFig = list(i.split(',')[3].split(';').count('Criação de lista de figuras') for i in espaco).count(1)
difNumPag = list(i.split(',')[3].split(';').count('Numeração de páginas') for i in espaco).count(1)
difEspTexto = list(i.split(',')[3].split(';').count('Espaçamento do texto') for i in espaco).count(1)
difAlinTex = list(i.split(',')[3].split(';').count('Alinhamento do texto') for i in espaco).count(1)
dif = list(i.split(',')[3].split(';').count('Criar referências') for i in espaco).count(1)
difNumPag = list(i.split(',')[3].split(';').count('Fazer citações') for i in espaco).count(1)
difNumPag = list(i.split(',')[3].split(';').count('Criar tabelas') for i in espaco).count(1)
difNumPag = list(i.split(',')[3].split(';').count('Não compreender a ferramenta') for i in espaco).count(1)

print(dif)