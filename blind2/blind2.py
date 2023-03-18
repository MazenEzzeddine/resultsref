import matplotlib
import matplotlib.pyplot as plt
import math

import csv

from numpy import double

# https://snapshots.raintank.io/dashboard/snapshot/tvr11TUPeg514X0g1V1M70z2biS9x9PL?orgId=2
def graf():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}

    matplotlib.rc('font', **font)
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
    tissrb=[]



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
    tisb=0
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


    t=0
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


    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True)  # create the canvas for plotting


    ax1.plot(sectab, secb, label='Event Arrival rate ' )
    ax1.plot(sectarb, secrb, label='Maximum Consumption rate' )

    ax2.plot(acqtab, acqb, label='sec µs')
    ax2.plot(acqtarb, acqrb, label='sec µs')
    ax3.plot(tissb, lamdaissb, label='Issuer µs Arrival rate')
    ax3.plot(tissrb, rissb, label='Maximum consumption rate \n (number of replicas)')

    ax4.plot(ltb, lvb, 'r', label='latency (ms)')
    # ax4.plot(tr1, lr1, label='latency 2nd replica (ms)')
    # ax4.plot(tr2, lr2, 'g', label='latency 3nd replica (ms)')
    # ax4.plot(tr3, lr3, 'black', label='latency 4nd replica (ms)')

    ax1.set_ylabel('Security µs', fontdict=font)
    ax2.set_ylabel('MerchantBank µs', fontdict=font)
    ax3.set_ylabel('ClientBank µs', fontdict=font)
    ax4.set_ylabel('End-to-end  \n latency (ms)', fontdict=font)

    ax4.set_xlabel('Time (sec)', fontdict=font)




    ax1.legend(fontsize='x-small')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    graf()