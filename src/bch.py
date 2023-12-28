import utilsG
import utilsP
import functools

def minP(beta, modulus):
  p = [beta, 1]
  current_beta = beta
  while(True):
    current_beta = utilsG.prodG(current_beta,current_beta,modulus)
    if current_beta == beta:
      break
    p = utilsP.prodP(p, [current_beta, 1], modulus)
  return p

def puja(p):
  list = [*map(int, bin(p)[2:])]
  return list[::-1]

def baixa(n):
  return int(''.join(map(str, n[::-1])), 2)

def valueInArray(array, value):
    for val in array:
        if val == value:
            return True
    return False

def genBCH(beta, D, modulus):
  results = [minP(utilsG.expG(beta, i, modulus), modulus) for i in range(1, D)]
  filteredResults = [result for (i,result) in enumerate(results) if not valueInArray(results[0:i], result)]

  return functools.reduce(lambda result, acc: utilsP.prodP(acc, result, modulus), filteredResults)

def sindBCH(received, beta, D, modulus):
  return  

def sugiBCH(syndrome, beta, D, modulus):
  return

def dimBCH(beta, n, D, modulus):
  return