from utilsG import *

#Suma de polinomis, no cal modul
def sumP(polinomi1,polinomi2):
  l1=len(polinomi1)
  l2=len(polinomi2)
  if l1 <= l2:
    p1=polinomi1
    p2=polinomi2
  else:
    p1=polinomi2
    p2=polinomi1
  for i in range(min(l1,l2)):
    p2[i]=p1[i]^p2[i]
  return p2
# redueix el polinom pol (treu els coeficients 0 a la dreta)
def redP(pol,modul):
  while pol!=[] and div(pol[-1],modul)[1]==0:
    del pol[-1]
  return pol # list(map(lambda x: div(x,modul)[1], pol))

def grauP(pol, modul):
  return len(redP(pol,modul))-1

def prodP(polinomi1,polinomi2,modul): #polinomi1, polinomi2 polinomis,
  polinomi1=redP(polinomi1,modul)
  grau1=len(polinomi1)-1
  polinomi2=redP(polinomi2,modul)
  grau2=len(polinomi2)-1
  producte=[0 for i in range(grau1+grau2+1)]
  for i in range(grau1+1):
    for j in range(grau2+1):
      producte[i+j]=producte[i+j]^prodG( polinomi1[i],polinomi2[j],modul )
  return producte
#mpou a la dreta el polinomi nombrePosicions
# multiplica polinomi per x**nombrePosicions
def mouP(polinomi,nombrePosicions):
  return [0 for i in range(nombrePosicions)]+ polinomi


def divP(polinomi1,polinomi2,modul):
  polinomi1=redP(polinomi1,modul)
  grau1=len(polinomi1)-1
  polinomi2=redP(polinomi2,modul)
  grau2=len(polinomi2)-1
  invers=invG(polinomi2[-1],modul)
  residus=polinomi1
  quocient=[0 for i in range(grau1-grau2+1)]
  while len(residus)>=len(polinomi2):
    grauResidus=len(residus)-1
    quot=prodG( residus[-1] , invers , modul )
    quocient[grauResidus-grau2]= quot
    residus=redP( sumP( residus , mouP( prodP( [quot] , polinomi2 , modul ),
    grauResidus-grau2 ) ) , modul )
  return [quocient,residus]


def evalP(poly, value, modulus):
  acc = 0
  for index, pos in enumerate(poly):
    acc += prodG(pos, expG(value, index, modulus), modulus)
  return acc
  