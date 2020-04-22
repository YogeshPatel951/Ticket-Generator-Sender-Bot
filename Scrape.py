import requests
import bs4

def scrape(link):
    response = requests.get(link)
    html = response.text

    soup = bs4.BeautifulSoup(html)
    li = soup.select('li')
    data = []
    for l in li:
        name = l.select('.name')[0].text
        email = l.select('.email')[0].text
        dob = l.select('.dob')[0].text
        if l.select('.city'):
            city = l.select('.city')[0].text
        else:
            city = ''
        if l.select('.phone'):
            phone = l.select('.phone')[0].text
        else:
            phone = ''
        payment = l.select('.payment')[0].text
        data.append([name,dob,email,city,phone,payment])

    print('data is scraped')
    return data


