import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Fungsi IEPF
# Input berupa list koordinat titik dan list endpoint dari titik 
def iepfFunction(dThreshold, ptList, ePtList):
    maxDPtToLine = 0
    # dThreshold = 60
    ptIndex = -1
    k = 0
    # ePtList[0].append(80)
    # ePtList[1].append(67)
    # print 'awal '       
    # print ePtList

    jumlahTitik = len(ptList[0])
    jumlahEndpoint = len(ePtList[0])
    
    # print 'Jumlah Endpoint Awal{}'.format(jumlahEndpoint)

    for i in range(0, jumlahEndpoint-1):
        varA = float(ePtList[1][i+1] - ePtList[1][i]) / float(ePtList[0][i+1] - ePtList[0][i])
        # listPersamaanGaris[0].append(varA)
        varB = -1.00
        # C = Y - MX
        varC = float(ePtList[1][i] - varA * ePtList[0][i])
        print 'IEPF Line Function {}x  + {}y + {} = 0'.format(varA, varB, varC)
        # print 'Jumlah Titik {}'.format(jumlahTitik)
        # loop sebanyak jumlah titik
        for j in range(ePtList[2][i],ePtList[2][i+1]):
            # print 'j = {}'.format(j)
            if j == 0 or j == ePtList[2][i]:
                continue
            dPtToLine =  float(abs((varA*ptList[0][j] + varB*ptList[1][j] + varC) / (math.sqrt(varA*varA + varB*varB))))
            # print 'D = {}'.format(dPtToLine)
            if dPtToLine > dThreshold:
                if (dPtToLine > maxDPtToLine):
                    maxDPtToLine = dPtToLine
                    ptIndex = j
                    
            # print 'index = {}'.format(ptIndex)
    
    # print 'akhir '       
    
    # print 'ptindex'
    # print ptIndex
    if(ptIndex != -1):
        ePtList[0].insert(jumlahEndpoint-1, ptList[0][ptIndex])
        ePtList[1].insert(jumlahEndpoint-1, ptList[1][ptIndex])
        ePtList[2].insert(jumlahEndpoint-1, ptIndex)
        print ePtList
        iepfFunction(dThreshold, ptList, ePtList)
    else:
        plt.title("IEPF Algorithm")
        plt.plot(ptList[0], ptList[1], 'ro')
        plt.plot(ePtList[0], ePtList[1])
        plt.axis([0, 1000, 0, 1000])
        plt.show()
        print "Calc done"


def main():
    listTitikP = [[5,5],[200,550],[700,550],[600,150]]
    # listTitikP = [[5,5],[450,950]]
    listKoorTitik = [[0,0]]
    listM = [0,0]
    listC = [0,0]
    # Clear list
    del listM[:]
    del listC[:]
    for i in range (0,len(listTitikP)-1):
        # m = (y2 - y1) / (x2 - x1)
        m = float(listTitikP[i+1][1] - listTitikP[i][1]) / float(listTitikP[i+1][0] - listTitikP[i][0])
        # print m
        # c = y - m * x
        c = float(listTitikP[i][1] - m * listTitikP[i][0])
        # print c
        listM.append(m)
        listC.append(c)
        # print(listTitikP[1][1])

    del listKoorTitik[:]
    listKoorTitik.append([])
    listKoorTitik.append([])
    # print listKoorTitik
    # Plot titik 
    # print (len(listTitikP))
    jumlahTitik = 0
    for i in range(0,len(listTitikP)-1):
        step = 0
        if(listTitikP[i][0] > listTitikP[i+1][0]):
            step = -10
        elif(listTitikP[i][0] < listTitikP[i+1][0]):
            step = 10
        for j in range(listTitikP[i][0],listTitikP[i+1][0],step):
            # Random gaussian untuk simulasi noise
            mu, sigma = 0 , 0.1
            k = random.randint(-10, 10)
            # print k
            # l = np.random.normal(mu, sigma, k)
            x = float(j + k)
            # x = float(j)
            # y = mx + c
            y = float((listM[i] * x + listC[i]) + k )
            # print x
            # print y
            # print i
            listKoorTitik[0].append(x)
            listKoorTitik[1].append(y)
            jumlahTitik += 1

    # print listKoorTitik
    distance = 0
    lastDistance = 0
    maxDistance = 0
    p0 = 0
    pN = jumlahTitik-1

    # print 'Maximum D P{}-P{} = {}'.format(p0, pN, maxDistance)
    # print 'P0 {},{} - Pn {},{}'.format(listKoorTitik[0][p0], listKoorTitik[1][p0], listKoorTitik[0][pN], listKoorTitik[1][pN])
    # Kalkulasi persamaan garis dari 2 titik terjauh
    listPersamaanGaris = [[0,0,0]] # Ax + Bx + C = 0
    del listPersamaanGaris[:]
    listPersamaanGaris.append([])
    varA = float(listKoorTitik[1][pN] - listKoorTitik[1][p0]) / float(listKoorTitik[0][pN] - listKoorTitik[0][p0])
    listPersamaanGaris[0].append(varA)
    varB = -1.00
    # C = Y - MX
    varC = float(listKoorTitik[1][p0] - varA * listKoorTitik[0][p0])
    # print 'Gradient P{}-P{} = {}'.format(p0, pN, varA)
    # print 'Persamaan garis {}x + {}y + {} = 0'.format(varA,varB,varC)

    # List predicted line point
    # Isinya point x,y dari titik endpoint
    listPredLinePt = [[0,0]]
    del listPredLinePt[:]
    listPredLinePt.append([])
    # Ambil nilai x dan y dari koordinat titik P0
    
    listPredLinePt.append([])
    listPredLinePt[0].append(listKoorTitik[0][p0])
    listPredLinePt[1].append(listKoorTitik[1][p0])
    # Ambil nilai x dan y dari koordinat titik PN
    listPredLinePt[0].append(listKoorTitik[0][pN])
    listPredLinePt[1].append(listKoorTitik[1][pN])
    dThreshold =200.00
    # print listPredLinePt
    # Hitung jarak antar titik
    foundBreakpoint = 1
    maxDPtToLine = 0
    ptIndex = 0
    for i in range(0,jumlahTitik):
        if i == p0 or i == pN:
            continue
        # d = | ax1 + by1 + c / sqrt(a^2 + b^2) |
        dPtToLine =  float(abs((varA*listKoorTitik[0][i] + varB*listKoorTitik[1][i] + varC) / (math.sqrt(varA*varA + varB*varB))))
        # print 'Jarak titik ke garis'
        # print dPtToLine
        # print foundBreakpoint
        if dPtToLine > dThreshold:
            if (dPtToLine > maxDPtToLine):
                maxDPtToLine = dPtToLine
                ptIndex = i
                # foundBreakpoint += 1
            
    listPredLinePt[0].insert(foundBreakpoint, listKoorTitik[0][ptIndex])
    listPredLinePt[1].insert(foundBreakpoint, listKoorTitik[1][ptIndex])

    # INPUT ENDPOINT UNTUK MASUKAN
    # print listPredLinePt
    listEndPoint = [[0,0]]
    del listEndPoint[:]
    listEndPoint.append([])
    listEndPoint.append([])
    listEndPoint.append([])
    # x y P0
    listEndPoint[0].append(listKoorTitik[0][p0])
    listEndPoint[1].append(listKoorTitik[1][p0])
    listEndPoint[2].append(p0)

    # simulasi titik tengah
    # listEndPoint[0].append(listKoorTitik[0][45])
    # listEndPoint[1].append(listKoorTitik[1][45])
    # listEndPoint[2].append(45)

    # xy PN
    listEndPoint[0].append(listKoorTitik[0][pN])
    listEndPoint[1].append(listKoorTitik[1][pN])
    listEndPoint[2].append(pN+1)

    # listEndPoint[0].append(50)
    # listEndPoint[1].append(30)

    # listEndPoint[0].append(60)
    # listEndPoint[1].append(40)

    # print listEndPoint
    # print listKoorTitik
    iepfFunction(100, listKoorTitik, listEndPoint)

    

if __name__ == "__main__":
    main()