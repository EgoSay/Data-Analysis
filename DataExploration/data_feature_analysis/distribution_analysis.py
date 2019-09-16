# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/28 上午10:33
# @IDE     : PyCharm
"""分布分析"""
import math
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
    # 方法一： 可以利用箱线图观察异常值，然后根据业务自定义异常值区间
    #     p = data.boxplot(return_type='dict')
    #     # filers标签为异常值，得到异常值
    #     y = p['fliers'][0].get_ydata()
    # 方法二： 直接根据3σ原则定义异常值区间

    df = pd.DataFrame(data)
    # 根据3σ原则异常值被定义为与平均值的偏差超过3倍标准差的值
    df = df[~((df - df.mean()).abs() > 3 * df.std())].dropna()

    # 求极差=最大值 - 最小值
    data_range = df.max()[0] - df.min()[0]
    # 分组， 取组距为500， 划分区间数为7
    group_num = math.ceil(data_range / 500)
    # 决定分点， 即分布区间, 最大值为4065.2, 所以取区间为0～4500， 9个区间
    point_list = [0 + i * 500 for i in range(group_num + 2)]
    # plt.legend()

    # 绘制频次分布直方图
    plt.xlim(point_list[0], point_list[-1])
    plt.title(r"季度销售额的频率分布直方图，$\sigma={0}$".format(df.std()[0]))
    plt.xlabel('日销售额/元')
    plt.ylabel('频率')
    # draw_data = sorted([v[0] for v in df.values.tolist()])
    draw_data = [v[0] for v in df.values.tolist()]
    n_val, bins, patches = plt.hist(
        draw_data, point_list, density=False, stacked=True)
    fracs = n_val / n_val.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    for x, y, thisfrac, thispatch in zip(bins, n_val, fracs, patches):
        # 字体上边文字
        plt.text(x + 250, y + 1.5, y, ha='center', va='center', fontsize=12)
        # plt.text(x + bins_interval / 2, y + 0.25, '%.2f' % y, ha='center', va='top')
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.show()


def distribution_analysis_of_qualitative_data(data):
    """
    定性数据的分布分析
    :param data: Pandas读取的数据源
    :return:
    """
    # 定义字典存储每个菜品的销售量
    sale_volume = dict()
    dish_types = data.columns.tolist()
    df = pd.DataFrame(data)
    for dish in dish_types:
        sale_volume.setdefault(dish, df[dish].sum())
    labels = [k + "销售额为:" + str(v) for k, v in sale_volume.items()]
    _, ax = plt.subplots()
    ax.pie(
        list(
            sale_volume.values()),
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
    ax.set_title("这段时间内每个菜品的销售量分布")
    plt.show()


if __name__ == '__main__':
    # 读取数据， 指定 "日期列" 为索引列
    # 定量数据
    quantitative_data = pd.read_excel('../data/catering_sale.xls', index_col=u'日期')
    distribution_analysis_of_quantitative_data(quantitative_data)

    # 定性数据
    qualitative_data = pd.read_excel('../data/catering_sale_all.xls', index_col=u'日期')
    distribution_analysis_of_qualitative_data(qualitative_data)
