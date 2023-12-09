from utilsP import divP, sumP, prodP, grauP
from utilsG import expG

beta = 2

def EEP(poly1, poly2, grau, modulus):
  p1 = poly1
  p2 = poly2
  r = []
  w = p2
  while (grauP(p2, modulus) >= grau):
    [quotient, remainder] = divP(p1, p2, modulus)
    r.append(quotient)
    w = remainder
    p1, p2 = p2, remainder
  
  l1 = []
  l2 = [1]
  p1 = [1]
  p2 = []
  l, p = [], []
  for reminder in r: 
    l = sumP(l1, prodP(reminder, l2, modulus))
    p = sumP(p1, prodP(reminder, p2, modulus))
    l1, l2 = l2, l
    p1, p2 = p2, p
  return [w, p, l]

def genRS(r, b, modulus):
  g = [1]
  for i in range(r):
    g = prodP(g, [expG(b, i+1, modulus), 1], modulus)
  return g

def subsP(value, poly, modulus):
  remainder = divP(poly, [value, 1], modulus)[1] or [0]
  return remainder[0]

def sindRS(received, b, r, modulus):
  return [subsP(expG(b, i+1, modulus), received, modulus) for i in range(r)]

def sugiRS(syndrome, r, modulus):
  xr = [0] * r + [1]
  [w, p, _] = EEP(syndrome, xr, r//2, modulus)
  return [w, p]

def roots(pol, modulus):
  return [i for i in range(modulus) if (subsP(i, pol, modulus) == 0)]

def derivate(pol):
  derivate = []
  for i in range(len(pol)-1):
    if (i % 2 == 0): derivate.append(0)
    else: derivate.append((i+1)*pol[i+1])
  return derivate