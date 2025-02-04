numeros=[1,2,3,4,5,6,7,8,9,10]
pares=[]
impares=[]
def separa_pares_D_impares(numeros):
 for n in numeros:
     if(n %2==0):
         pares.append(n)
     else:
         impares.append(n)
         print(f'Pares {pares}')
         print(f'Impares {impares}')

separa_pares_D_impares(numeros)