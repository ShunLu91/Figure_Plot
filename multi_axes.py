import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import HostAxes, ParasiteAxes

# data
np.random.seed(2020)
# data = np.ones([20, 5])
data = np.random.rand(5, 30)
arr_0 = list(data[:][0] * 1 + 10)
arr_1 = list(data[:][1] * 2 + 10)
arr_2 = list(data[:][2] * 3 + 10)
arr_3 = list(data[:][3] * 4 + 10)
arr_4 = list(data[:][4] * 5 + 10)
rpms = np.linspace(0, 2500, len(arr_0))

# figure
fig = plt.figure(figsize=[8, 4])
ax_cof = HostAxes(fig, [0.1, 0.1, 0.7, 0.8])  # 用[left, bottom, weight, height]的方式定义axes，0 <= l,b,w,h <= 1

# parasite addtional axes, share x
ax_temp = ParasiteAxes(ax_cof, sharex=ax_cof)
ax_load = ParasiteAxes(ax_cof, sharex=ax_cof)
ax_cp = ParasiteAxes(ax_cof, sharex=ax_cof)
ax_wear = ParasiteAxes(ax_cof, sharex=ax_cof)

# append axes
ax_cof.parasites.append(ax_temp)
ax_cof.parasites.append(ax_load)
ax_cof.parasites.append(ax_cp)
ax_cof.parasites.append(ax_wear)

# invisible right axis of ax_cof
ax_cof.axis['right'].set_visible(False)
ax_cof.axis['top'].set_visible(False)
ax_temp.axis['right'].set_visible(True)
ax_temp.axis['right'].major_ticklabels.set_visible(True)
ax_temp.axis['right'].label.set_visible(True)

# set label for axis
ax_cof.set_ylabel('Oil Flow(L/min)')
ax_cof.set_xlabel('Inner Ring (rpm)')
ax_temp.set_ylabel('Line0_Percentage(%)')
ax_load.set_ylabel('Line1_Percentage(%)')
ax_cp.set_ylabel('Line2_Percentage(%)')
ax_wear.set_ylabel('Line3_Percentage(%)')

load_axisline = ax_load.get_grid_helper().new_fixed_axis
cp_axisline = ax_cp.get_grid_helper().new_fixed_axis
wear_axisline = ax_wear.get_grid_helper().new_fixed_axis

ax_load.axis['right2'] = load_axisline(loc='right', axes=ax_load, offset=(40, 0))
ax_cp.axis['right3'] = cp_axisline(loc='right', axes=ax_cp, offset=(80, 0))
ax_wear.axis['right4'] = wear_axisline(loc='right', axes=ax_wear, offset=(120, 0))

fig.add_axes(ax_cof)

# curve_cof, = ax_cof.plot(rpms, arr_0, label="Line0", color='black')
curve_temp, = ax_cof.plot(rpms, arr_1, label="Line1", color='red')
curve_load, = ax_cof.plot(rpms, arr_2, label="Line2", color='green')
curve_cp, = ax_cof.plot(rpms, arr_3, label="Line3", color='orange')
curve_wear, = ax_cof.plot(rpms, arr_4, label="Line4", color='blue')

#ax_cof.set_xlim(0, 2)
ax_cof.set_ylim(10, 15)
ax_temp.set_ylim(0, 1*100)
ax_temp.set_yticks((0, 20, 40, 60, 80, 100))
ax_load.set_ylim(0, 1.25*100)
ax_load.set_yticks((0, 20, 40, 60, 80, 100))
ax_cp.set_ylim(0, 5/3*100)
ax_cp.set_yticks((0, 20, 40, 60, 80, 100))
ax_wear.set_ylim(0, 2.5*100)
ax_wear.set_yticks((0, 20, 40, 60, 80, 100))
# plt.yticks(ax_wear.get_yticks(), ('a', 'b', 'c'))

ax_cof.legend()

# 轴名称，刻度值的颜色
# ax_cof.axis['left'].label.set_color(ax_cof.get_color())
ax_temp.axis['right'].label.set_color('red')
ax_load.axis['right2'].label.set_color('green')
ax_cp.axis['right3'].label.set_color('orange')
ax_wear.axis['right4'].label.set_color('blue')

ax_temp.axis['right'].major_ticks.set_color('red')
ax_load.axis['right2'].major_ticks.set_color('green')
ax_cp.axis['right3'].major_ticks.set_color('orange')
ax_wear.axis['right4'].major_ticks.set_color('blue')

ax_temp.axis['right'].major_ticklabels.set_color('red')
ax_load.axis['right2'].major_ticklabels.set_color('green')
ax_cp.axis['right3'].major_ticklabels.set_color('orange')
ax_wear.axis['right4'].major_ticklabels.set_color('blue')

ax_temp.axis['right'].line.set_color('red')
ax_load.axis['right2'].line.set_color('green')
ax_cp.axis['right3'].line.set_color('orange')
ax_wear.axis['right4'].line.set_color('blue')

# plt.tight_layout()
plt.grid(axis='y')
plt.savefig('fig.png', bbox_inches='tight')
plt.show()
