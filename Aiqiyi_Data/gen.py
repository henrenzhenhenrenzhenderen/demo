import requests
from bs4 import BeautifulSoup

# 发送HTTP GET请求，获取网页内容
url = "https://www.a-hospital.com/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8"
response = requests.get(url)

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.content, "html.parser")

# 查找医院列表所在的HTML元素
hospital_table = soup.find("table", {"class": "wikitable"})
hospital_rows = hospital_table.find_all("tr")

# 遍历医院列表，提取医院名字和省份信息
for row in hospital_rows:
    # 忽略表头行
    if row.find("th"):
        continue
    # 提取医院名字和省份信息
    cells = row.find_all("td")
    if len(cells) >= 2:
        hospital_name = cells[0].text.strip()
        province = cells[1].text.strip()
        print(f"医院名字：{hospital_name}\t省份：{province}")
