'''Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input('Didite um número: '))
n2 = float(input('Didite um número: '))
if n1 > n2:
    print(f'{n1} é o número maior!')
else:
    print(f'{n2} é o número maior!')'''

'''2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('Digite um valor: '))
if valor > 0:
    print(f'O {valor} é positivo')
else:
    print(f'O {valor} é negativo')'''

'''3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -
Masculino, Sexo Inválido.
letra = input('Digite uma letra F ou M e descubra o que significa: ')
if letra == 'M':
    print(f'A letra {letra} é masculino')
elif letra == 'm':
    print(f'A letra {letra} é masculino')
elif letra == 'F':
    print(f'A letra {letra} é feminino')
elif letra == 'f':
    print(f'A letra {letra} é feminino')
else:
    print('Que pena!!!\nLetra não reconhecida, por favor digite outra letra!')'''

'''4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite qualquer letra e descubra se é vogal ou consoante: ')
if letra == 'a':
    print(f'A letra "{letra}" é vogal')
elif letra == 'A':
    print(f'A letra "{letra}" é vogal')
elif letra == 'e':
    print(f'A letra "{letra}" é vogal')
elif letra == 'E':
    print(f'A letra "{letra}" é vogal')
elif letra == 'i':
    print(f'A letra "{letra}" é vogal')
elif letra == 'I':
    print(f'A letra "{letra}" é vogal')
elif letra == 'o':
    print(f'A letra "{letra}" é vogal')
elif letra == 'O':
    print(f'A letra "{letra}" é vogal')
elif letra == 'u':
    print(f'A letra "{letra}" é vogal')
elif letra == 'U':
    print(f'A letra "{letra}" é vogal')
else:
    print(f'A letra "{letra}" não é vogal é consoante"')'''

'''5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
media = (nota1 + nota2) / 2
if media == 10:
    print('Aprovado com Distição')
elif media >= 7:
    print('Parabéns você foi aprovado')
else:
    print('Foi reprovado, você vai ter que estudar mais!')'''

'''6. Faça um Programa que leia três números e mostre o maior deles.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if (n1 > n2) and (n1 > n3):
    print(f'{n1} é o maior número')
elif (n1 >= n2) and (n1 >= n3):
    print(f'{n1} é o maior número')
elif (n2 > n1) and (n2 > n3):
    print(f'{n2} é o maior número')
elif (n2 >= n1) and (n2 >= n3):
    print(f'{n2} é o maior número')
elif (n3 > n1) and (n3 > n2):
    print(f'{n3} é o maior número')
elif (n3 >= n1) and (n3 >= n2):
    print(f'{n3} é o maior número')'''

'''8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
preco1 = float(input('Digite o preço do produto: '))
preco2 = float(input('Digite o preço do produto: '))
preco3 = float(input('Digite o preço do produto: '))
if (preco1 < preco2) and (preco1 < preco3):
    print(f'O produto menor preço é {preco1:.2f}')
elif (preco2 < preco3) and (preco2 < preco1):
    print(f'O produto menor preço é {preco2:.2f}')
elif (preco3 < preco1) and (preco3 < preco2):
    print(f'O produto menor preço é {preco3:.2f}')'''




'''9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))
if (n1 > n2):
    if(n2 > n3):
        print(f'{n1}, {n2} e {n3}')
if (n1 > n3):
    if (n3 > n2):
        print(f'{n1}, {n3} e {n2}')
if (n2 > n1):
    if (n1 > n3):
        print(f'{n2}, {n1} e {n3}')
if (n2 > n3):
    if(n3 > n1):
        print(f'{n2}, {n3} e {n1}')
if (n3 > n1):
    if(n1 > n2) :
        print(f'{n3}, {n1} e {n2}')
if (n3 > n2):
    if(n2 > n1):
        print(f'{n3}, {n2} e {n1}'''

'''10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('M-matutino ou V-Vespertino ou N- Noturno')
turno = input('Em qual turno você estuda? ')
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')'''


'''11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

salario_atual = float(input('Digite o seu sálario atual: '))
if salario_atual <= 280:
    per = '20%'
    aumento = salario_atual * 1.20
    VA = aumento - salario_atual
elif salario_atual <= 700 and salario_atual > 280:
    per = '15%'
    aumento = salario_atual * 1.15
    VA = aumento - salario_atual
elif salario_atual <= 1500 and salario_atual > 700:
    per = '10%'
    aumento = salario_atual * 1.10
    VA = aumento - salario_atual
elif salario_atual > 1500:
    per = '5%'
    aumento = salario_atual * 1.05
    VA = aumento - salario_atual
print()
print(f'Salario antes do reajuste R$ {salario_atual:.2f}')
print(f'Percentual de aumento aplicado foi {per}')
print(f'O valor do aumento foi de R$ {VA:.2f}')
print(f'O novo salário, após o aumento é R$ {aumento:.2f}')'''

'''12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00

valor_da_hora = float(input('Digite o valor da hora R$ '))
quantidade_hora = float(input('Digite a quabtidade de horas trabalhada: '))
salario_bruto = valor_da_hora * quantidade_hora

if salario_bruto <= 900:
    print('Você é isentos de impostos')
elif salario_bruto <= 1500 and salario_bruto > 900:
    por = '5%'
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    td = ir + inss
    salario_liquido = salario_bruto - td
elif salario_bruto <= 2500 and salario_bruto > 1500:
    por = '10%'
    ir = salario_bruto * 0.1
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    td = ir + inss
    salario_liquido = salario_bruto - td
elif salario_bruto > 2500:
    por = '20%'
    ir = salario_bruto * 0.2
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    td = ir + inss
    salario_liquido = salario_bruto - td
print(f'Salário Bruto: {valor_da_hora:.0f} * {quantidade_hora:.0f}: R$ {salario_bruto:.2f}')
print(f'(-) IR ({por}) : R$ {ir:.2f}')
print(f'(-) INSS (10%) : R$ {inss:.2f}')
print(f'FGTS (11%) : R$ {fgts:.2f}')
print(f'Total de descontos : R$ {td:.2f}')
print(f'Salário Liquido : R$ {salario_liquido:.2f}')'''

'''13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido.
dia = int(input('Digite um numero: '))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sábado')
else:
    print('Valor Inválido')'''

'''14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digite a 2ª nota do aluno: '))
media = (nota1 + nota2)/2
if 9 <= media < 10:
     Conceito = "A"
     men = 'APROVADO'
     print(f'1ª nota do aluno: {nota1}\n2ª nota do aluno: {nota2}')
     print(f'a média é: {media}')
     print(f'O conceito correspondente: {Conceito}')
     print(f'Aluno {men}')
elif 7.5 <= media < 9:
    Conceito = "B"
    men = 'APROVADO'
    print(f'1ª nota do aluno: {nota1}\n2ª nota do aluno: {nota2}')
    print(f'a média é: {media}')
    print(f'O conceito correspondente: {Conceito}')
    print(f'Aluno {men}')
elif 6 <= media < 7.5:
    Conceito = "C"
    men = 'APROVADO'
    print(f'1ª nota do aluno: {nota1}\n2ª nota do aluno: {nota2}')
    print(f'a média é: {media}')
    print(f'O conceito correspondente: {Conceito}')
    print(f'Aluno {men}')
elif 4 <= media < 6:
    Conceito = "D"
    men = 'REPROVADO'
    print(f'1ª nota do aluno: {nota1}\n2ª nota do aluno: {nota2}')
    print(f'a média é: {media}')
    print(f'O conceito correspondente: {Conceito}')
    print(f'Aluno {men}')
elif 0 <= media < 4:
    Conceito = "E"
    men = 'REPROVADO'
    print(f'1ª nota do aluno: {nota1}\n2ª nota do aluno: {nota2}')
    print(f'a média é: {media}')
    print(f'O conceito correspondente: {Conceito}')
    print(f'Aluno {men}')
else:
    print('Valor inválido')'''

'''15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
lado1 = float(input('Digite o valor de um lado do triângulo: '))
lado2 = float(input('Digite o valor de um lado do triângulo: '))
lado3 = float(input('Digite o valor de um lado do triângulo: '))
if (lado1 == lado2 == lado3):
    print('Triângulo Equilátero')
elif (lado2 == lado3 and lado2 != lado1) or (lado3 == lado1 and lado3 != lado2) or (lado1 == lado2 and lado1 != lado3):
    print('Triângulo Isósceles')
elif (lado1 != lado2 != lado3):
    print('Triânculo Escaleno')'''

'''16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Digite o valor de a: '))
if a == 0:
    print('A equação não é do 2º grau')
else:
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))

delta = -b**2 * 4 * a * c

if(delta > 0):
    x1 = round(-b + delta ** (1/2)) / (2 * a)
    x2 = round(-b - delta ** (1/2)) / (2 * a)
    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')
elif (delta == 0):
    x1 = round(-b + delta ** (1/2)) / (2 * a)
    print(f'{x1}')
else:
    print('Não possuí raizes reais')'''

'''17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
não bissexto.
ano = int(input('Digite um ano para saber se é BISSEXTO: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')'''

'''18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dd = int(input('Didite o dia do mês: '))
mm = int(input('Didite o mês do ano: '))
aa = int(input('Didite um ano: '))

if (1 < dd <= 31 and 1 < mm <= 12 and aa > 0):
    print('A data é válida!')
else:
    print('Essa data não é valida')'''

'''19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e
16
n1 = int( input('Digite um número para saber a quantidade de centenas, dezenas e unidades: '))

if (n1 < 1000 and n1 > 0):
    centena = n1 // 100
    dezena = (n1 % 100) // 10
    unidade = n1 % 10

    if(centena > 1):
        print(f'{centena} centenas')
    else:
        print(f'{centena} centena')
    if (dezena > 1):
        print(f'{dezena} dezenas')
    else:
        print(f'{dezena} dezena')
    if (unidade > 1):
        print(f'{unidade} unidades')
    else:
        print(f'{unidade} unidade')
else:
    print('Número fora do intervalo!')'''


'''20. Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite uma nota: '))
nota3 = float(input('Digite uma nota: '))
media = (nota1 + nota2 + nota3) / 3

if (media == 10):
    print('Aprovado com Distinção!')
elif(media >= 7):
    print('Aprovado com a Respectiva média alcançada')
else:
    print('Reprovado com a respectiva média alcançada')'''

'''21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
de 10, uma nota de 5 e quatro notas de 1.

print('Notas disponíveis na maquina R$100, R$50, R$10, R$5 e R$1')
saque = int(input('Digite um valor que deseja: '))

if (saque < 10 or saque > 600):
    print('Valor utrapassou o limite')
else:
    nota100 = saque // 100
    saque = saque % 100

    nota50 = saque // 50
    saque = saque % 50

    nota10 = saque // 10
    saque = saque % 10

    nota5 = saque // 5
    saque = saque % 5

    nota1 = saque

    if (nota100 > 0):
        print(f'{nota100} nota(s) de 100 reais"')
    if (nota50 > 0):
        print(f'{nota50} nota(s) de 50 reais"')
    if (nota10 > 0):
        print(f'{nota10} nota(s) de 10 reais"')
    if (nota5 > 0):
        print(f'{nota5} nota(s) de 5 reais"')
    if (nota1 > 0):
        print(f'{nota1} nota(s) de 1 real"')'''


'''22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da
divisão).
n1 = int(input('Digite um numero, que vamos determinar se ele é par ou ímpar: '))
if (n1 % 2 == 0):
    print(f'O {n1} é um número "PAR"')
else:
    print(f'O {n1} é um número "ÍMPAR"')'''

'''23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
n1 = float(input('Digite um numero qualquer: '))
numero_arendondado = round(n1)

if n1 == numero_arendondado:
    print(f'{n1:.0f} é um número inteiro')
else:
    print(f'{n1} é um número decimal')'''

'''24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
operacoes = input('Qual operção o usuário deseja usar?\n"+"<>Adição\n"-"<>Subtração\n"*"<>Multiplicação\n"/"<>Divisão\nDigite o nome da operação: ')
if (operacoes == '+'):
    resultado = n1 + n2
elif (operacoes == '-'):
    resultado = n1 - n2
elif(operacoes == '*'):
    resultado = n1 * n2
elif(operacoes == '/'):
    if (n2 != 0):
        resultado = n1 / n2
    else:
        print('Erro! Divisão por 0 não é permitida!')
else:
    print('Operação Invalida')
par_ou_impar = 'Par' if resultado % 2 == 0 else 'Impar'
positivo_ou_negativo = 'positivo' if resultado > 0 else 'Negativo'
inteiro_ou_decimal = 'inteiro' if resultado.is_integer() else 'decimal'
print(f'Resultado da operação: {resultado}')
print(f'O número é {par_ou_impar}, {positivo_ou_negativo}, e {inteiro_ou_decimal}')'''

'''25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
resposta_positiva = 0
pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para a vítima? ')
pergunta5 = input('Já trabalhou com a vítima? ')

if(pergunta1 == 'sim'):
   resposta_positiva = resposta_positiva + 1
if(pergunta2 == 'sim'):
   resposta_positiva = resposta_positiva + 1
if(pergunta3 == 'sim'):
   resposta_positiva = resposta_positiva + 1
if(pergunta4 == 'sim'):
   resposta_positiva = resposta_positiva + 1
if(pergunta5 == 'sim'):
   resposta_positiva = resposta_positiva + 1

if resposta_positiva == 2:
    print('Você é classificado como "Suspeito"')
elif 3 <= resposta_positiva <= 4:
    print('Você é classificado como "Cúmplice"')
elif resposta_positiva == 5:
    print('Você é classificado como "Assassino"')
else:
    print('Você é classificado como "Inocente"')'''

'''26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros_vendidos = float(input('Digite quantos litros foi abastecido: '))
tipo_combustivel = input('Digite G-dasoline e A-álcool: ')
gasolina = 2.50
alcool = 1.90
preco_gasolina = litros_vendidos * gasolina
preco_alcool = litros_vendidos * alcool

if (tipo_combustivel == 'A'):
    if litros_vendidos <= 20:
        desconto = preco_alcool * 0.97
    else:
        desconto = preco_alcool * 0.95
if (tipo_combustivel == 'G'):
    if litros_vendidos <= 20:
        desconto = preco_gasolina * 0.96
    else:
        desconto = preco_gasolina * 0.94
print(f'O valor a ser pago pelo cliente é R$ {desconto:.2f}')'''

'''27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
            Até 5 Kg        Acima de 5 Kg
Morango     R$ 2,50 por Kg  R$ 2,20 por Kg
Maçã        R$ 1,80 por Kg  R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

quantidade_morango = float(input('Digite a quantidade de morango: '))
quantidade_maca = float(input('Digite a quantidade de maça: '))

if (quantidade_morango <= 5):
    preco_morango = quantidade_morango * 2.50
else:
    preco_morango = quantidade_morango * 2.20
if (quantidade_maca <= 5):
    preco_maca = quantidade_maca * 1.80
else:
    preco_maca = quantidade_maca * 1.50
preco_total = preco_maca + preco_morango

#Aplicando o desconto para compra acima de 8Kg ou acima de R$ 25,00
if (quantidade_maca + quantidade_morango > 8 or preco_maca + preco_morango > 25):
    desconto = preco_total * 1.90
    preco_total = desconto - preco_total
print(f'O valor pago pelo cliente é R$ {preco_total:.2f}')'''

'''28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                Até 5 Kg        Acima de 5 Kg
File Duplo    R$ 4,90 por Kg      R$ 5,80 por Kg
Alcatra       R$ 5,90 por         Kg R$ 6,80 por Kg
Picanha       R$ 6,90 por         Kg R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

tipo_de_carne = input('Escreva qual tipo de carne o cliente deseja levar:\nF - File Bovino\nP - Picanha'
                      '\nA - Alcatra\nDigite qual deseja: ')
quantidade_carne = float(input('Digite o total de quilos: '))
cartao = input('Você deseja pagar com o cartão Tabajara? ')

if (tipo_de_carne == 'F'):
    nome = 'File Bovino'
    if quantidade_carne <= 5:
        valordacarne = quantidade_carne * 4.90
    else:
        valordacarne = quantidade_carne * 5.80
elif(tipo_de_carne == 'A'):
    nome = 'Alcatra'
    if quantidade_carne <= 5:
        valordacarne = quantidade_carne * 5.90
    else:
        valordacarne = quantidade_carne * 6.80
elif(tipo_de_carne == 'P'):
    nome = 'Picanha'
    if quantidade_carne <= 5:
        valordacarne = quantidade_carne * 6.90
    else:
        valordacarne = quantidade_carne * 7.80
else:
    print('O que você digitou está fora dos parâmentros!')

if cartao == 'sim':
    des = '5%'
    desconto = valordacarne - (valordacarne * 0.95)
else:
    des = ''
    desconto = 0

valortotal =  valordacarne - desconto
print('\n')

print( 10 * '=','CUPOM FISCAL',10 * '=','\n')
print('\tSupermercado Tabajara\n\n')

print(f'Qual o tipo de carne escolhida: {nome}')
print(f'Qual a quantidade de carne comprada: {quantidade_carne} quilos')
print(f'Qual o preço da carne sem desconto R$ {valordacarne:.2f} reais')
print(f'Você usou o cartão Tabajara? {cartao}')
print(f'O valor do desconto foi de R$ {desconto:.2f} reais')
print(f'Total a pagar será de R$ {valortotal:.2f} reais')
