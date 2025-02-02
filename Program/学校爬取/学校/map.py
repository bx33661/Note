import folium
import pandas as pd

# 假设你有一个DataFrame，包含学校名称、经纬度信息
data = {
    'school_name': ['清华大学', '北京大学', '浙江大学', '上海交通大学'],
    'latitude': [39.999, 39.998, 30.265, 31.025],
    'longitude': [116.326, 116.305, 120.123, 121.437]
}

df = pd.DataFrame(data)

# 创建一个基础地图
m = folium.Map(location=[35.8617, 104.1954], zoom_start=5)

# 添加学校标记
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['school_name'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# 保存地图到HTML文件
m.save('school_distribution_map.html')