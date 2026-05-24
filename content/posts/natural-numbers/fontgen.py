from numbers import cout, cset


def font():
    fontname = "7UP.64C"
    digitidx = 48

    rawdata = open(fontname, "rb").read()[2:]
    result = []

    for offset in range(digitidx * 8, (digitidx + 10) * 8, 8):
        c = 8
        for y in range(8):
            ch = rawdata[offset + y]
            for x in range(8):
                if (1 << x) & ch:
                    c = cset(c, 7 - x, y)
        print(cout(c))
        result.append(c)
    print(result)


font()
