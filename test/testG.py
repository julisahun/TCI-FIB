import sys
path = sys.path[0]
sys.path.insert(0, path.replace('/test', '/src'))
from utilsG import prod, div, bez, prodG, invG, expG, ordG


def testProd():
    print("Running testProd")
    tests = [(1234, 5678), (123, 456), (87654321, 1234567), (111111, 333333)]
    expected = [5728828, 23448, 99473114910871, 31751616619]
    for (a, b), e in zip(tests, expected):
        assert prod(a, b) == e
    print("TestProd: OK\n")


def testDiv():
    print("Running testDiv")
    tests = [(1234, 123), (111111, 4444), (12345678, 654321), (55555, 333)]
    expected = [[27, 55], [26, 3999], [20, 274842], [228, 87]]
    for (a, b), e in zip(tests, expected):
        assert div(a, b) == e
    print("TestDiv: OK\n")


def testBez():
    print("Running testBez")
    tests = [(23436, 7656677), (1112342, 4567123),
             (12345, 67890), (123, 123456)]
    expected = [[387739, 1681],  [74840, 20459], [28065, 2869], [17001, 16]]
    for (a, b), e in zip(tests, expected):
        assert bez(a, b) == e
    print("TestBez: OK\n")


def testProdG():
    print("Running testProdG")
    tests = [(1234234, 43267, 1033), (1233444, 6543, 1033), (333, 55555, 1033)]
    expected = [995, 408, 913]
    for (a, b, g), e in zip(tests, expected):
        assert prodG(a, b, g) == e
    print("TestProdG: OK\n")


def testInvG():
    print("Running testInvG")
    tests = [(2345, 1033), (4444, 1033), (4444, 8219), (333, 8219)]
    excepted = [85, 320, 3769, 2060]
    for (a, g), e in zip(tests, excepted):
        assert invG(a, g) == e
    print("TestInvG: OK\n")


def testExpG():
    print("Running testExpG")
    tests = [(666666, 1234, 1033), (22, 76543, 1033),
             (55555, 12345, 8219), (333, 123456, 8219)]
    expected = [545, 4,  7551, 7366]
    for (a, n, g), e in zip(tests, expected):
        assert expG(a, n, g) == e
    print("TestExpG: OK\n")


def testOrdG():
    print("Running testOrdG")
    tests = [(2, 1033), (333, 1033)]
    expected = [1023, 33]
    for (a, g), e in zip(tests, expected):
        assert ordG(a, g) == e
    print("TestOrdG: OK\n")


testProd()
testDiv()
testBez()
testProdG()
testInvG()
testExpG()
testOrdG()
