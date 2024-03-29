# 缺失值分析
>参考自CSDN博主「BYR_jiandong」的原创文章[
数据分析中的缺失值处理](https://blog.csdn.net/lujiandong1/article/details/526547036)

### 造成缺失值的原因
- 信息暂时无法获取。例如在医疗数据库中，并非所有病人的所有临床检验结果都能在给定的时间内得到，就致使一部分属性值空缺出来。
- 信息被遗漏。可能是因为输入时认为不重要、忘记填写了或对数据理解错误而遗漏，也可能是由于数据采集设备的故障、存储介质的故障、传输媒体的故障、一些人为因素等原因而丢失。
- 有些对象的某个或某些属性是不可用的。如一个未婚者的配偶姓名、一个儿童的固定收入状况等。
- 有些信息（被认为）是不重要的。如一个属性的取值与给定语境是无关。
获取这些信息的代价太大。
- 系统实时性能要求较高。即要求得到这些信息前迅速做出判断或决策。
 
### 对缺失值的处理要具体问题具体分析
- “年收入”：商品推荐场景下填充平均值，借贷额度场景下填充最小值；
- “行为时间点”：填充众数；
- “价格”：商品推荐场景下填充最小值，商品匹配场景下填充平均值；
- “人体寿命”：保险费用估计场景下填充最大值，人口估计场景下填充平均值；
- “驾龄”：没有填写这一项的用户可能是没有车，为它填充为0较为合理；
- ”本科毕业时间”：没有填写这一项的用户可能是没有上大学，为它填充正无穷比较合理；
- “婚姻状态”：没有填写这一项的用户可能对自己的隐私比较敏感，应单独设为一个分类，如已婚1、未婚0、未填-1。

### 缺失的类型
>将数据集中不含缺失值的变量称为完全变量，数据集中含有缺失值的变量称为不完全变量

>从缺失的分布来将缺失可以分为完全随机缺失，随机缺失和完全非随机缺失

- 完全随机缺失（missing completely at random,MCAR）：指的是数据的缺失是完全随机的，不依赖于任何不完全变量或完全变量，不影响样本的无偏性。如家庭地址缺失。
- 随机缺失(missing at random,MAR)：指的是数据的缺失不是完全随机的，即该类数据的缺失依赖于其他完全变量。例如财务数据缺失情况与企业的大小有关。
- 非随机缺失(missing not at random,MNAR)：指的是数据的缺失与不完全变量自身的取值有关。如高收入人群的不原意提供家庭收入。
 
### 缺失数据的处理方法
#### 删除元组
>说明：将存在遗漏信息属性值的对象（元组，记录）删除，从而得到一个完备的信息表\
优点：简单易行，在对象有多个属性缺失值、被删除的含缺失值的对象与初始数据集的数据量相比非常小的情况下非常有效\
不足：当缺失数据所占比例较大，特别当遗漏数据非随机分布时，这种方法可能导致数据发生偏离，从而引出错误的结论。



#### 数据补齐
>说明：用一定的值去填充空值，从而使信息表完备化。通常基于统计学原理，根据初始数据集中其余对象取值的分布情况来对一个缺失值进行填充。

>数据挖掘中常用的有以下几种补齐方法：

> 1.人工填写（filling manually）

> 2.特殊值填充（Treating Missing Attribute values as Special values）\
将空值作为一种特殊的属性值来处理，它不同于其他的任何属性值。如所有的空值都用“unknown”填充。一般作为临时填充或中间过程。

> 3.平均值填充（Mean/Mode Completer）
```
将初始数据集中的属性分为数值属性和非数值属性来分别进行处理。

如果空值是数值型的，就根据该属性在其他所有对象的取值的平均值来填充该缺失的属性值； 
如果空值是非数值型的，就根据统计学中的众数原理，用该属性在其他所有对象的取值次数最多的值(即出现频率最高的值)来补齐该缺失的属性值。

与其相似的另一种方法叫条件平均值填充法（Conditional Mean Completer）。
在该方法中，用于求平均的值并不是从数据集的所有对象中取，而是从与该对象具有相同决策属性值的对象中取得。 
例如泰安尼克生存预测数据集里的Embarked变量，缺失这一变量的两个乘客Pclass和Fare相同，所以可以用Pclass和Fare与其相同的乘客这一集合的众数来确定Embarked的值。

这两种数据的补齐方法，其基本的出发点都是一样的，以最大概率可能的取值来补充缺失的属性值，只是在具体方法上有一点不同。与其他方法相比，它是用现存数据的多数信息来推测缺失值。
```
>4.热卡填充（Hot deck imputation，或就近补齐）
```
对于一个包含空值的对象，热卡填充法在完整数据中找到一个与它最相似的对象，然后用这个相似对象的值来进行填充。
不同的问题可能会选用不同的标准来对相似进行判定, 这个方法的缺点在于难以定义相似标准，主观因素较多。 
例如Fare变量的缺失值处理可以用这一方法，找到与该乘客信息相似度最高的乘客，Pclass船舱级别、Embarked登船港口占更大权重。
```
>5.最近距离邻法（K-means clustering）\
先根据欧式距离或相关分析来确定距离具有缺失数据样本最近的K个样本，将这K个值加权平均来估计该样本的缺失数据。

> 6.使用所有可能的值填充（Assigning All Possible values of the Attribute）
```
用空缺属性值的所有可能的属性取值来填充，能够得到较好的补齐效果.
但是当数据量很大或者遗漏的属性值较多时，其计算的代价很大，可能的测试方案很多.
如果没有任何可以借助的变量或可参考变量作用很低时可以采用这个方法，方便简单.
```
>7.回归（Regression）\
基于完整的数据集，建立回归方程。对于包含空值的对象，将已知属性值代入方程来估计未知属性值，以此估计值来进行填充。当变量不是线性相关时会导致有偏差的估计。

>8.期望值最大化方法（Expectation maximization，EM）
```
EM算法是一种在不完全数据情况下计算极大似然估计或者后验分布的迭代算法。
在每一迭代循环过程中交替执行两个步骤：
E步（Excepctaion step,期望步），在给定完全数据和前一次迭代所得到的参数估计的情况下计算完全数据对应的对数似然函数的条件期望；
M步（Maximzation step，极大化步），用极大化对数似然函数以确定参数的值，并用于下步的迭代。
算法在E步和M步之间不断迭代直至收敛，即两次迭代之间的参数变化小于一个预先给定的阈值时结束。该方法可能会陷入局部极值，收敛速度也不是很快，并且计算很复杂。
```
>9.多重插补（Multiple Imputation，MI）
```
多重填补方法分为三个步骤：

为每个空值产生一套可能的填补值，这些值反映了无响应模型的不确定性；
每个值都被用来填补数据集中的缺失值，产生若干个完整数据集合。
每个填补数据集合都用针对完整数据集的统计方法进行统计分析。
对来自各个填补数据集的结果进行综合，产生最终的统计推断，这一推断考虑到了由于数据填补而产生的不确定性。
该方法将空缺值视为随机样本，这样计算出来的统计推断可能受到空缺值的不确定性的影响。
该方法的计算也很复杂, 例如泰坦尼克数据集的Age变量缺失较多，缺失值占比超过10%，多采用多重插补法或随机森林算法。
```

>10.C4.5方法
```
通过寻找属性间的关系来对遗失值填充。
它寻找之间具有最大相关性的两个属性，其中没有遗失值的一个称为代理属性，另一个称为原始属性，用代理属性决定原始属性中的遗失值。
这种基于规则归纳的方法只能处理基数较小的名词型属性。
```

>原作者的话：就几种基于统计的方法而言，删除元组法和平均值法差于热卡填充法、期望值最大化方法和多重填充法；\
回归是比较好的一种方法，但仍比不上hot deck和EM；EM缺少MI包含的不确定成分。\
值得注意的是，这些方法直接处理的是模型参数的估计而不是空缺值预测本身,它们合适于处理无监督学习的问题，而对有监督学习来说，情况就不尽相同了。\
譬如，你可以删除包含空值的对象用完整的数据集来进行训练，但预测时你却不能忽略包含空值的对象。\
另外，C4.5和使用所有可能的值填充方法也有较好的补齐效果，人工填写和特殊值填充则是一般不推荐使用的。



#### 不处理
>不处理缺失值，直接在包含空值的数据上进行数据挖掘的方法包括贝叶斯网络和人工神经网络等。\
补齐处理只是将未知值补以我们的主观估计值，不一定完全符合客观事实，在对不完备信息进行补齐处理的同时，我们或多或少地改变了原始的信息系统。\
而且，对空值不正确的填充往往将新的噪声引入数据中，使挖掘任务产生错误的结果。\
因此，在许多情况下，我们还是希望在保持原始信息不发生变化的前提下对信息系统进行处理。

