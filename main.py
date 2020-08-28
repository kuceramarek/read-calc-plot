# Simple template for data read and create charts.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import walk


def main():
    mypath = 'data'

    # Go trought the directory and print dirpath, dirname and filenames
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break

    print(f'Dirpath: {dirpath}')
    print(f'Zoznam suborov: {filenames}')
    print(f'Zoznam adresarov: {dirnames}')

    elements = []
    pressure = []
    temp_max = []
    temp_min = []
    temp_range = []
    press = []

    # Split the filename to the separate words.
    for item in filenames:
        if item.endswith('.txt'):
            item = item[:-4]
        k = item.split('_')
        elements.append(k[0])
        pressure.append(k[1])
        temp_range.append(k[2])

    for temp in temp_range:
        if temp.endswith('K'):
            temp = temp[:-1]
        k = temp.split('-')
        temp_min.append(k[0])
        temp_max.append(k[1])

    for p in pressure:
        if p.endswith('bar'):
            p = p[:-3]
        press.append(int(p[0]))


    # Read the data from data folder. Return DataFrame
    file = dirpath + '/' + filenames[0]
    data = pd.read_csv(file,  sep='\t+', engine='python', index_col=False)  # , delimiter='\t' , delim_whitespace=True
    print(data.columns)
    print(data.head())

    x = data['Temperature (K)']
    y = data['Density (mol/l)']

    # Create the figure from data.
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, '-b', label='Temperature', linewidth=0.8)

    ax.set(title='Example')
    ax.set_ylabel('Temperature [°C]', fontsize=10)
    ax.set_xlabel('Time [s]', fontsize=10)
    ax.legend(loc='lower left', fontsize=8)

    ax.yaxis.set_ticks_position('both')
    ax.tick_params(axis='y', labelright=True, labelsize=8, labelcolor='red')
    ax.grid(True, linestyle='--', linewidth=0.4)
    ax.tick_params(axis='x', labelsize=8)

    # ax.set_xscale("log", nonposx='clip')
    # ax.set_yscale("log", nonposy='clip')

    filename = 'output_' + filenames[0] + '.pdf'
    plt.savefig(filename)
    plt.show()


if __name__ == '__main__':
    main()
