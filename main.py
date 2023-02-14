from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from data.dataScraping import getData
from icons import icons_rc
import folium
import time as tm
import io
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.init_ui()

    def init_ui(self):

        uic.loadUi('./UI/mainwindow.ui', self)
        self.closeWindow.clicked.connect(lambda : self.close())
        self.hideWindow.clicked.connect(lambda : self.showMinimized())
        self.restoreWindow.clicked.connect(lambda : self.restore_or_maximize_window())

        m, latitude, longitude = self.Map()
        self.updateButton.clicked.connect(lambda: self.mapClear())



    def mapClear(self):
        self.view.deleteLater()
        self.Map()


    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def earthQuakeRatingSize(self, size):
        if size >= 0 and size <= 2.9:
            radiusVal = 1000
        elif size >= 3 and size <= 3.9:
            radiusVal = 2000
        elif size >= 4 and size <= 4.9:
            radiusVal = 3000
        elif size >= 5 and size <= 5.9:
            radiusVal = 5000
        elif size >= 6 and size <= 6.9:
            radiusVal = 7000
        elif size >= 7 and size <= 7.9:
            radiusVal = 9000
        return radiusVal

    def earthQuakeRatingDepth(self, depth):
        if depth >= 0 and depth <= 5:
            depthVal = '#a80000'
            depthValRgb = '168, 0, 0'
        elif depth > 5 and depth <= 10:
            depthVal = '#ff1a0a'
            depthValRgb = '255, 26, 10'
        elif depth > 10 and depth <= 20:
            depthVal = '#ff5500'
            depthValRgb = '255, 85, 0'
        elif depth > 20 and depth <= 40:
            depthVal = '#ffff11'
            depthValRgb = '254, 255, 17'
        elif depth > 40 and depth <= 80:
            depthVal = '#55ff00'
            depthValRgb = '85, 255, 0'
        elif depth > 80 and depth <= 150:
            depthVal = '#00aaff'
            depthValRgb = '0, 170, 255'
        return depthVal, depthValRgb

    def circleMaker(self, m, latitude, longitude):
        folium.Circle(
            radius=100,
            location=[latitude, longitude],
            popup='Warning',
            color='#ff2566',
            fill=True,
            fillOpacity=1,
        ).add_to(m)

    def Map(self):
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=6,
            location=[39.1667, 35.6667]
        )

        self.view = QWebEngineView(self.frame_8)
        self.horizontalLayout_6.addWidget(self.view, stretch=1)
        allData = getData()

        for index in allData:
            if len(index) >= 8:
                id = index['id']
                date = index['date']
                time = index['time']
                latitude = index['latitude']
                longitude = index['longitude']
                depth = index['depth']
                size = index['size']
                location = index['location']
                if len(index) == 9:
                    locationTwo = index['locationTwo']

            popupVal = """<strong><h5>{} {}</h5>{} {} (M: {})</strong><br><br>Enlem: {}<br>Boylam: {}""".format(location, locationTwo, date, time, size, latitude,longitude)
            timeP = '{}  -  {}'.format(date, time)
            depthP = '{}  -  {}'.format(depth, size)
            coordinateP = '{}  -  {}'.format(latitude, longitude)
            locationP = '{} - {}'.format(location, locationTwo)
            radiusVal = self.earthQuakeRatingSize(size)
            depthVal, depthValRgb = self.earthQuakeRatingDepth(depth)
            styleSheet = "background-color: rgb({});\nborder-radius: 10px;".format(depthValRgb)

            popupCustom = folium.Popup(popupVal,
                                 min_width=150,
                                 max_width=150)
            folium.Circle(
                radius=radiusVal,
                location = [latitude,longitude],
                popup=popupCustom,
                color=depthVal,
                fill=True,
                fillOpacity= 1,
            ).add_to(m)

            if id == 0:
                self.label_1.setText(timeP)
                self.label_2.setText(depthP)
                self.label_3.setText(coordinateP)
                self.label_4.setText(locationP)
                self.frame_10.setStyleSheet(styleSheet)
                folium.Marker(
                    location = [latitude, longitude],
                    icon = folium.Icon(color='darkred', icon='exclamation-triangle', prefix='fa'),
                ).add_to(m)
            elif id == 1:
                self.label_5.setText(timeP)
                self.label_6.setText(depthP)
                self.label_7.setText(coordinateP)
                self.label_8.setText(locationP)
                self.frame_11.setStyleSheet(styleSheet)
            elif id == 2:
                self.label_9.setText(timeP)
                self.label_10.setText(depthP)
                self.label_11.setText(coordinateP)
                self.label_12.setText(locationP)
                self.frame_12.setStyleSheet(styleSheet)
            elif id == 3:
                self.label_13.setText(timeP)
                self.label_14.setText(depthP)
                self.label_15.setText(coordinateP)
                self.label_16.setText(locationP)
                self.frame_13.setStyleSheet(styleSheet)
            elif id == 4:
                self.label_17.setText(timeP)
                self.label_18.setText(depthP)
                self.label_19.setText(coordinateP)
                self.label_20.setText(locationP)
                self.frame_14.setStyleSheet(styleSheet)
            elif id == 5:
                self.label_21.setText(timeP)
                self.label_22.setText(depthP)
                self.label_23.setText(coordinateP)
                self.label_24.setText(locationP)
                self.frame_15.setStyleSheet(styleSheet)
            elif id == 6:
                self.label_25.setText(timeP)
                self.label_26.setText(depthP)
                self.label_27.setText(coordinateP)
                self.label_28.setText(locationP)
                self.frame_16.setStyleSheet(styleSheet)
            elif id == 7:
                self.label_29.setText(timeP)
                self.label_30.setText(depthP)
                self.label_31.setText(coordinateP)
                self.label_32.setText(locationP)
                self.frame_17.setStyleSheet(styleSheet)


        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())
        nowDate = tm.strftime('%x')
        nowTime = tm.strftime('%X')
        now = f'{nowDate}  -  {nowTime}'
        self.lastUpdateValue.setText(now)
        return m, latitude, longitude


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = Ui()
        window.show()
        app.exec_()
    except Exception as f:
        print(f)