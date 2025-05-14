import time

print ('=====GERADOR DE TABUADA=====')

num1 = int(input('Qual número deseja saber a tabuada:'))
num2 = int(input('Até que número a tabuada deve ser gerada:'))
print('Tabuada sendo gerada....')
time.sleep(1.5)
for i in range(1,num2+1):
    print (f'{num1}x{i}={num1*i}')

