import matplotlib
import matplotlib.pyplot as plt
import math

import csv

from matplotlib.patches import ConnectionPatch
from numpy import double

# https://snapshots.raintank.io/dashboard/snapshot/tvr11TUPeg514X0g1V1M70z2biS9x9PL?orgId=2
def graf():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}

    matplotlib.rc('font', **font)
    sect = 0
    sec = []
    secta = []
    with open('ar.csv', 'r') as csvfile:
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
    with open('replica.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectar.append(sectr)
            sectr += 5
            secr.append(double(row[1]))

###########################End Acquirer
    acqt = 0
    acq = []
    acqta = []
    with open('ar.csv', 'r') as csvfile:
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
    with open('replica.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtar.append(acqtr)
            acqtr += 5
            acqr.append(double(row[1]))



    #########################################################
    tiss = []
    lamdaiss = []

    riss = []
    tissr = []

    tis = 0
    s1 = 0



    with open('ar.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            tiss.append(tis)
            tis += 5
            lamdaiss.append(double(row[1]))



    #####################################################
    tis=0
    with open('replica.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            tissr.append(tis)
            riss.append(double(row[1]))
            tis += 5



    tp = 0
    lt = []
    lv = []


    t=0
    with open('latency.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            # if t%15 == 0:
            #     tp +=5
            lt.append(t)
            lv.append(double(row[1]))
            t += 5



    ##########################################################


    fig, ax = plt.subplots(4,2, sharex=True)  # create the canvas for plotting


    ax[0,0].plot(secta, sec, label='Event Arrival rate ' )
    ax[0,0].plot(sectar, secr, label='Maximum Consumption rate' )

    ax[1,0].plot(acqta, acq, label='sec µs')
    ax[1,0].plot(acqtar, acqr, label='sec µs')
    ax[2,0].plot(tiss, lamdaiss, label='Issuer µs Arrival rate')
    ax[2,0].plot(tissr, riss, label='Maximum consumption rate \n (number of replicas)')

    ax[3,0].plot(lt, lv, 'r', label='latency (ms)')
    # ax4.plot(tr1, lr1, label='latency 2nd replica (ms)')
    # ax4.plot(tr2, lr2, 'g', label='latency 3nd replica (ms)')
    # ax4.plot(tr3, lr3, 'black', label='latency 4nd replica (ms)')

    ax[0,0].set_ylabel('Security µs', fontdict=font)
    ax[1,0].set_ylabel('MerchantBank µs', fontdict=font)
    ax[2,0].set_ylabel('ClientBank µs', fontdict=font)
    ax[3,0].set_ylabel('End-to-end  \n latency (ms)', fontdict=font)

    ax[3,0].set_xlabel('Time (sec)', fontdict=font)




    ax[0,0].legend(fontsize='x-small')
    #######################################################################################################################
    sectb = 0
    secb = []
    sectab = []
    with open('arb1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectab.append(sectb)
            sectb += 5
            secb.append(double(row[1]))

    sectrb = 0
    secrb = []
    sectarb = []
    with open('rb1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectarb.append(sectrb)
            sectrb += 5
            secrb.append(double(row[1]))

    ###########################End Acquirer
    acqtb = 0
    acqb = []
    acqtab = []
    with open('arb2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtab.append(acqtb)
            acqtb += 5
            acqb.append(double(row[1]))

    acqtrb = 0
    acqrb = []
    acqtarb = []
    with open('rb2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtarb.append(acqtrb)
            acqtrb += 5
            acqrb.append(double(row[1]))

    #########################################################
    tissb = []
    lamdaissb = []

    rissb = []
    tissrb = []

    tisb = 0
    s1b = 0

    with open('arb3.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            tissb.append(tisb)
            tisb += 5
            lamdaissb.append(double(row[1]))

    #####################################################
    tisb = 0
    with open('rb3.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            tissrb.append(tisb)
            rissb.append(double(row[1]))
            tisb += 5

    tpb = 0
    ltb = []
    lvb = []

    t = 0
    with open('latencyb.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            # if t%15 == 0:
            #     tp +=5
            ltb.append(t)
            lvb.append(double(row[1]))
            t += 5

    ##########################################################


    ax[0,1].plot(sectab, secb, label='Event Arrival rate ')
    ax[0,1].plot(sectarb, secrb, label='Maximum Consumption rate')

    ax[1,1].plot(acqtab, acqb, label='sec µs')
    ax[1,1].plot(acqtarb, acqrb, label='sec µs')
    ax[2,1].plot(tissb, lamdaissb, label='Issuer µs Arrival rate')
    ax[2,1].plot(tissrb, rissb, label='Maximum consumption rate \n (number of replicas)')

    ax[3,1].plot(ltb, lvb, 'r', label='latency (ms)')
    # ax4.plot(tr1, lr1, label='latency 2nd replica (ms)')
    # ax4.plot(tr2, lr2, 'g', label='latency 3nd replica (ms)')
    # ax4.plot(tr3, lr3, 'black', label='latency 4nd replica (ms)')

    # ax1.set_ylabel('Security µs', fontdict=font)
    # ax2.set_ylabel('MerchantBank µs', fontdict=font)
    # ax3.set_ylabel('ClientBank µs', fontdict=font)
   # ax[3,1].set_ylabel('End-to-end  \n latency (ms)', fontdict=font)
    ax[3, 1].set_xlabel('time (s)', fontdict=font)



    ax[0,1].legend(fontsize='x-small')

    ax[0, 0].set(title="Topological DAG autoscaler")
    ax[0, 1].set(title="Blind/Local DAG autoscaler")


    #######################################
    pointC = (129, 175)
    coordsC = "data"
    coordsD = "data"
    con = ConnectionPatch(xyA=pointC, xyB=pointC, coordsA=coordsC, coordsB=coordsD,
                          axesA=ax[1,0], axesB=ax[0,0],
                          shrinkB=1, color="green", linestyle="dotted")
    con2 = ConnectionPatch(xyA=pointC, xyB=pointC, coordsA=coordsC, coordsB=coordsD,
                          axesA=ax[2, 0], axesB=ax[1, 0],
                          shrinkB=1, color="green", linestyle="dotted")

    #ax[0,0].add_artist(con)
    ax[1,0].add_artist(con)
    ax[2,0].add_artist(con2)


    ####################################
    pointC = (122, 178)
    coordsC = "data"
    coordsD = "data"
    conp = ConnectionPatch(xyA=pointC, xyB=pointC, coordsA=coordsC, coordsB=coordsD,
                          axesA=ax[0,1], axesB=ax[1,1],
                          shrinkB=1, color="green", linestyle="dotted")
    con2p = ConnectionPatch(xyA=pointC, xyB=pointC, coordsA=coordsC, coordsB=coordsD,
                          axesA=ax[1, 1], axesB=ax[2, 1],
                          shrinkB=1, color="green", linestyle="dotted")

    #ax[0,0].add_artist(con)
    ax[1,0].add_artist(con)
    ax[2,0].add_artist(con2)
    ax[1, 1].add_artist(conp)
    ax[2, 1].add_artist(con2p)



    ######################################
    plt.tight_layout()
    plt.show()



    ########################################################################################################################




if __name__ == '__main__':
    graf()