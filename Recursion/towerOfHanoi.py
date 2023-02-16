def towerOfHanoi(disks, start = 1, end = 3):
    if disks:
        towerOfHanoi(disks - 1, start, 6 - start - end)
        print("Move disk {} from peg {} to peg {}".format(disks, start, end))
        towerOfHanoi(disks - 1, 6-start-end, end)
if __name__ == "__main__":
    disks = int(input("Please inter number of disks:\n"))
    towerOfHanoi(disks)
