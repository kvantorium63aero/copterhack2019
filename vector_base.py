import cv2
import math

image = cv2.imread('kek.png', 0)

im = image.shape

image1 = []
for i in range(len(image)):
    image1.append([])
    for j in range(len(image[0])):
        if image[i][j] >= 255:
            image1[i].append(0)
        else:
            image1[i].append(1)

leninm = 30
lenjnm = (len(image1[0]) / len(image1)) * 30
lenjnm = int(lenjnm)

i1 = len(image1[0]) // lenjnm
i2 = len(image1) // leninm
i1 += 1
i2 += 1

new_mas = []
mas_count = []
k = 0
for ii in range(leninm):
    mas_count.append([])
    new_mas.append([])
    for ij in range(lenjnm):
        sum = 0
        if (ii + 1) * i1 < len(image1):
            rgi = (ii + 1) * i1
        else:
            rgi = len(image1)
        if (ij + 1) * i2 < len(image1[0]):
            rgj = (ij + 1) * i2
        else:
            rgj = len(image1[0])
        for i in range(ii * i1,  rgi):
            for j in range(ij * i2, rgj):
                k += 1
                sum += image1[i][j]
        mas_count[ii].append(sum)
        if sum >= 3:
            new_mas[ii].append(1)
        else:
            new_mas[ii].append(0)


coord = []

for i in range(len(new_mas) - 1, 1, -1):
    for j in range(len(new_mas[0])):
        if new_mas[i][j] == 1:
            coord.append([])
            coord[-1].append((i + 1) / 10)
            coord[-1].append((j + 1) / 10)


way = []
cX = coord[0][0]
cY = coord[0][1]
way.append([])
way[0].append(cX)
way[0].append(cY)
k = 1
del coord[0]

while (len(coord) != 0):
    minr = 10e10
    ind = 0
    for i in range(len(coord)):
        if math.sqrt((coord[i][0] - cX) ** 2 + (coord[i][1] - cY) ** 2) < minr:
            minr = math.sqrt((coord[i][0] - cX) ** 2 + (coord[i][1] - cY) ** 2)
            ind = i
            cX = coord[i][0]
            cY = coord[i][1]
    way.append([])
    way[k].append(cX)
    way[k].append(cY)
    k += 1
    del coord[ind]

f = open('points.txt', 'w')
for i in range(len(way)):
    f.write(str(way[i]) + '\n')
f.close()

decoderOK.decoderOK()
