import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import HostAxes, ParasiteAxes


def multi_parasite_axes(x, data, total):
    # color list
    color_list = ['red', 'green', 'orange', 'deepskyblue', 'black', 'navy', 'pink', 'aqua']

    # figure
    fig = plt.figure(figsize=[8, 4])
    # main axes location & size
    ax_main = HostAxes(fig, [0.0, 0.0, 0.6, 0.8])
    ax_main.set_ylabel('Oil Flow(L/min)')
    ax_main.set_xlabel('Inner Ring (rpm)')

    ax_list = []
    _axis = []
    for i in range(len(total)):
        ax_list.append(ParasiteAxes(ax_main, sharex=ax_main))
        ax_main.parasites.append(ax_list[i])
        ax_list[i].set_ylabel('Percentage(%)')
        if i:
            _axis.append(ax_list[i].get_grid_helper().new_fixed_axis)
            ax_list[i].axis[str(i)] = _axis[i-1](loc='right', axes=ax_list[i], offset=(60*i, 0))
            ax_list[i].axis[str(i)].label.set_color(color_list[i])
            ax_list[i].axis[str(i)].major_ticks.set_color(color_list[i])
            ax_list[i].axis[str(i)].major_ticklabels.set_color(color_list[i])
            ax_list[i].axis[str(i)].line.set_color(color_list[i])
        else:
            ax_list[i].axis['right'].label.set_color(color_list[i])
            ax_list[i].axis['right'].major_ticks.set_color(color_list[i])
            ax_list[i].axis['right'].major_ticklabels.set_color(color_list[i])
            ax_list[i].axis['right'].line.set_color(color_list[i])

    # invisible right axis of ax_cof
    ax_main.axis['right'].set_visible(False)
    ax_main.axis['top'].set_visible(False)
    ax_list[0].axis['right'].set_visible(True)
    ax_list[0].axis['right'].major_ticklabels.set_visible(True)
    ax_list[0].axis['right'].label.set_visible(True)

    # add axes to fig
    fig.add_axes(ax_main)

    # plot
    for i in range(len(data)):
        ax_main.plot(x, data[i], label='line' + str(i), color=color_list[i])

    # set ylim
    min_level = int(np.min(np.array(data)))
    max_level = round(np.max(np.array(data)))
    ax_main.set_ylim(min_level-0.5, max_level+0.5)
    for i in range(len(total)):
        ax_list[i].set_ylim(100 * (min_level-0.5)/total[i], 100 * (max_level+0.5)/total[i])
        # ax_list[i].set_yticks(np.round(np.linspace(100 * min_level/total[i], 100, 5)))
        y_ticks = [100 * (min_level-0.5) / total[i]]
        for j in np.linspace(0, 100, 11):
            if j > y_ticks[0] + 5:
                y_ticks.append(j)
        ax_list[i].set_yticks(np.round(np.array(y_ticks)))

    # legend
    ax_main.legend()

    plt.grid(axis='y')
    plt.savefig('fig_func.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    np.random.seed(2020)
    # rand_data
    rand_data = np.random.rand(4, 30)
    arr_0 = list(rand_data[:][0] * 1 + 4)
    arr_1 = list(rand_data[:][1] * 2 + 4)
    arr_2 = list(rand_data[:][2] * 3 + 4)
    arr_3 = list(rand_data[:][3] * 5 + 4)
    rpms = np.linspace(1600, 2500, len(arr_0))
    multi_parasite_axes(x=rpms, data=[arr_0, arr_1, arr_2, arr_3], total=[5, 6, 7, 9])
