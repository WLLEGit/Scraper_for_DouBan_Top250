# Scraper

## 1. requests

```
pip install requests
```

### 1) GET

```python
r = requests.get(url, params={}, headers={}, cookies={}, timeout=limit)
```

```python
r.url 		# url that includes params(already edcoded)
r.status_code	# 200 if success
r.text  	# string
r.content 	# bytes
r.encoding
r.json()	# json data if exists
r.headers	# a dict  	r.headers['Content-Type']
r.cookies 	# a dict(already parsed)	r.cookies['ts']
```

### 2) POST

```python
r = requests.post(url, data={})
r = requests.post(url, json={})
```

```python
upload_files = {'file':open(path, 'rb')}
r = requests.post(url, files=upload_files)
```



## 2. BeautifulSoup

```
pip install beautifulsoup4
```

### 1) Quick Start

To cook a doc into a beautiful one

To change a doc into complex DOM Tree

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser", from_encoding='utf-8')
								# also lxml and html5lib
```

### 2) find_all()

```python
find_all(name, attrs, recursive, string, **kwargs)
# set recursive to False if you only want to get direct childs
```

```python
soup.find_all("li")
soup.find_all(id="")
soup.find_all(attrs={})
soup.find_all(class_="")
```

```python
soup.a.get_text()
# get only the text content
```



## 3. 正则表达式

### 1）普通字符

```
[ABC]		
[^ABC]		除去某些字符
[A-Z]		
.			匹配除换行符\n\r之外的所有字符，相当于[^\n\r]
[\s][\S]	分别匹配空白符（含换行）与非空白符（含换行）
[\w] 		匹配数字字母下划线，相当于[0-9a-zA-Z_]
```

### 2）特殊字符

```
正常匹配需转义
```

```
$ 		匹配字符串结尾
()	 	包含一个表达式
*		前面的表达式出现零次或多次
+		前面的表达式出现一次或多次
.		匹配除换行符外字符
[]
{}
?		零次或一次
\		转义
^		字符串开始
|		两项之间的选择
```

### 3）限定符

```
*
+
?
{n}		n次
{n,}	>=n次
{n,m}	n至m次
```

### 4）定位符

```
^		字符串开始
$		字符串结束
\b		单词边界
\B		非单词边界
```



### 5）贪婪匹配与非贪婪匹配

默认为贪婪匹配，即匹配尽量多的字符

要进行非贪婪匹配，在限定符后面加上?

```
/<.*>/		从'<'匹配到最后一个'>'
/<.*?>/		匹配一个html标签
```

### 6）选择

```
()					选择并记录，用下标访问
?=	exp1(?=exp2)	匹配exp2前面的exp1
?<=	(?<=exp2)exp1	匹配exp2后面的exp1
?!	exp1(?!exp2)	查找后面不是 exp2 的 exp1
?<!	(?<!exp2)exp1	查找前面不是 exp2 的 exp1
```



## 4. Read and Write Csv Files

```python
import csv
with open(path,'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print()
        
with open(path,'wb') as csvfile:
    writer = csv.writer(f)
    writer.writerows([(),()])
```

Another approach(dict):

```python
import csv
with open(path) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print()
		
		
with open(path,'w',encoding="utf-8-sig",newline="") as csvfile:
	fieldnames = []   # dict is unordered, so use list
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	
	writer.writeheader()
	writer.writerow({})
    writer.writerows([{},{}])
    
# UnicodeEncodeError: 'gbk' codec can't encode character '\ub3c4' in position 9: illegal multibyte sequence  --->if you omit the encoding parameter you will possibly encounter this error
# 中文乱码问题：写入时编码改为utf-8-sig（带签名的utf-8）
# 不加newline会出现空行，因为系统默认多加一个\r
# 网页空格有多种形式，在python中现实不出来，需要replace
```



