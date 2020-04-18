import argparse as ap
import os
import matplotlib.pyplot as plt
import numpy as np

# Globals
x_done = False

def main():
    parser = ap.ArgumentParser(description='Take in Config file names')
    parser.add_argument('yaxis_column', type=int, help='Column from out file that gets plotted on y-axis')
    parser.add_argument('-n', '--hbm_none_fName', help='Name of config file for HBM simulation with no ECC')
    parser.add_argument('-b1s', '--hbm_bch1s_fName', help='Name of config file for HBM simulation with BCH1 ECC and scrubbing')
    parser.add_argument('-b1ns', '--hbm_bch1ns_fName', help='Name of config file for HBM simulation with BCH1 ECC and no scrubbing')
    parser.add_argument('-b6s', '--hbm_bch6s_fName', help='Name of config file for HBM simulation with BCH6 ECC and scrubbing')
    parser.add_argument('-b6ns', '--hbm_bch6ns_fName', help='Name of config file for HBM simulation with BCH6 ECC and no scrubbing')
    parser.add_argument('-rs', '--hbm_RSs_fName', help='Name of config file for HBM simulation with Reed Solomon ECC and scrubbing')
    parser.add_argument('-rns', '--hbm_RSns_fName', help='Name of config file for HBM simulation with Reed Solomon ECC and no scrubbing')
    args = parser.parse_args()

    # booleans to determine which simulations run
    # can be expanded later to include other ECC schemes
    HBM_none = False
    HBM_BCH1s = False
    HBM_BCH1ns = False
    HBM_BCH6s = False
    HBM_BCH6ns = False
    HBM_RSs = False
    HBM_RSns = False
    column = 1

    # run simulation for config files
    for name in vars(args):
        if name != None:
            if(name == 'hbm_none_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_none_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_none_out.txt')
                HBM_none = True
            elif(name == 'hbm_bch1s_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH1s_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH1s_out.txt')
                HBM_BCH1s = True
            elif (name == 'hbm_bch1ns_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH1ns_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH1ns_out.txt')
                HBM_BCH1ns = True
            elif (name == 'hbm_bch6s_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH6s_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH6s_out.txt')
                HBM_BCH6s = True
            elif (name == 'hbm_bch6ns_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH6ns_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_BCH6ns_out.txt')
                HBM_BCH6ns = True
            elif(name == 'hbm_RSs_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_RSs_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_RSs_out.txt')
                HBM_RSs = True
            elif (name == 'hbm_RSns_fName' and getattr(args, name) != None):
                print('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_RSns_out.txt')
                os.system('./faultsim --configfile configs/' + str(getattr(args, name)) + ' --outfile HBM_RSns_out.txt')
                HBM_RSns = True
            elif(name == 'yaxis_column'):
                print(str(getattr(args, name)))
                column = int(getattr(args, name))
            else:
                print('No simulation run for ' + str(name))

    x = []
    y_none = []
    y_BCH1s = []
    y_BCH1ns = []
    y_BCH6s = []
    y_BCH6ns = []
    y_RSs = []
    y_RSns = []

    if(HBM_none):
        read_results(x, y_none, 'HBM_none_out.txt', column)
        y_none = np.array(y_none)
    if(HBM_BCH1s):
        read_results(x, y_BCH1s, 'HBM_BCH1s_out.txt', column)
        y_BCH1s = np.array(y_BCH1s)
    if (HBM_BCH1ns):
        read_results(x, y_BCH1ns, 'HBM_BCH1ns_out.txt', column)
        y_BCH1ns = np.array(y_BCH1ns)
    if (HBM_BCH6s):
        read_results(x, y_BCH6s, 'HBM_BCH6s_out.txt', column)
        y_BCH6s = np.array(y_BCH6s)
    if (HBM_BCH6ns):
        read_results(x, y_BCH6ns, 'HBM_BCH6ns_out.txt', column)
        y_BCH6ns = np.array(y_BCH6ns)
    if(HBM_RSs):
        read_results(x, y_RSs, 'HBM_RSs_out.txt', column)
        y_RSs = np.array(y_RSs)
    if (HBM_RSns):
        read_results(x, y_RSns, 'HBM_RSns_out.txt', column)
        y_RSns = np.array(y_RSns)

    #x = np.array(x)
    if(HBM_none):
        plt.plot(x, y_none, color='red', label='HBM_none')
    if(HBM_BCH1s):
        plt.plot(x, y_BCH1s, color='blue', label='HBM_BCH1s')
    if (HBM_BCH1ns):
        plt.plot(x, y_BCH1ns, color='yellow', label='HBM_BCH1ns')
    if (HBM_BCH6s):
        plt.plot(x, y_BCH6s, color='black', label='HBM_BCH6s')
    if (HBM_BCH6ns):
        plt.plot(x, y_BCH6ns, color='brown', label='HBM_BCH6ns')
    if(HBM_RSs):
        plt.plot(x, y_RSs, color='green', label='HBM_RSs')
    if (HBM_RSns):
        plt.plot(x, y_RSns, color='violet', label='HBM_RSns')

    yaxis_label = ''
    if(column == 1):
        yaxis_label = 'FAULT'
    elif(column == 2):
        yaxis_label = 'FAULT - CUMU'
    elif(column == 3):
        yaxis_label = 'P(FAULT)'
    elif(column == 4):
        yaxis_label = 'P(FAULT - CUMU)'
    elif(column == 5):
        yaxis_label = 'UNCORRECTABLE'
    elif(column == 6):
        yaxis_label = 'UNCORRECTABLE - CUMU'
    elif(column == 7):
        yaxis_label = 'P(UNCORRECTABLE)'
    elif(column == 8):
        yaxis_label = 'P(UNCORRECTABLE - CUMU)'
    elif(column == 9):
        yaxis_label = 'UNDETECTABLE'
    elif(column == 10):
        yaxis_label = 'UNDETECTABLE - CUMU'
    elif(column == 11):
        yaxis_label = 'P(UNDETECTABLE)'
    elif(column == 12):
        yaxis_label = 'P(UNDETECTABLE - CUMU)'
    else:
        yaxis_label = ''

    plt.legend(loc='upper left')
    plt.title("FaultSim Results", fontsize=16, fontweight='bold')
    plt.xlabel("Weeks")
    plt.ylabel(yaxis_label)
    plt.show()


def read_results(x, y, fName, column):
    global x_done
    with open(fName, 'r') as f:
        f.readline()  # read the first line that holds the column names
        lines = f.readlines()
        for line in lines:
            if x_done == False:
                x.append(int(line.split(',')[0]))  # x is set to weeks
            y.append(float(line.split(',')[column]))  # y is set to P(Uncorrectable)
        x_done = True


if __name__ == "__main__":
    main()