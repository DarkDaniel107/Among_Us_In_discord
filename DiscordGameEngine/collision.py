def line_intersect(Line1, Line2):
    """
        :var\n
        Uses: Line1 being -> ((x, y), (x, y))\n
        Line2 being -> ((x, y),(x, y))\n

        :returns\n
        (x, y) if there is a intersection.\n
        None if there is not a intersection.
        """
    Ax1 = Line1[0][0]
    Ay1 = Line1[0][1]
    Ax2 = Line1[1][0]
    Ay2 = Line1[1][1]

    Bx1 = Line2[0][0]
    By1 = Line2[0][1]
    Bx2 = Line2[1][0]
    By2 = Line2[1][1]

    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not (0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)

    return x, y


if __name__ == '__main__':
    LineA = ((4, 0), (6, 4))  # try (4, 0), (6, 4)
    LineB = (0, 3), (10, 7)  # for non intersecting test
    pt = line_intersect(LineA, LineB)
    print(pt)
