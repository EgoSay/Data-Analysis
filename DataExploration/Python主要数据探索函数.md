### Pandas主要统计特征函数

|方法名|函数功能|
|:-:|:-:|
|sum()|计算数据样本的总和（按列计算）|
|mean()|计算数据样本的算数平均数|
|var()|计算数据样本的方差|
|std()|计算数据样本的标准差|
|corr()|计算数据样本的Spearman(Pearson)相关系数矩阵|
|cov()|计算数据样本的协方差矩阵|
|skew()|样本值的偏度（三阶矩）|
|kurt()|样本值的峰度（四阶矩）|
|describe()|给出样本的基本描述（基本统计量如均值、标注差等）|


### Pandas累积统计特征函数

|方法名|函数功能|
|:-:|:-:|
|cumsum(`n`)|依次给出前n个数的和|
|cumprod(`n`)|依次给出前n个数的积|
|cummax(`n`)|依次给出前n个数的最大值|
|cummin(`n`)|依次给出前n个数的最小值|


### Pandas滚动统计特征函数

|方法名|函数功能|
|:-:|:-:|
|rolling_sum()|计算数据样本的总和（按列计算）|
|rolling_mean()|数据样本的算数平均数|
|rolling_var()|计算数据样本的方差|
|rolling_std()|计算数据样本的标准差|
|rolling_corr()|计算数据样本的Spearman(Pearson)相关系数矩阵|
|rolling_cov()|计算数据样本的协方差矩阵|
|rolling_skew()|样本值的偏度（三阶矩）|
|rolling_kurt()|样本的峰度（四阶矩）|

调用方法：pd.rolling_mean(D, k)，意思是每k列计算依次均值，滚动计算。


### Pandas绘图函数
Pandas 基于 Matplotlib并对某些命令进行了简化，因此作图通常是 Matplotlib 和 Pandas 相互结合着使用。

**Pandas主要统计作图函数**

|函数名|函数功能|
|:-:|:-:|
|plot()|绘制线性二维图，折线图|
|pie()|绘制饼形图|
|hist()|绘制二维条形直方图，可显示数据的分配情况|
|boxplot()|绘制样本数据的箱型图|
|plot(logy = True)|绘制y轴的对数图形|
|plot(yerr = error)|绘制误差条形图|
