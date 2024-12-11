import json
import csv
import requests
import time
from datetime import datetime
import random
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def extract_school_info(json_data):
    college_data = json_data['college']
    attach_data = college_data.get('attach', {})
    
    # 基本信息
    school_info = {
        'school_name': college_data.get('name', ''),
        'school_address': attach_data.get('address', ''),
        'school_introduce': attach_data.get('introduce', ''),
        'short_introduce': attach_data.get('shortIntroduce', ''),
        'school_telephone': attach_data.get('telephone', ''),
        'school_website': attach_data.get('website', ''),
        'school_email': attach_data.get('email', ''),
        'enroll_website': attach_data.get('enrollWebsite', ''),
        
        # 地理位置信息
        'school_province': college_data.get('province', {}).get('name', ''),
        'school_city': college_data.get('city', {}).get('name', ''),
        'school_district': college_data.get('district', {}).get('name', ''),
        
        # 学校属性
        'school_type': college_data.get('type', {}).get('name', ''),
        'school_nature': college_data.get('nature', {}).get('name', ''),
        'school_level': college_data.get('level', {}).get('name', ''),
        'school_belong': college_data.get('belong', ''),
        
        # 学校规模
        'build_year': attach_data.get('buildYear', ''),
        'area': attach_data.get('area', ''),
        'doctor_num_a': attach_data.get('doctorNumA', 0),
        'doctor_num_b': attach_data.get('doctorNumB', 0),
        'master_num_a': attach_data.get('masterNumA', 0),
        'master_num_b': attach_data.get('masterNumB', 0),
        'national_subject': attach_data.get('nationalSubject', 0),
        'research_num': attach_data.get('researchNum', 0),
        
        # 生活设施
        'canteen_info': attach_data.get('canteen', ''),
        'dormitory_info': attach_data.get('dormitory', ''),
    }
    
    # 标签信息
    school_info['school_tags'] = ', '.join([tag['name'] for tag in college_data.get('tags', [])])
    
    # 排名信息
    ranks = []
    for rank in college_data.get('attachRanks', []):
        rank_info = {
            'rank': rank.get('rank', ''),
            'rank_type': rank.get('topRankType', {}).get('name', ''),
            'year': rank.get('year', ''),
            'order': rank.get('order', '')
        }
        ranks.append(rank_info)
    school_info['school_ranks'] = str(ranks)
    
    # 媒体资源
    media_urls = []
    for media in college_data.get('attachMedias', []):
        media_info = {
            'name': media.get('name', ''),
            'type': media.get('type', ''),
            'url': media.get('url', '')
        }
        media_urls.append(media_info)
    school_info['media_resources'] = str(media_urls)
    
    # Logo URL
    school_info['logo_url'] = college_data.get('logo_url', '')
    
    return school_info

def fetch_and_save_school_info(start_id, end_id, csv_file_path):
    fieldnames = [
        'school_name', 'school_address', 'school_introduce', 'short_introduce',
        'school_telephone', 'school_website', 'school_email', 'enroll_website',
        'school_province', 'school_city', 'school_district',
        'school_type', 'school_nature', 'school_level', 'school_belong',
        'build_year', 'area', 'doctor_num_a', 'doctor_num_b',
        'master_num_a', 'master_num_b', 'national_subject', 'research_num',
        'canteen_info', 'dormitory_info',
        'school_tags', 'school_ranks', 'media_resources', 'logo_url'
    ]
    
    # 创建一个Session对象，配置重试策略
    session = requests.Session()
    retry_strategy = Retry(
        total=3,  # 最多重试3次
        backoff_factor=1,  # 重试间隔时间
        status_forcelist=[500, 502, 503, 504]  # 遇到这些状态码就重试
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    # 记录失败的ID
    failed_ids = []
    
    with open(csv_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        total_schools = end_id - start_id + 1
        
        for i in range(start_id, end_id + 1):
            url = f"https://api.caihongzhiyuan.cn/api_front/college/{i}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            
            # 显示进度
            progress = (i - start_id + 1) / total_schools * 100
            print(f"\r正在处理: ID {i}, 进度: {progress:.2f}%", end="")
            
            try:
                response = session.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        if 'college' in json_data:
                            school_info = extract_school_info(json_data)
                            writer.writerow(school_info)
                        else:
                            print(f"\n学校ID {i} 数据格式不正确")
                            failed_ids.append(i)
                    except json.JSONDecodeError:
                        print(f"\n学校ID {i} JSON解析失败")
                        failed_ids.append(i)
                else:
                    print(f"\n学校ID {i} 请求失败，状态码: {response.status_code}")
                    failed_ids.append(i)
                
                # 添加随机延时，避免请求过于频繁
                time.sleep(random.uniform(0.5, 1.5))
                
            except requests.exceptions.RequestException as e:
                print(f"\n学校ID {i} 请求异常: {str(e)}")
                failed_ids.append(i)
        
        print("\n爬取完成！")
        if failed_ids:
            print(f"以下学校ID爬取失败: {failed_ids}")
            # 将失败的ID保存到文件中
            failed_file = f'failed_schools_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
            with open(failed_file, 'w') as f:
                f.write(','.join(map(str, failed_ids)))
            print(f"失败的学校ID已保存到文件: {failed_file}")

# 使用示例
fetch_and_save_school_info(1, 300, 'output/schools.csv')