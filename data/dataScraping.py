from selenium import webdriver
from time import sleep
import json

def getData():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_position(-300, -300)
    browser.set_window_size(0, 0)
    browser.get('http://udim.koeri.boun.edu.tr/zeqmap/hgmmap.asp')
    sleep(2)
    a = browser.find_elements_by_class_name('tbldiv')
    data = []
    all = []
    for i in a:
        text = i.text
        data.append(text.split('\n'))
    data[0].pop(0)
    for j in data[0]:
        j.split(' ')
        all.append(j)
    sleep(1)
    localData = []
    counter = 0
    for index in all:
        earthQuake = index.split(' ')
        locationTwo = None
        if len(earthQuake) >= 7:
            date = earthQuake[0]
            time = earthQuake[1]
            latitude = earthQuake[2]
            longitude = earthQuake[3]
            depth = float(earthQuake[4])
            size = float(earthQuake[5])
            location = earthQuake[6]
            if len(earthQuake) == 8:
                locationTwo = earthQuake[7]

        jsonData =  json.dumps({
            'id' : counter,
            'date' : date,
            'time' : time,
            'latitude' : latitude,
            'longitude' : longitude,
            'depth' : depth,
            'size' : size,
            'location' : location,
            'locationTwo' : locationTwo
        })
        counter += 1
        localData.append(json.loads(jsonData))
    return localData
