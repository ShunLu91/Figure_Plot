import bezier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


def rang(x, y, jump):
    while x < y:
        yield x
        x += jump


if __name__ == '__main__':
    # 读取原始数据
    data = pd.read_excel('data/data2.xlsx').values
    split = 200
    x = data[:, 1]
    y = data[:, 2]
    x1, x2 = data[0:split, 1], data[split:, 1]
    y1, y2 = data[0:split, 2], data[split:, 2]

    x_circle = data[150:, 3]
    y_circle = data[150:, 4]

    # 1th
    z1 = np.polyfit(x, y, 20)
    p1 = np.poly1d(z1)
    # print(p1)
    fit1 = p1(x[:260])

    # 2th
    z2 = np.polyfit(x2, y2, 5)
    p2 = np.poly1d(z2)
    # print(p2)
    fit2 = p2(x[260:])
    print(fit1.shape, fit2.shape)
    # stack
    fit_value = np.hstack((fit1, fit2))

    # bezier
    inter_val = np.linspace(0, 100, 6, dtype='int')
    print(inter_val)
    print(x2.shape)
    x3 = x2[inter_val]
    y3 = y2[inter_val]
    print(x3)
    a = np.array([x3, y3])
    print(a)
    curve = bezier.Curve(a, degree=5)
    fit3 = curve.evaluate_multi(x[260:]/30)[0]
    print(fit3)
    fit_value2 = np.hstack((fit1, fit3))

    # # 3th
    # z3 = np.polyfit(x2, y2, 4)
    # p3 = np.poly1d(z3)
    # # print(p2)
    # fit3 = p3(x[260:])
    # fit_value2 = np.hstack((fit1, fit3))

    # 65 line
    k = -0.46630766 * x

    # 构造参数方程表示的圆
    # theta = np.arange(0, 2 * np.pi, 0.01)
    # r = p1(0)
    # a = r * np.cos(theta)
    # b = r * np.sin(theta)
    # b = -abs(b)

    # # 检查交点
    # for i in range(0, 301):
    #     for j in range(0, theta.shape[0]):
    #         if round(x[i], 3) == round(a[j], 3):
    #             if (abs(p1(x[i])) - abs(b[j])) < 0:
    #                 print('intersection:', x[i])
    #                 print(yvals[i])
    #                 print(b[j])

    # 坐标轴移到中间
    fig = plt.figure('Sine Wave', (10, 8))
    ax = axisartist.Subplot(fig, 1, 1, 1)
    fig.add_axes(ax)
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0, 0)
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    ax.axis["x"].set_axis_direction('top')
    ax.axis["y"].set_axis_direction('left')

    # plot
    plot0 = plt.plot(x, k, color='y', label='65 degree line')
    plot1 = plt.plot(x, y, color='g', label='data')
    plot2 = plt.plot(x, fit_value, color='r', label='polyfit values')
    plot2_1 = plt.plot(x, fit_value2, color='orange', label='bezier')
    plot3 = plt.plot(x_circle, y_circle, color='b', label='circle benchmark')
    plt.savefig("filename.png")
    fig.legend(loc='lower left')
    plt.show()
