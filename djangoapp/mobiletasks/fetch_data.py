from pyppeteer import launch
import asyncio


async def get_info():
    browser = await launch(headless=False, autoClose=False, width=1200, height=1200)
    page = await browser.newPage()
    base = 'https://airquality.ie'
    await page.goto('https://airquality.ie/stations', timeout=90000)
    await asyncio.sleep(5)
    await page.waitForXPath('//*[@id="monitors-table"]', timeout=50000)
    stations = await page.xpath('//tbody/tr[@class="row-as-link"]')
    station_info = []
    station_id = []
    station_name = []
    geoloc_info = []
    lat = []
    lgn = []
    station_links = [await page.evaluate('(element) => element.getAttribute("data-href")', station) for station in
                     stations]
    base += '% s'
    links = [base % i for i in station_links]
    # print(links)
    dict_ = []
    new_arr = ['https://airquality.ie/station/EPA-54', 'https://airquality.ie/station/EPA-78',
               'https://airquality.ie/station/EPA-25']
    for i in new_arr:
        await page.goto(i)
        await page.waitForXPath('/html/body/main/section/div/div[2]/div[2]/div[2]/div[1]/div/header', timeout=5000)
        info = await page.xpath('/html/body/main/section/div/div[2]/div[2]/div[2]/div[1]/div/header/h3')
        geolocation = await page.xpath(
            '/html/body/main/section/div/div[2]/div[2]/div[2]/div[3]/div/section/div[2]/span[2]')
        for d in info:
            info_txt = await page.evaluate('(element) => element.textContent', d)
            station_info.append(info_txt)
        # print(station_info)
        station_id = [x[8:10] for x in station_info]
        station_name = [x[12:] for x in station_info]
        for g in geolocation:
            geoloc_txt = await page.evaluate('(element) => element.textContent', g)
            geoloc_info.append(geoloc_txt)
            # print(geoloc_info)
            lat = [float(x[:7]) for x in geoloc_info]
            lgn = [float(x[11:18]) for x in geoloc_info]
            # print(lat)
            # print(lgn)

        await asyncio.sleep(5)
    for i, n, l, g in zip(station_id, station_name, lat, lgn):
        dict_.append({
            'Station_id': i,
            'Station_Name': n,
            'Latitude': l,
            'Longnitude': g,
        })

    return dict_

# asyncio.get_event_loop().run_until_complete(get_info())
