def decoderOK():
    file = open('points.txt', 'r')
    mas = file.read().split('\n')
    for i in range(len(mas) - 1):
        print('x = ' + mas[i][1:4] + ', y = ' + mas[i][5:9])
