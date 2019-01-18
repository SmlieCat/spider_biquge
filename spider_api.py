import requests
from bs4 import BeautifulSoup





headers = {
        "Host": "www.biquge5200.cc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0"
    }



def book():

    url = 'https://www.biquge5200.cc/xuanhuanxiaoshuo/'

    response = requests.get(url, headers=headers)

    response.encoding = 'gbk'
    after_bs = BeautifulSoup(response.text, 'lxml')

    new_updata = after_bs.find_all('div', class_='l')  # div class=l标签 包裹的内容
    after_new_updata = BeautifulSoup(str(new_updata), 'lxml')

    span2 = after_new_updata.find_all('span', class_='s2')  # 继续筛选书籍
    span5 = after_new_updata.find_all('span', class_='s5')  # 继续筛选作者

    writer_list = []  # 作者list
    for sp5 in span5:
        writer_list.append(sp5.text)

    after_span2 = BeautifulSoup(str(span2), 'lxml')

    a_list = after_span2.find_all('a')
    for a in a_list:

        book_name = a.text  # ----------------小说名

        book_url = a.get('href')  # ------------------小说url

        writer = writer_list.pop(0)  # -----------------作者





#章节
def section(book_url):

    response = requests.get(book_url, headers=headers)
    response.encoding = 'gbk'

    after_bs = BeautifulSoup(response.text, 'lxml')

    div_fmimg = after_bs.find('div', id="fmimg")
    img_list = div_fmimg('img')
    for a in img_list:
        img_url = a.get('src')  # ------------图片url


    div_intro = after_bs.find('div', id="intro")
    book_desc = div_intro.text  # -----------------------小说简介


    dl = after_bs.find_all('dl')
    after_new_updata = BeautifulSoup(str(dl), 'lxml')
    dd_list = after_new_updata.find_all('dd')

    after_dd = BeautifulSoup(str(dd_list), 'lxml')
    a_list = after_dd.find_all('a')

    num = len(a_list) - 9
    for i in range(num):
        section_url = a_list[9 + i].get('href')  # ---------------小说章节url
        section_title = a_list[9 + i].text  # --------------------小说章节标题




#小说正文
def content(section_url):

    response = requests.get(section_url, headers=headers)
    response.encoding = 'gbk'
    after_bs = BeautifulSoup(response.text, 'lxml')

    div_content = after_bs.find('div', id="content")

    content_p = BeautifulSoup(str(div_content), 'lxml')
    content = content_p.text# -------------------小说正文





