from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#创建一个D6
die_1 = Die()
die_2 = Die(8)

#摇骰子并把结果添加到列表中
results = []
for roll in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#计算每个面出现的次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '频率'}

my_layout = Layout(title='掷骰子的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')


