#/usr/bin/python3

def domino(dm1, dm2):
    resultantDomino = dm1 * dm2
    resultantDomino = resultantDomino // 2
    return resultantDomino

if __name__ =="__main__":
    domino1 = int(input("Enter Domino1:\n"))
    domino2 = int(input("Enter Domino2:\n"))
    print(domino(domino1, domino2))
