### - 数据质量分析
- [缺失值分析](data_quality_analysis/missing_value.md)
- [异常值分析](data_quality_analysis/outlier_analysis.py)
- [一致性分析]()
### - 数据特征分析
- [分布分析](data_feature_analysis/distribution_analysis.py)
    1. 定量数据的分布分析
        >一般按照以下步骤进行：<p>
        1）求极差<p>
        2）决定组距与组数<p>
        3）决定分点<p>
        4）列出频率分布表<p>
        5）绘制频率分布直方图<p>
    2. 定性数据的分布分析
        >对于定性变量，常常根据变量的分类类型来分组，可以采用饼状图和条形图来描述展现
- [对比分析](data_feature_analysis/comparative_analysis.py)
- [统计量分析](data_feature_analysis/statistics_analysis.py)
    >用统计指标对定量数据进行统计描述，常从集中趋势和离中趋势两个方面进行分析
    1. 平均水平的指标是对集中趋势的度量，使用最广泛的是均值和中位数
        ```
        1)均值
        均值是所有数据的平均值,主要问题是对极值很敏感，可以使用截断均值或者中位数来度量
        截断均值是去掉高，低极端值之后的平均数
        2）中位数
        中位数是将一组观察值按从小到大的顺序排列，位于中间的那个数
        3）众数
        众数是指数据集中出现最频繁的值
        ```
    2. 离中趋势度量
        
        >1）极差<p>
        极差 = 最大值 - 最小值，<p>
        极差对数据集的极端值非常敏感， 并且忽略了位于最大值最小值之间的数据的分布情况<p>
        2）标准差<p>
        标准差度量数据偏离均值的程度， 计算公式为
        ![公式](images/标准差.gif)<p>
        3）变异系数<p>
        变异系数度量标准差相对于均值的离中趋势<p>
        4）四分位数间距<p>
        将所有数值由小到大排列并分成四等份，位于第一个分割点的是上四分位数，
        位于第二个分割点的是中位数，位于第三个分割点的数是下四分位数<p>
        四分数数间距，是上四分数与下四分数之差，其值越大，说明数据的变异程度越大
- [周期性分析](data_feature_analysis/periodic_analysis.py)
    >周期性分析是探索某个变量是否随着时间变化而呈现出某种周期变化趋势
- [贡献度分析](data_feature_analysis/contribution_analysis.py)
    >又称帕累托分析， 原理是帕累托法则， 即我们熟知的二八定律<p>
    帕累托法则: [百度百科](https://dwz.cn/YRTb7MUr)
- [相关性分析](data_feature_analysis/correlation_analysis.py)
    >相关性分析: 分析连续变量之间线性相关程度的强弱<p>
    判断两个变量是否具有线性相关关系最直观的方法是直接绘制散点图<p>
    考察多个变量间的相关关系时， 可以绘制散点图矩阵
    
    >计算相关系数：[链接](https://blog.csdn.net/zhaozhn5/article/details/78392220)
    > 1. Pearson相关系数: [维基百科](https://dwz.cn/af4FsnpN)
    > 2. Spearman轶相关系数: [百度百科](https://dwz.cn/iYAvJGyU)
### - [Python主要数据探索函数](Python主要数据探索函数.md)