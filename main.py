import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import walk


def main():
    mypath = 'data'

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

    # print(f'Naplnene elements: {elements}')
    # print(f'Naplnene pressure: {pressure}')
    # print(f'Naplnene temperature: {temp_range}')
    # print(f'Min temperature: {temp_min}')
    # print(f'Max temperature: {temp_max}')
    # print(f'Pressure: {press}, type of press: {type(press[0])}')

    # odtialto zacneme slucku vypoctu pre rozne vstupne data
    file = dirpath + '/' + filenames[0]
    data = pd.read_csv(file,  sep='\t+', engine='python', index_col=False)  # , delimiter='\t' , delim_whitespace=True
    print(data.columns)
    print(data.head())

    x = data['Temperature (K)']
    y = data['Density (mol/l)']

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
