'''
爬取当当网的五星图书排行榜的信息
'''

Max_Page = 3  # 爬取前三页的排行榜信息

import requests
from pyquery import PyQuery as pq
import json

def requests_dangdang(url, headers=None, retry=3):
    for _ in range(retry):
        try:
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                response.encoding = response.apparent_encoding
                return response.text
        except requests.RequestException as e:
            print(f'Requests Error:\n\t{url}\n\t{e.args}')
    return None

def parse_html(text):
    doc = pq(text)('ul[class="bang_list clearfix bang_list_mode"] li')
    for item in doc.items():
        yield {
           '排名': item('[class^="list_num"]').text().rstrip('.'),  ## 排名
           '书名': item('.name a').text(),  ## 书名
           '推荐指数': item('.star .tuijian').text(),  ## 推荐指数
           '作者': item('.publisher_info a').attr.title,  ## 作者
           '五星评分次数': item('.biaosheng span').text(),  ## 五星评分次数
           '价格': item('.price p:not([class]) .price_n').text(),  ## 价格
           '图书链接': item('.pic a').attr.href  ## 图书链接
       }
    return

def save_book_info(book):
    json_str = json.dumps(book, ensure_ascii=False, indent=4)
    with open('book.json', 'a', encoding='utf-8') as f:
        f.write(json_str)

def run(max_page=Max_Page):
    for page in range(1, max_page+1):
        url = f'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{str(page)}'
        text = requests_dangdang(url)
        if text == None:
            continue
        for book in parse_html(text):
            save_book_info(book)

if __name__ == '__main__':
    run()
