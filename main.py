import requests

url = 'https://www.kn.vutbr.cz/is2/index.html'
form = {'str': 'B04-0319'}

res = requests.post(url,
                  json=form,
                  headers={
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                                'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                      'Accept-Encoding': 'gzip, deflate, br',
                      'Accept-Language': 'en-US,en;q=0.9',
                      'Cache-Control': 'max-age=0',
                      'Connection': 'keep-alive',
                      'Content-Length': '12',
                      'Content-Type': 'keep-alive',
                      'Cookie': 'PHPSESSID=0bfgka6ukp4ttdunvqvihphr34',
                      'Host': 'www.kn.vutbr.cz',
                      'Origin': 'https://www.kn.vutbr.cz',
                      'Pragma': 'no-cache',
                      'Referer': 'https://www.kn.vutbr.cz/is2/index.html',
                      'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                      'sec-ch-ua-mobile': '?0',
                      'sec-ch-ua-platform': '"Linux"',
                      'Sec-Fetch-Dest': 'document',
                      'Sec-Fetch-Mode': 'navigate',
                      'Sec-Fetch-Site': 'same-origin',
                      'Sec-Fetch-User': '?1',
                      'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/112.0.0.0 Safari/537.36',
                      'Remote-Address': '147.229.191.132:443',
                      'Referrer-Policy': 'strict-origin-when-cross-origin',

                  })

print(res.text)
