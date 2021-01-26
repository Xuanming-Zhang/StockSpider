import re

import xlwt
from bs4 import BeautifulSoup
import requests
import time


def main():
    baseurl = "https://cn.investing.com"
    start_date = "2020/12/01"
    end_date = "2021/01/14"
    datalist = getAmericaData(baseurl, start_date, end_date)
    savepath = "StockHomePage.xls"
    cols = ('href', 'title', 'last', 'high', 'low', 'pc', 'pcp', 'volume', 'curr_id', 'smlID', 'code')
    saveData(datalist, savepath, cols)


def getAmericaData(baseurl, start_date, end_date):
    url = baseurl + "/equities/StocksFilter?noconstruct=1&smlID=800&sid=&tabletype=price&index_id=all"
    print(url)
    headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Connection': 'keep-alive',
               "Cookie": "logglytrackingsession=ae534cd7-da4d-4679-903d-fae5c49cbbc2; udid=57815717000011562c52f23e0f83f5c7; adBlockerNewUserDomains=1610361615; _ga=GA1.2.932510087.1610361622; _gid=GA1.2.2108773129.1610361622; __gads=ID=79b4f3a718ae630b-224cfc2fa9c50065:T=1610361625:S=ALNI_MYDDDX0L3P-6-YWdVHu2N_gwghj1w; G_ENABLED_IDPS=google; _fbp=fb.1.1610415058590.104454704; OB-USER-TOKEN=060b0c2c-2f55-4091-aa6e-e9fe9473698d; _hjid=c9ffc1ae-66f0-482c-b3f8-0b3a70eb3445; adsFreeSalePopUp=3; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A6%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22942611%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A17%3A%22%2Findices%2Fusdollar%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226408%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A28%3A%22%2Fequities%2Fapple-computer-inc%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22243%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A25%3A%22%2Fequities%2Fbank-of-america%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22251%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Fequities%2Fintel-corp%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226373%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A23%3A%22%2Fequities%2Fadobe-sys-inc%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2215577%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A22%3A%22%2Fequities%2Fbiolase-tech%22%3B%7D%7D%7D%7D; PHPSESSID=i1bbhnbne6dnrf90upgcv5u8dq; geoC=CN; StickySession=id.63288621718.001cn.investing.com; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1610435281,1610519022,1610519160,1610591018; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1610591018; nyxDorf=MTZmN2M3ZSdiNm9jYjhhfT9mMW82LzExNDVhZw%3D%3D; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jan+14+2021+10%3A23%3A38+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BSH; OptanonAlertBoxClosed=2021-01-14T02:23:38.784Z",
               "Host": "cn.investing.com",
               "Referer": "https://cn.investing.com/equities/united-states",
               "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors",
               "Sec-Fetch-Site": "same-origin",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
               'X-Requested-With': 'XMLHttpRequest'}
    html = getURL(url, headers)
    # print(html)
    # 逐一解析html
    bs = BeautifulSoup(html, "html.parser")
    datalist = []
    i = 0
    for item in bs.tbody.find_all('tr', id=re.compile(r'^pair_\d*')):
        i += 1
        data = []
        item = str(item)
        href = re.findall(r'<a href="(.*?)"', item)[0]
        title = re.findall(r'<a href=.*? title="(.*?)">', item)[0]

        print("inputting " + title, i)

        last = re.findall(r'<td class=".*?-last">(.*?)</td>', item)[0]
        high = re.findall(r'<td class=".*?-high">(.*?)</td>', item)[0]
        low = re.findall(r'<td class=".*?-low">(.*?)</td>', item)[0]
        pc = re.findall(r'<td.*?-pc">(.*?)</td>', item)[0]
        pcp = re.findall(r'<td.*?-pcp">(.*?)</td>', item)[0]
        volume = re.findall(r'<td.*?-turnover">(.*?)</td>', item)[0]
        curr_id = re.findall(r'<tr id="pair_(\d+?)">', item)[0]
        stock_headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br',
                         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                         'Connection': 'keep-alive',
                         "Cookie": "logglytrackingsession=ae534cd7-da4d-4679-903d-fae5c49cbbc2; udid=57815717000011562c52f23e0f83f5c7; adBlockerNewUserDomains=1610361615; _ga=GA1.2.932510087.1610361622; _gid=GA1.2.2108773129.1610361622; __gads=ID=79b4f3a718ae630b-224cfc2fa9c50065:T=1610361625:S=ALNI_MYDDDX0L3P-6-YWdVHu2N_gwghj1w; G_ENABLED_IDPS=google; _fbp=fb.1.1610415058590.104454704; OB-USER-TOKEN=060b0c2c-2f55-4091-aa6e-e9fe9473698d; _hjid=c9ffc1ae-66f0-482c-b3f8-0b3a70eb3445; adsFreeSalePopUp=3; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A6%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22942611%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A17%3A%22%2Findices%2Fusdollar%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226408%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A28%3A%22%2Fequities%2Fapple-computer-inc%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22243%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A25%3A%22%2Fequities%2Fbank-of-america%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22251%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Fequities%2Fintel-corp%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226373%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A23%3A%22%2Fequities%2Fadobe-sys-inc%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2215577%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A22%3A%22%2Fequities%2Fbiolase-tech%22%3B%7D%7D%7D%7D; PHPSESSID=i1bbhnbne6dnrf90upgcv5u8dq; geoC=CN; StickySession=id.63288621718.001cn.investing.com; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1610435281,1610519022,1610519160,1610591018; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1610591018; nyxDorf=MTZmN2M3ZSdiNm9jYjhhfT9mMW82LzExNDVhZw%3D%3D; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jan+14+2021+10%3A23%3A38+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BSH; OptanonAlertBoxClosed=2021-01-14T02:23:38.784Z",
                         "Host": "cn.investing.com",
                         "Sec-Fetch-Dest": "document",
                         "Sec-Fetch-Mode": "navigate",
                         "Sec-Fetch-Site": "none",
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
        stock_url = baseurl + href + '-historical-data'
        stock_html = getURL(stock_url, headers=stock_headers)
        stock_html = str(stock_html)
        smlID = re.findall(r'window.siteData.smlID = (\d+?);', stock_html)[0]
        code = re.findall(r'<h2 class="float_lang_base_1 inlineblock">([A-Z]+).*?</h2>', stock_html)[0]
        data.append(href)
        data.append(title)
        data.append(last)
        data.append(high)
        data.append(low)
        data.append(pc)
        data.append(pcp)
        data.append(volume)
        data.append(curr_id)
        data.append(smlID)
        data.append(code)
        historical_data = getStockData(curr_id, smlID, start_date, end_date, code, baseurl, stock_url)
        historical_savepath = 'stock_data/' + code + '.xls'
        cols = ('date','close','open','high','low','volume','turnover')
        saveData(historical_data, historical_savepath, cols)
        datalist.append(data)
        if i == 2: break
    return datalist


def getStockData(curr_id, smlID, start_date, end_date, code, baseurl, stock_url):
    print("inputting historical data",curr_id, smlID, start_date, end_date, code, baseurl, stock_url)
    url = baseurl + '/instruments/HistoricalDataAjax'
    headers = {'Accept': 'text/plain, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded',
               # 'Cookie': 'udid=57815717000011562c52f23e0f83f5c7; adBlockerNewUserDomains=1610361615; _ga=GA1.2.932510087.1610361622; __gads=ID=79b4f3a718ae630b-224cfc2fa9c50065:T=1610361625:S=ALNI_MYDDDX0L3P-6-YWdVHu2N_gwghj1w; G_ENABLED_IDPS=google; _fbp=fb.1.1610415058590.104454704; OB-USER-TOKEN=060b0c2c-2f55-4091-aa6e-e9fe9473698d; _hjid=c9ffc1ae-66f0-482c-b3f8-0b3a70eb3445; OptanonAlertBoxClosed=2021-01-14T09:17:56.220Z; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jan+14+2021+17%3A17%3A57+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BSH; PHPSESSID=fn3sp80ednd3o4p470ph5687r3; StickySession=id.92613105909.773cn.investing.com; geoC=CN; logglytrackingsession=f90e46ec-10c4-4cd6-8567-9c6c6f03f936; outbrain_cid_fetch=true; _gid=GA1.2.71416090.1610871605; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1610519160,1610591018,1610615824,1610871605; adsFreeSalePopUp=3; __atuvc=1%7C3; __atuvs=6003f35c5e1f7489000; _gat=1; _gat_allSitesTracker=1; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A7%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22275%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Fequities%2Fmerck---co%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22276%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A22%3A%22%2Fequities%2Fmotorola-inc%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22277%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A15%3A%22%2Fequities%2F3m-co%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22278%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A22%3A%22%2Fequities%2Foffice-depot%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A6291%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A29%3A%22%2Fequities%2Fcelesio-mu%3Fcid%3D6291%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A629%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A25%3A%22%2Fequities%2Falumina-limited%22%3B%7Di%3A6%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226408%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A28%3A%22%2Fequities%2Fapple-computer-inc%22%3B%7D%7D%7D%7D; nyxDorf=NzA0ZTFmNXc0YG9gYDRifjZmMG5mYDIuPDwwNWZp; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1610871675',
               'Host': 'cn.investing.com', 'Origin': 'https://cn.investing.com',
               'Referer': stock_url,
               'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
               'X-Requested-With': 'XMLHttpRequest'}
    data = {'curr_id': str(curr_id), 'smlID': str(smlID), 'header': code+'历史数据', 'st_date': start_date,
            'end_date': end_date, 'interval_sec': 'Daily', 'sort_col': 'date', 'sort_ord': 'DESC',
            'action': 'historical_data'}
    html = postURL(url, headers, data)
    bs = BeautifulSoup(html, "html.parser")
    datalist = []
    for item in bs.tbody.find_all('tr'):
        item = str(item)
        data = re.findall(r'>(.*?)</td>',item)
        datalist.append(data)
    return datalist

def saveData(datalist, savepath, cols):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('stocks_US', cell_overwrite_ok=True)
    for i in range(len(cols)):
        worksheet.write(0, i, cols[i])
    for i in range(len(datalist)):
        print('run %d' % (i + 1))
        for j in range(len(cols)):
            worksheet.write(i + 1, j, datalist[i][j])
    workbook.save(savepath)


def getURL(url, headers):
    response = requests.get(url, headers=headers)
    html = ""
    try:
        html = response.text
    except Exception as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def postURL(url, headers, data):
    response = requests.post(url, headers=headers, data=data)
    html = ""
    try:
        html = response.text
    except Exception as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()
