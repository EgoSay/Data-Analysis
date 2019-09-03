#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/28 上午10:33
# @IDE     : PyCharm
"""分布分析"""
import random

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors


def distribution_analysis_of_quantitative_data(data):
    """
    定量数据的分布分析
    :param data: Pandas读取的数据源
    :return:
    """
    # pandas清洗异常值以及空值
    """
    方法一： 可以利用箱线图观察异常值，然后根据业务自定义异常值区间
        p = data.boxplot(return_type='dict')
        # filers标签为异常值，得到异常值
        y = p['fliers'][0].get_ydata()
    
    方法二： 直接根据3σ原则定义异常值区间 
    """
    df = pd.DataFrame(data)
    # 根据3σ原则异常值被定义为与平均值的偏差超过3倍标准差的值
    df = df[~((df - df.mean()).abs() > 3 * df.std())].dropna()

    # 求极差=最大值 - 最小值
    data_range = df.max()[0] - df.min()[0]
    # 分组， 取组距为500
    group_num = int(data_range / 500) + 1
    # 决定分点， 即分布区间
    point_list = [0 + i * 500 for i in range(group_num + 2)]
    # plt.legend()
    # TODO 调整优化图表效果
    # 绘制频次分布直方图
    plt.xlim(point_list[0], point_list[-1])
    plt.title("季度销售额的频率分布直方图，$\sigma={0}$".format(df.std()[0]))
    plt.xlabel('日销售额/元')
    plt.ylabel('频率')
    # draw_data = sorted([v[0] for v in df.values.tolist()])
    draw_data = [v[0] for v in df.values.tolist()]
    n_val, bins, patches = plt.hist(draw_data, point_list, density=False, stacked=True)
    fracs = n_val / n_val.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    for x, y, thisfrac, thispatch in zip(bins, n_val, fracs, patches):
        # 字体上边文字
        plt.text(x + 250, y + 1.5, y, ha='center', va='center', fontsize=12)
        # plt.text(x + bins_interval / 2, y + 0.25, '%.2f' % y, ha='center', va='top')
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    #
    plt.show()


def distribution_analysis_of_qualitative_data(df):
    """
    定性数据的分布分析
    :param data:
    :return:
    """


if __name__ == '__main__':
    # 读取数据， 指定 "日期列" 为索引列
    catering_sale = '../data/catering_sale.xls'
    data = pd.read_excel(catering_sale, index_col=u'日期')
    distribution_analysis_of_quantitative_data(data)