import requests, re

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

s = requests.Session()
s.headers.update({'User-Agent': UA})
s.get('https://www.cpbl.com.tw/')
r = s.get('https://www.cpbl.com.tw/schedule')
print('schedule status:', r.status_code)

m = re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', r.text)
token = m.group(1) if m else 'NOT FOUND'
print('token:', token[:30])

r2 = s.post(
    'https://www.cpbl.com.tw/schedule/getgamedatas',
    data={
        'calendar': '2026/03/01',
        'location': '',
        'kindCode': 'G',
        '__RequestVerificationToken': token
    },
    headers={
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.cpbl.com.tw/schedule',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
)
print('post status:', r2.status_code)
print('response:', r2.text[:500])
