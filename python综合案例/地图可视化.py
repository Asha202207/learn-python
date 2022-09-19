"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data = [
    ("北京", 99),
    ("上海", 199),
    ("湖南", 299),
    ("台湾", 399),
    ("广东", 499)
]
# 添加数据
map.add("测试地图", data, "china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF "},
            {"min": 100, "max": 999, "label": "100-990人", "color": "#FFFF99 "},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966 "},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666 "},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333 "},
            {"min": 100000, "label": "100000+人", "color": "#990033 "},
        ]
    )
)
# 绘图
map.render()
