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
    sect = 0
    sec = []
    secta = []
    with open('arn177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            secta.append(sect)
            sect += 15
            sec.append(double(row[1]))

    sectr = 0
    secr = []
    sectar = []
    with open('rn177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            sectar.append(sectr)
            sectr += 15
            secr.append(double(row[1]))

###################################################################################

    acqt = 0
    acq = []
    acqta = []
    with open('acqn1777.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqta.append(acqt)
            acqt += 15
            acq.append(double(row[1]))

    acqtr = 0
    acqr = []
    acqtar = []
    with open('acqr177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            acqtar.append(acqtr)
            acqtr += 15
            acqr.append(double(row[1]))



    #########################################################
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s1 = 0



    with open('arissuer177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 15
            lamda15.append(double(row[1]))

    t = 0
    tp =0
    lt = []
    lv = []


    #####################################################


    with open('riss177.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            lamda1.append(double(row[1]))
            s1 += 15





    t=0
    with open('l1y.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:

            if t%15 == 0:
                tp +=5
                lt.append(tp)
                lv.append(double(row[1]))
            t += 15



    ##########################################################


    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True)  # create the canvas for plotting


    ax1.plot(secta, sec, label='Event Arrival rate ' )
    ax1.plot(sectar, secr, label='Maximum Consumption rate' )

    ax2.plot(acqta, acq, label='sec µs')
    ax2.plot(acqtar, acqr, label='sec µs')
    ax3.plot(t15, lamda15, label='Issuer µs Arrival rate')
    ax3.plot(t1, lamda1, label='Maximum consumption rate \n (number of replicas)')

    ax4.plot(lt, lv, 'r', label='latency (ms)')
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