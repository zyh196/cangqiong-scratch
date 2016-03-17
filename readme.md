# 苍穹滴滴快的智能出行平台数据获取器

## 数据来源

http://v.kuaidadi.com/

data下有已经获取好的成都的相关数据

## 解释

比如data下有这么个文件

`demand_2016.03.10_510100_.csv`

名称头部是数据类型

* demand 打车需求量
* distribute 出租车分布
* money 车费
* response 被抢单时间
* satisfy 打车难易度

然后是日期2016.03.10，城市编号510100（这里只包括成都510100的为减小仓库大小）

`.csv`文档即逗号分隔符文档。R语言,Python,Matlab读起来应该都很容易。WPS,Excel也可以读取或者存成这个格式。

数据里面都是id,经度,纬度,值(不同类型值的意思不一样)的记录模式。

## 使用脚本

下载脚本是Python写的，主要是如果想下其他城市的数据可以用它，去修改`Downloader`类里`cityId_list`的值，
现在这个列表里只有成都的代号。

下载执行

		downloader=Downloader()
		downloader.download()
		to_csv_all(downloader.data)
		
## 信度

这个数据来源不明，使用请谨慎。特别是可以看到返回的json数据里标的
realdate与date不一致，疑似是从过去某个月的时间推断的现在的数据。

另外还有些明显的异常值，比如明明是成都的数据却出现了在哈尔滨或海上的数据点之类的注意排除。
