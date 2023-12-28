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

def genBCH(beta, D, modulus):
  # fer el set de fer minP desde B find a B**D-1
  return

def sindBCH(received, beta, D, modulus):
  return  

def sugiBCH(syndrome, beta, D, modulus):
  return

def dimBCH(beta, n, D, modulus):
  return