from ASFunction.ImageFunction import PicGetWidth, PicGetHeight

def FindMin(x1, x2, x3, x4, x5, x6, x7, x8, ori, g):
    thisweight = []
    thisweight.append(abs(g.cost(ori, x1)))
    thisweight.append(abs(g.cost(ori, x2)))
    thisweight.append(abs(g.cost(ori, x3)))
    thisweight.append(abs(g.cost(ori, x4)))
    thisweight.append(abs(g.cost(ori, x5)))
    thisweight.append(abs(g.cost(ori, x6)))
    thisweight.append(abs(g.cost(ori, x7)))
    thisweight.append(abs(g.cost(ori, x8)))
    min = 100
    out = []
    for i in range(8):
        if thisweight[i] < min:
            min = thisweight[i]
    if min == abs(g.cost(ori, x1)) and x1 > 0:
        out.append(x1)
        return [x1, min]
    if min == abs(g.cost(ori, x2)) and x2 > 0:
        out.append(x2)
        return [x2, min]
    if min == abs(g.cost(ori, x3)) and x3 > 0:
        out.append(x3)
        return [x3, min]
    if min == abs(g.cost(ori, x4)) and x4 > 0:
        out.append(x4)
        return [x4, min]
    if min == abs(g.cost(ori, x5)) and x5 > 0:
        out.append(x5)
        return [x5, min]
    if min == abs(g.cost(ori, x6)) and x6 > 0:
        out.append(x6)
        return [x6, min]
    if min == abs(g.cost(ori, x7)) and x7 > 0:
        out.append(x7)
        return [x7, min]
    if min == abs(g.cost(ori, x8)) and x8 > 0:
        out.append(x8)
        return [x8, min]


def GainTree(g, pic, cost, num, treelist, threshold):
    width = PicGetWidth(pic)
    '''
        vertexnum1 — vertexnum2 — vertexnum3
            |            |            |
            |            |            |
            |            |            |
        vertexnum4 — — — i  — — — vertexnum5
            |            |            |
            |            |            |
            |            |            |
        vertexnum6  — vertexnum7 — vertexnum8

    '''
    vnum1 = num - width - 1
    vnum2 = num - width
    vnum3 = num - width + 1
    vnum4 = num - 1
    vnum5 = num + 1
    vnum6 = num + width - 1
    vnum7 = num + width
    vnum8 = num + width + 1
    next = FindMin(vnum1, vnum2, vnum3, vnum4, vnum5, vnum6, vnum7, vnum8, num, g)[0]
    weight = FindMin(vnum1, vnum2, vnum3, vnum4, vnum5, vnum6, vnum7, vnum8, num, g)[1]
    if cost < threshold:
        treelist.append(next)
        cost += weight
        num = next
        GainTree(g, pic, cost, num, treelist, threshold)
    else:
        None


def TestMST(g, pic, num, threshold, cost):
    treelist = []
    treenum = 0
    if cost < threshold:
        GainTree(g, pic, cost, num, treelist, threshold)
        # print(cost)
    else:
        treenum += 1
        treelist = []
        TestMST(g, pic, num, threshold, cost)
    return [treelist, treenum]


def putpixelMST(pic, x, treelist):
    width = PicGetWidth(pic)
    height = PicGetHeight(pic)
    for i in range(len(treelist)):
        yy = treelist[i] % width
        xx = int((treelist[i] - yy) / width)
        if xx < width and yy < height and xx > 0 and yy > 0:
            x.putpixel((xx, yy), (0, 0, 0))
