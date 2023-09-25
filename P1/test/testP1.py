import sys
path = sys.path[0]
sys.path.insert(0, path.replace('/test', '/src'))
from problem1 import prod, div, bez

def testProd():
  tests = [(1234,5678), (123,456), (87654321,1234567),(111111,333333)]
  expected = [5728828, 23448, 99473114910871, 31751616619]
  for (a,b),e in zip(tests,expected):
    assert prod(a,b) == e
  print("TestProd: OK")

def testDiv():
  tests = [(1234,123), (111111,4444), (12345678,654321), (55555,333)]
  expected = [[27, 55], [26, 3999], [20, 274842], [228, 87]]
  for (a,b),e in zip(tests,expected):
    assert div(a,b) == e
  print("TestDiv: OK")

def testBez():
  tests = [(23436,7656677), (1112342,4567123), (12345,67890), (123,123456)]
  expected = [[387739, 1681],  [74840, 20459], [28065, 2869], [17001, 16]]
  for (a,b),e in zip(tests,expected):
    assert bez(a,b) == e
  print("TestBez: OK")


testProd()
testDiv()
testBez()