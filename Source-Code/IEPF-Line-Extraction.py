# Author EK
import math
import matplotlib.pyplot as plt
import numpy as np
import random

def measPointToPoint(varP1, varP2):
    return math.sqrt(((varP2[0]-varP1[0])*(varP2[0]-varP1[0])) + ((varP2[1]-varP1[1])*(varP2[1]-varP1[1])))

# https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
def measPointToLine(varPk, varPl, varP0):
    return abs((varPl[1]-varPk[1])*varP0[0] - (varPl[0]-varPk[0])*varP0[1] + varPl[0]*varPk[1] - varPl[1]*varPk[0]) / math.sqrt( math.pow((varPl[0] - varPk[0]),2) + math.pow((varPl[1] - varPk[1]),2) )

# Fungsi IEPF
# Input berupa list koordinat titik dan list endpoint dari titik 
# Ouput berupa list persamaan garis dalam bentuk Ax + By + C = 0
def iepfFunction(dThreshold, ptList, ePtList):
    maxDPtToLine = 0
    breakPointIndex = -1

    # listLineFunc = [[0,0]]
    # del listLineFunc[:]
    # listLineFunc.append([])
    # listLineFunc.append([])
    # listLineFunc.append([])

    # listLineEndPoint = [[0,0]]
    # del listLineEndPoint[:]
    # listLineEndPoint.append([])
    # listLineEndPoint.append([])
    # listLineEndPoint.append([])

    # jumlahTitik = len(ptList[0])
    jumlahEndpoint = len(ePtList[0])

    # loop sebanyak jumlah end point yang diinputkan
    for i in range(0, jumlahEndpoint-1):
        # A = y2 - y1 / x2 - x1
        varA = float(ePtList[1][i+1] - ePtList[1][i]) / float(ePtList[0][i+1] - ePtList[0][i])
        # B = -1
        varB = -1.00
        # C = y - Ax
        varC = float(ePtList[1][i] - varA * ePtList[0][i])
        # print 'IEPF Line Function {}x  + {}y + {} = 0'.format(varA, varB, varC)
        # listLineFunc[0].append(varA)
        # listLineFunc[1].append(varB)
        # listLineFunc[2].append(varC)
        # loop sebanyak jumlah titik yang berada diantara endpoint
        for j in range(ePtList[2][i],ePtList[2][i+1]):
            # print 'j = {}'.format(j)
            if j == 0 or j == ePtList[2][i]:
                continue
            # Pengukuran jarak titik ke line
            # d = | ax1 + by1 + c / sqrt(a^2 + b^2) |
            dPtToLine =  float(abs((varA*ptList[0][j] + varB*ptList[1][j] + varC) / (math.sqrt(varA*varA + varB*varB))))
            # print 'D = {}'.format(dPtToLine)
            if dPtToLine > dThreshold:
                if (dPtToLine > maxDPtToLine):
                    maxDPtToLine = dPtToLine
                    breakPointIndex = j

    if(breakPointIndex != -1):
        # Cari nilai MNE        
        ePtList[0].insert(jumlahEndpoint-1, ptList[0][breakPointIndex])
        ePtList[1].insert(jumlahEndpoint-1, ptList[1][breakPointIndex])
        ePtList[2].insert(jumlahEndpoint-1, breakPointIndex)

        # pawal = [ePtList[0][jumlahEndpoint-2],ePtList[1][jumlahEndpoint-2]]
        # pakhir = [10,10]
        # pnol = [5,4]
        # varMNE0 = maxDPtToLine / measPointToLine()
        # print ePtList
        ePtList = iepfFunction(dThreshold, ptList, ePtList)
    # else:
        # plt.title("IEPF Algorithm")
        # plt.plot(ptList[0], ptList[1], 'ro')
        # plt.plot(ePtList[0], ePtList[1])
        # plt.axis([0, 1000, 0, 1000])
        # plt.show()
        # print listLineFunc
    return ePtList

def mergeLine(mneThreshold, ptList, ePtList):
    jumlahEndpoint = len(ePtList[0])
    for i in range(0, jumlahEndpoint-2):
        # print 'garis'
        varPk = [ePtList[0][i] , ePtList[1][i]]
        varPl = [ePtList[0][i+2] , ePtList[1][i+2]]
        varP0 = [ePtList[0][i+1] , ePtList[1][i+1]]
        varMaxDistance = measPointToLine(varPk,varPl,varP0)
        varPk = [ePtList[0][i] , ePtList[1][i]]
        varPl = [ePtList[0][i+1] , ePtList[1][i+1]]
        prevIndex = ePtList[2][i+1] - 1
        nextIndex = ePtList[2][i+1] + 1
        # print 'PREV {} NEXT{}'.format(prevIndex, nextIndex) 
        varP0 = [ptList[0][prevIndex], ptList[1][nextIndex]]
        # print 'K {},{} L {},{} P0 {},{}'.format(varPk[0], varPk[1], varPl[0], varPl[1], varPl[0], varPl[1])
        print varPk
        print varPl
        print varP0
        xx = measPointToLine(varPk,varPl,varP0)
        varMNEprev = varMaxDistance / xx
        # print 'MNE Prev {}'.format(varMNEprev)
        print 'Prev list'
        print ePtList
        if varMNEprev > 2:
            # remX = ePtList[0][i+1]
            # remY = ePtList[1][i+1]
            # remIndex = ePtList[2][i+1]
            # ePtList[0].remove(remX)
            ePtList[0].pop(i+1)
            ePtList[1].pop(i+1)
            ePtList[2].pop(i+1)
        # print 'K {},{} L {},{}'.format(varPk[0], varPk[1], varPl[0], varPl[1],)
        # for j in range(ePtList[2][i],ePtList[2][i+1]):
        print 'last list'
        print ePtList
    return ePtList

def main():
    listLineL = [[5,5],[200,550],[700,550],[600,150]]
    listPointP = [[0,0]]
    listGradientL = [0,0]
    listConstantaL = [0,0]
    # Clear list
    del listGradientL[:]
    del listConstantaL[:]
    for i in range (0,len(listLineL)-1):
        # M = (y2 - y1) / (x2 - x1)
        varM = float(listLineL[i+1][1] - listLineL[i][1]) / float(listLineL[i+1][0] - listLineL[i][0])
        # C = y - m * x
        varC = float(listLineL[i][1] - varM * listLineL[i][0])
        listGradientL.append(varM)
        listConstantaL.append(varC)

    del listPointP[:]
    listPointP.append([])
    listPointP.append([])

    for i in range(0,len(listLineL)-1):
        step = 0
        if(listLineL[i][0] > listLineL[i+1][0]):
            step = -10
        elif(listLineL[i][0] < listLineL[i+1][0]):
            step = 10
        for j in range(listLineL[i][0],listLineL[i+1][0],step):
            # Random noise
            # simNoise = 0
            simNoise = random.randint(-20, 20)
            pointX = float(j + simNoise)
            # y = mx + c
            pointY = float((listGradientL[i] * pointX + listConstantaL[i]) + simNoise )
            listPointP[0].append(pointX)
            listPointP[1].append(pointY)

    # Simulasi endpoint
    '''
    del listPointP[:]
    listPointP.append([])
    listPointP.append([])

    listPointP[0] = [0,100,200,300,350,505,450,500,550,600]
    listPointP[1] = [300,350,400,501,450,600,350,300,200,100]
    '''

    # Input 2 buah endpoint untuk masukan awal
    endPoint0 = 0
    endPointN = len(listPointP[0])-1

    listEndPoint = [[0,0]]
    del listEndPoint[:]
    listEndPoint.append([])
    listEndPoint.append([])
    listEndPoint.append([])

    # endPoint0 x,y coordinat dan index
    listEndPoint[0].append(listPointP[0][endPoint0])
    listEndPoint[1].append(listPointP[1][endPoint0])
    listEndPoint[2].append(endPoint0)

    # endPointN x,y coordinat dan index
    listEndPoint[0].append(listPointP[0][endPointN])
    listEndPoint[1].append(listPointP[1][endPointN])
    listEndPoint[2].append(endPointN+1)

    # fungsi IEPF dengan threshold 100
    lsih = iepfFunction(80, listPointP, listEndPoint)
    print lsih
    # lsih = mergeLine(9,listPointP,lsih)
    plt.title("IEPF Algorithm")
    plt.plot(listPointP[0], listPointP[1], 'ro')
    plt.plot(lsih[0], lsih[1])
    plt.axis([0, 1000, 0, 1000])
    plt.show()
    # pawal = [0,0]
    # pakhir = [10,10]
    # pnol = [5,4]
    # print measPointToLine(pawal,pakhir,pnol)

if __name__ == "__main__":
    main()