import re

import xlwt
from bs4 import  BeautifulSoup
import urllib.request



def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = "douban_top250.xls"
    saveData(datalist,savepath)

findlink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
def getData(baseurl):
    datalist=[]
    for i in range(10):
        url = baseurl + str(i*25)
        html = askURL(url)

        #逐一解析html
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"): #查找符合要求
            data=[]
            item=str(item)
            link = re.findall(findlink,item)[0]
            imgSrc = re.findall(findImgSrc, item)[0]
            Title = re.findall(findTitle, item)
            rating = re.findall(findRating,item)[0]
            judge = re.findall(findJudge,item)[0]
            inq = re.findall(findInq,item)
            bd = re.findall(findBd,item)[0]
            data.append(link)
            data.append(imgSrc)
            if len(Title)==1:
                data.append(Title[0])
                data.append(" ")
            else:
                data.append(Title[0])
                data.append(Title[1].replace('/',''))
            data.append(rating)
            data.append(judge)
            if len(inq)!=0:
                data.append(inq[0].replace('。',''))
            else:
                data.append(' ')
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd = bd.replace('/',' ')
            data.append(bd.strip())
            datalist.append(data)
    return datalist

def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('douban',cell_overwrite_ok=True)
    cols = ('link','img','Chinese Title','English Title','Rating','Judge number','Introduce','Information')
    for i in range(8):
        worksheet.write(0,i,cols[i])
    for i in range(250):
        print('run %d' %(i+1))
        for j in range(8):
            worksheet.write(i+1,j,datalist[i][j])
    workbook.save(savepath)


def askURL(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    request = urllib.request.Request(url,headers = head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
if __name__=="__main__":
    main()