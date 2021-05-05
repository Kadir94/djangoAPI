import asyncio
from pyppeteer import launch


async def get_info():
    city_arr = []
    browser = await launch(headless=False, autoClose=False, width=1200, height=1200)
    page = await browser.newPage()
    await page.goto('https://www.checkmybus.de/', timeout=90000)
    await page.evaluate('''(selector) => document.querySelector(selector).click()''', "#origincityname")
    origin_cities = await page.waitForXPath('//div[contains(@class,"autocomplete hand hidden")]', timeout=5000)
    popular_cities = await origin_cities.xpath('//div[contains(@class,"city-result popular-city")]')
    for i in popular_cities:
        city_txt = await page.evaluate('(element) => element.textContent', i)
        city_arr.append(city_txt)
    city_arr = [x.strip('\xa0') for x in city_arr]

    return city_arr


asyncio.get_event_loop().run_until_complete(get_info())
