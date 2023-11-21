from utilsP import divP, sumP, prodP, grauP, evalP
from utilsG import expG

def EEP(poly1, poly2, grau, modulus):
  p1 = poly1
  p2 = poly2
  r = []
  w = p2
  while (grauP(p2, modulus) >= grau):
    [quotient, remainder] = divP(p1, p2, modulus)
    r.append(quotient)
    w = remainder
    p1 = p2
    p2 = remainder
  
  l1 = []
  l2 = [1]
  p1 = [1]
  p2 = []
  for _, reminder in enumerate(r): 
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

def sindRS(received, b, r, modulus):
  s = []
  for i in range(r):
    si = evalP(received, expG(b, i+1, modulus), modulus)
    s.append(si)
  return s