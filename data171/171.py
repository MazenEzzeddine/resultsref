


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import matplotlib
import math

import csv

from matplotlib.patches import ConnectionPatch
from numpy import double


def graf():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}

    matplotlib.rc('font', **font)
    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0


    #############iiiiiiitttttttttttttttttttiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiooooooooooooooooooooooooooooooooooooooooooooooooooyyyyyyyyyyyyyyyyyyyyyyyyyykkkkkkkkkkkkkkkkkiiii

    print('hello')

    with open('arissuer171.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))


    lr1= [1300, 769, 593, 487, 216, 206, 190, 189,176, 164, 155, 131, 113, 103, 92, 99, 96, 86, 81, 168, 198, 260]
    lr2= [863,843, 841, 833, 818, 806, 793, 783, 771, 764, 745, 724, 695, 663, 627, 579, 563, 524, 483, 440, 358, 320, 282]

    r1end=0
    r1start=0
    tr1= []
    tr2 = []
    r2start = 0
    r2end=0
    with open('rissuer171.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)

            lamda1.append(double(row[1]))
            if double(row[1]) == 350 and r1end!=1:
                tr1.append(s1)
                r1start=1
            if r1start == 1 and double(row[1]) == 175 :
                r1end=1
            if r1end == 1 and double(row[1]) == 350 and r2end != 1 :
                r2start = 1
                tr2.append(s1)
            if r2start == 1 and double(row[1]) == 175:
                r2end = 1

            s1 += 5
    print(tr1)

    t=0
    lt=[]
    lv=[]
    with open('1l.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            lt.append(t)
            t += 5
            lv.append(double(row[1]))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True)  # create the canvas for plotting

    # ax4 = plt.subplot(4, 1, 4)
    # ax1 = plt.subplot(4, 1, 1, sharex=ax4)
    # # (2,1,1) indicates total number of rows, columns, and figure number respectively
    # ax2 = plt.subplot(4, 1, 2, sharex=ax4)
    # ax3 = plt.subplot(4, 1, 3, sharex=ax4)

    sect = 0
    sec = []
    secta = []
    with open('arr171sec.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            secta.append(sect)
            sect += 5
            sec.append(double(row[1]))

    sectr = 0
    secr = []
    sectar = []
    with open('r171sec.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectar.append(sectr)
            sectr += 5
            secr.append(double(row[1]))

    acqt = 0
    acq = []
    acqta = []
    with open('arr171seco.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqta.append(acqt)
            acqt += 5
            acq.append(double(row[1]))

    acqtr = 0
    acqr = []
    acqtar = []
    with open('r171seco.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtar.append(acqtr)
            acqtr += 5
            acqr.append(double(row[1]))

    # fig, ax1 = plt.subplots()
    #
    # fig, [[ax1x, ax1y], [ax2x, ax2y], [ax3x, ax3y], [ax4x, ax4y]] = plt.subplots(nrows=4, ncols=2)
    #axt = ax1.twinx()
    # ##ax1.plot(t5, lamda5)

    pointC = (450, 340)
    pointD = (450, 179)

    coordsC = "data"
    coordsD = "data"
    conp = ConnectionPatch(xyA=pointC, xyB=pointD, coordsA=coordsC, coordsB=coordsD,
                           axesA=ax1, axesB=ax2,
                           shrinkB=1, color="green", linestyle="dotted")
    con2p = ConnectionPatch(xyA=pointD, xyB=pointD, coordsA=coordsC, coordsB=coordsD,
                            axesA=ax2, axesB=ax3,
                            shrinkB=1, color="green", linestyle="dotted")

    ax1.plot(secta, sec, label='Event Arrival rate ' )
    ax1.plot(sectar, secr, label='Maximum Consumption rate' )

    #ax1.set_frame_on(False)  # make it transparent
    #ax1.set_xticks([])
    #ax1.set_xticklabels([])

    ax2.plot(acqta, acq, label='sec µs')
    ax2.plot(acqtar, acqr, label='sec µs')
    #ax2.set_xticks([])

    ax3.plot(t15, lamda15, label='Issuer µs Arrival rate')
    ax3.plot(t1, lamda1, label='Maximum consumption rate \n (number of replicas)')
    #ax3.set_xticks([])

    #
    ax4.plot(lt, lv, 'r', label='end-to-end latency (ms)')
    # ax4.plot(tr1, lr1 ,'black',  label='latency 2nd replica (ms)')
    # ax4.plot(tr2, lr2, 'g' , label='latency 2nd replica (ms)')



    # #
    # #ax1.legend())
    #
    ax1.set_ylabel('Security µs', fontdict=font)
    ax2.set_ylabel('AcquirerBank', fontdict=font)
    ax3.set_ylabel('IssuerBank', fontdict=font)
    ax4.set_ylabel('End-to-end  \n latency (ms)', fontdict=font)

    ax2.add_artist(conp)
    ax3.add_artist(con2p)




    ax4.set_xlabel('Time (sec)', fontdict=font)
    # ax3.set_ylabel('Event Arrival Rate')
    # #
    # ax2.set_ylabel('End to end Latency (ms)')
    # # #
    # # plt.title('Graph Bin pack autoscaler')
    # ax3.legend()
    # # ax1.legend(bbox_to_anchor=(0.21, 0.7))
    # ax4.legend()
    # # #
    ax1.legend(fontsize='small')
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    graf()

