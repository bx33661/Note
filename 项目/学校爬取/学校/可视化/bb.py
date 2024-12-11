import pandas as pd
import folium
from pyecharts import options as opts
from pyecharts.charts import Map, Geo

def analyze_school_distribution():
    # 读取数据
    df = pd.read_csv('../学校/所有学校信息.csv')
    
    # 统计各省份学校数量
    province_stats = df['school_province'].value_counts()
    
    # 创建地图可视化
    c = (
        Map()
        .add("高校分布", [list(z) for z in zip(province_stats.index, province_stats.values)], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国高校地理分布热力图"),
            visualmap_opts=opts.VisualMapOpts(max_=province_stats.max()),
        )
    )
    c.render("school_distribution.html")