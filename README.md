# DangDangBook

爬取【当当网】畅销榜的图书信息

## 初版

* 2019/11/16: 独立完成网站爬取
* [爬取网站](http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1)
* 爬取内容： 畅销榜图书信息
* 结果文件：book.json

## 执行

```shell
pip install requests
pip install pyquery
python3 book.py
```

## [结果](book.json)

```json
{
    "排名": "1",
    "书名": "谜案鉴赏",
    "推荐指数": "100%推荐",
    "作者": "[美]莉比・菲舍尔・赫尔曼 著，汪德均 /刘建洲/马遇乐 译",
    "五星评分次数": "17669次",
    "价格": "¥35.80",
    "图书链接": "http://product.dangdang.com/28470981.html"
}
```
