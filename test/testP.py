import sys
path = sys.path[0]
sys.path.insert(0, path.replace('/test', '/src'))
import reedSolomon as rs


def testEEP():
  print("Running testEEP")
  tests = [([12,23,3,43,5,46,34,34,4],[77,66,55,44,33],4,1917), ([12,23,3,43,5,46,34,34,4],[77,66,55,44,33],3,1917), ([12,23,3,43,5,46,34,34,4],[77,66,55,44,33],2,1917), ([12,23,3,43,5,46,34,34,4],[77,66,55,44,33],1,1917), ([12,23,3,43,5,46,34,34,4],[77,66,55,44,33],0,1917)]
  expected = [[[575, 835, 78, 999], [1, 0, 0, 0], [891, 811, 728, 317, 518]], [[885, 164, 798], [192, 71], [621, 16, 279, 492, 320, 913]],  [[102, 1018], [1005, 600, 715], [551, 375, 174, 353, 437, 147, 510]],  [[651], [611, 145, 804, 372], [337, 715, 187, 16, 701, 99, 843, 763]],  [[], [387, 356, 646, 789, 178], [519, 916, 736, 8, 93, 85, 594, 594, 509]]]
  for (a, b, c, d), e in zip(tests, expected):
    assert rs.EEP(a, b, c, d) == e
  print("TestEEP: OK\n")

def testGenRS():
  print("Running TestGenRS")
  tests = [(6,2,1917),(10,2,1917),(10,7,1917),(15,11,1917)]
  expected = [[44, 435, 480, 783, 610, 126, 1],[728, 572, 874, 162, 372, 124, 427, 1006, 916, 131, 1],[942, 710, 406, 699, 664, 671, 582, 1021, 366, 305, 1],[937, 440, 130, 542, 408, 759, 218, 516, 25, 252, 451, 36, 933, 53, 513, 1]]
  for (a, b, c), e in zip(tests, expected):
    assert rs.genRS(a, b, c) == e
  print("TestGenRS: OK\n")

def testSubsP():
  print("Running TestSubsP")
  tests = [(23,[1,2,3],1917),(23,[1,2,3,4,5,6,7],1917),(111,[1,2,3,4,5,6,7,8,9,10,11,12,13],1917)]
  expected = 784,739,997
  for (a, b, c), e in zip(tests, expected):
    assert rs.subsP(a, b, c) == e
  print("TestSubsP: OK\n")


def testSindRS():
  print("Running TestSindRS")
  tests = [([1,2,3,4,5,6,7,8,9,10,11,12,13],2,4,1917),([1,2,3,4,5,6,7,8,9,10,11,12,13],7,8,1917),([1,2,3,4,5,6,7,8,9,10,11,12,13],11,15,1917)]
  expected = [[509, 912, 450, 887],[92, 487, 360, 761, 660, 336, 167, 605],[15, 1007, 206, 330, 783, 155, 958, 385, 650, 621, 541, 769, 59, 877, 276]]
  for (a, b, c, d), e in zip(tests, expected):
    assert rs.sindRS(a, b, c, d) == e
  print("TestSindRS: OK\n")

def testSugiRS():
  print("Running TestSugiRS")
  tests = [([1,2,3,4,5,6,7,8],8,1961), ([1,2,3,4,5,6,7,8],10,1961), ([1,2,3,4,5,6,7,8],12,1961)]
  expected = [([[298, 224, 926, 769], [298, 692, 545, 926, 351]]), ( [[477, 665, 221, 393, 750], [477, 291, 252, 969, 500, 651]]), ([[264, 606, 580, 175, 303, 744], [264, 78, 448, 116, 62, 590, 763]])]
  for (a, b, c), e in zip(tests, expected):
    assert rs.sugiRS(a, b, c) == e
  print("TestSugiRS: OK\n")



if (__name__ == "__main__"):
  testEEP()
  testGenRS()
  testSubsP()
  testSindRS()
  testSugiRS()