def decoderOK():
    coord = []
    file = open('points.txt', 'r')
    mas = file.read().split('\n')
    for i in range(len(mas) - 1):
        coord.append([])
        coord[i].append(float(mas[i][1:4]))
        coord[i].append(float(mas[i][6:9]))
    return coord
