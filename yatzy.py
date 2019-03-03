class Yatzy:

    @staticmethod
    def chance(*args):
        total = 0
        for arg in args:
            total += arg
        return total

    @staticmethod
    def yatzy(*args):
        num = args[0]
        for arg in args:
            if num != arg:
                return 0
        return 50

    @staticmethod
    def ones(*args):
        sum = 0
        for arg in args:
            if arg == 1:
                sum += 1
        return sum


    @staticmethod
    def twos(*args):
        sum = 0
        for arg in args:
            if arg == 2:
                sum += 2
        return sum

    @staticmethod
    def threes(*args):
        sum = 0
        for arg in args:
            if arg == 3:
                sum +=3
        return sum

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def fours(*args):
        sum = 0
        for arg in args:
            if arg == 4:
                sum += 4
        return sum

    @staticmethod
    def fives(*args):
        sum = 0
        for arg in args:
            if arg == 5:
                sum += 5
        return sum

    @staticmethod
    def sixes(*args):
        sum = 0
        for arg in args:
            if arg == 6:
                sum += 6
        return sum

    @staticmethod
    def pairs(*args):
        pair = 2
        for arg in range(6, 0, -1):
            if  args.count(arg) >= pair:
                return arg * pair
        return 0

    @staticmethod
    def two_pair(*args):
        pair = 2
        count = 0
        for arg in range(6, 0, -1):
            if args.count(arg) >= pair:
                count += arg * pair
        return count

    @staticmethod
    def four_of_a_kind(*args):
        pair = 4
        for arg in range(6, 0, -1):
            if  args.count(arg) >= pair:
                return arg * pair
        return 0


    @staticmethod
    def three_of_a_kind(*args):
        pair = 3
        for arg in range(6, 0, -1):
            if  args.count(arg) >= pair:
                return arg * pair
        return 0


    @staticmethod
    def smallStraight(*args):
        count = 1
        for arg in args:
            if arg == count:
                count += 1
                if count == 5:
                    return 15
        return 0


    @staticmethod
    def largeStraight(*args):
        count = 2
        for arg in args:
            if arg == count:
                count += 1
                if count == 6:
                    return 20
        return 0


    @staticmethod
    def fullHouse(*args):
        flagTwo = False
        flagThree = False

        pair = 2
        twoKind = 0
        for arg in range(6, 0, -1):
            if args.count(arg) >= pair:
                twoKind = arg * pair
                flagTwo = True

        newPair = 3
        threeKind = 0
        for arg in range(6, 0, -1):
            if  args.count(arg) >= newPair:
                threeKind = arg * newPair
                flagThree = True

        if flagTwo and flagThree:
            return twoKind + threeKind
        return 0


if __name__ == '__main__':

    ### TEST CASE ###

    # test case 1
    assert Yatzy.ones(1, 1, 1, 1, 1) == 5
    assert Yatzy.yatzy(1, 1, 1, 1, 1) == 50
    assert Yatzy.yatzy(1, 1, 1, 1, 2) == 0
    assert Yatzy.pairs(1,1,1,2,5,5) == 10
    assert Yatzy.two_pair(1, 1, 3, 3, 2, 3) == 8
    assert Yatzy.three_of_a_kind(1, 1, 1, 3, 2) == 3
    assert Yatzy.four_of_a_kind(1, 1, 1, 1, 3, 2) == 4
    assert Yatzy.smallStraight(1, 2, 3, 4, 5, 6, 5, 3, 4) == 15
    assert Yatzy.smallStraight(1, 2, 3, 6) == 0
    assert Yatzy.largeStraight(1, 2, 2, 3, 4, 5, 6, 5, 6) == 20
    assert Yatzy.fullHouse(1, 1, 2, 2, 2, 3, 5) == 8
    assert Yatzy.fullHouse(4, 4, 6, 6, 6, 2, 1) == 26

    # test case 2
    assert Yatzy.ones(1, 1, 1) == 3

    # test case 3
    assert Yatzy.ones(1, 1, 1, 1, 1, 1, 2, 1) == 7

    # test case 4
    assert Yatzy.twos(2, 2, 2, 3) == 6

    # test case 5
    assert Yatzy.threes(3, 3, 2, 3) == 9

    # test case 6
    assert Yatzy.threes(3, 2, 1, 8) == 3

    # test case 7
    assert Yatzy.fours(4, 4, 1, 8) == 8

    # test case 8
    assert Yatzy.fives(5, 5, 3, 6, 4, 5) == 15

    # test case 9
    assert Yatzy.sixes(6, 6, 6, 4, 3) == 18
