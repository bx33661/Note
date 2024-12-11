import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import options as opts
from pyecharts.charts import Map, Geo
import warnings
import os
warnings.filterwarnings('ignore')  # 忽略警告信息

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 构建数据文件的完整路径 - 使用根目录下的CSV文件
data_file = os.path.join(current_dir, '学校', '所有学校信息.csv')
# 构建结果目录的完整路径
result_dir = os.path.join(current_dir, '可视化结果')

def analyze_school_distribution():
    """分析高校地理分布"""
    print("正在分析高校地理分布...")
    
    # 读取数据
    df = pd.read_csv(data_file)
    
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
    c.render(os.path.join(result_dir, "school_distribution.html"))
    print("地理分布分析完成，结果保存在 可视化结果/school_distribution.html")

def analyze_school_types():
    """分析学校类型分布"""
    print("正在分析高校类型分布...")
    
    df = pd.read_csv(data_file)
    
    # 创建学校类型分布饼图
    plt.figure(figsize=(10, 8))
    type_counts = df['school_type'].value_counts()
    plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%')
    plt.title('高校类型分布')
    plt.axis('equal')
    plt.savefig(os.path.join(result_dir, 'school_types_pie.png'))
    plt.close()
    
    # 分析不同类型学校的博士点数量��布
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='school_type', y='doctor_num_a', data=df)
    plt.title('不同类型高校博士点数量分布')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(result_dir, 'doctor_programs_by_type.png'))
    plt.close()
    
    print("类型分布分析完成，结果保存在 可视化结果/school_types_pie.png 和 doctor_programs_by_type.png")

def analyze_school_scale():
    """分析学校规模"""
    print("正在分析高校规模...")
    
    df = pd.read_csv(data_file)
    
    # 创建散点图展示学校规模与研究实力的关系
    plt.figure(figsize=(10, 6))
    plt.scatter(df['area'], df['research_num'], alpha=0.5)
    plt.xlabel('校园面积(亩)')
    plt.ylabel('研究机构数量')
    plt.title('高校规模与研究实力关系图')
    plt.tight_layout()
    plt.savefig(os.path.join(result_dir, 'scale_research.png'))
    plt.close()
    
    # 分析学校的研究生教育规模
    df['total_graduate'] = df['master_num_a'] + df['master_num_b'] + df['doctor_num_a'] + df['doctor_num_b']
    top_20 = df.nlargest(20, 'total_graduate')
    
    plt.figure(figsize=(15, 6))
    plt.bar(top_20['school_name'], top_20['total_graduate'])
    plt.xticks(rotation=45, ha='right')
    plt.title('研究生教育规模TOP20���校')
    plt.tight_layout()
    plt.savefig(os.path.join(result_dir, 'top_20_graduate.png'))
    plt.close()
    
    print("规模分析完成，结果保存在 可视化结果/scale_research.png 和 top_20_graduate.png")

def analyze_school_tags():
    """分析学校标签"""
    print("正在分析高校标签...")
    
    df = pd.read_csv(data_file)
    
    # 分析学校标签
    tags = df['school_tags'].str.split(', ', expand=True).stack()
    tag_counts = tags.value_counts()
    
    plt.figure(figsize=(10, 6))
    tag_counts.plot(kind='bar')
    plt.title('高校标签分布')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(result_dir, 'school_tags.png'))
    plt.close()
    
    print("标签分析完成，结果保存在 可视化结果/school_tags.png")

def analyze_rankings():
    """分析学校排名"""
    print("正在分析高校排名...")
    
    df = pd.read_csv(data_file)
    
    # 提取软科排名
    def extract_rank(ranks_str):
        try:
            ranks = eval(ranks_str)
            for rank in ranks:
                if rank['rank_type'] == '软科':
                    return int(rank['rank']) if rank['rank'].isdigit() else None
        except:
            return None
    
    df['软科排名'] = df['school_ranks'].apply(extract_rank)
    
    # 创建TOP30高校排名对比图
    top_30 = df.dropna(subset=['软科排名']).nsmallest(30, '软科排名')
    
    plt.figure(figsize=(15, 8))
    plt.barh(top_30['school_name'], top_30['软科排名'])
    plt.title('软科排名TOP30高校')
    plt.xlabel('排名')
    plt.tight_layout()
    plt.savefig(os.path.join(result_dir, 'top_30_rankings.png'))
    plt.close()
    
    print("排名分析完成，结果保存在 可视化结果/top_30_rankings.png")

def main():
    """主函数"""
    # 创建保存结果的目录
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 检查数据文件是否存在
    if not os.path.exists(data_file):
        print(f"错误：找不到数据文件 {data_file}")
        print("请确保CSV文件与Python脚本在同一目录下")
        return
    
    # 执行所有分析
    analyze_school_distribution()
    analyze_school_types()
    analyze_school_scale()
    analyze_school_tags()
    analyze_rankings()
    
    print("\n所有分析完成！请查看'可视化结果'文件夹中的图表。")

if __name__ == "__main__":
    main() 