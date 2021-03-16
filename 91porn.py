import requests
import re
import os

url_91 = 'https://0316.workarea2.live/v.php?next=watch'
headers = {
    'User-Agent': " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",

}
data = {"session_language": "cn_CN"}


def getcontext():
    r = requests.post(url_91, data=data)
    url = re.findall(
        r'<a href="(.*?)&page=1&viewtype=basic&category=mr', r.text)
    img = re.findall(r'<img class="img-responsive" src="(.*?).jpg" />', r.text)
    time = re.findall(r'<span class="duration">(.*?)</span>', r.text)
    title = re.findall(
        r' <span class="video-title title-truncate m-t-5">(.*?)</span>', r.text)
    title_91 = "# 91PORN每日最新视频列表" + "\n"
    fp = open('remark.md', 'a')
    fp.write(title_91)
    for i in range(len(img)):
        #  list = 'url:' + url[i] + ' imgurl:' + img[i] + '.jpg time:' + time[i] + ' title:' + title[i]
        MD = '![Img](' + img[i] + '.jpg' + ')' + '\n' + '## 时长:' + time[i] + ' [' + title[i] + '](' + url[
            i] + ')' + '\n'
        fp.write(MD)
    fp.close()


if __name__ == "__main__":
    getcontext()
