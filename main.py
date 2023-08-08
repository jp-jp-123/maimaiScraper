from bs4 import BeautifulSoup as BSoup
from webdriver import OpenChromeDefaultProfile as OpenChrome
from os.path import basename
import constants
import requests

# TODO: FINALLY MAKE THE SCRAPER
# TODO: MAKE A SECOND VERSION WHERE USER DOESNT HAVE TO CLOSE ALL CHROME WINDOWS TO RUN SUCCESSFULLY


class MaiAlbumScraper:
    def __init__(self):
        self.home_url = 'https://maimaidx-eng.com/maimai-mobile/home/'
        self.album_url = 'maimai-mobile/photo/album/'
        self.target_url = constants.targetURL(self.album_url)

        self.driver = OpenChrome()

        self.parse_url = None
        self.source_element = None

        self.all_photo_instance = None

        self.datetime_included = True
        self.datetime = None
        self.difficulty = None
        self.song_title = None
        self.chart_type = None
        self.photo_url = None
        self.photo_info = {}

    def TakePageSource(self):
        driver = self.driver

        driver.get(self.home_url)
        driver.implicitly_wait(3)
        driver.get(self.target_url)
        driver.implicitly_wait(3)

        page_source = driver.page_source
        self.parse_url = BSoup(page_source, 'html5lib')

        self.source_element = self.parse_url.prettify()

    def SearchPhotoInstances(self):
        self.all_photo_instance = self.parse_url.find_all('div', class_='m_10 p_5 f_0')

    def ExtractPhotoInfo(self):
        for photo in self.all_photo_instance:
            self.song_title = photo.find('div', class_='black_block w_430 m_3 m_b_5 p_5 t_l f_15 break').text

            self.chart_type = photo.find('img', class_='music_kind_icon f_r')
            self.chart_type = constants.chartType(self.chart_type['src'])

            self.difficulty = photo.find('img', class_='h_16 f_l')
            self.difficulty = constants.diificulty(self.difficulty['src'])

            if self.datetime_included:
                self.datetime = photo.find('div', class_='block_info p_3 f_11 white').text

            self.photo_url = photo.find('img', class_='w_430')
            self.photo_url = self.photo_url.attrs['src']

            all_info = (self.song_title, self.chart_type, self.difficulty, self.datetime)
            all_info = '-'.join(all_info)

            # print(self.song_title, self.chart_type, self.difficulty, self.datetime, sep='-')
            # print('File', self.photo_url, sep='-')

            self.photo_info[self.photo_url] = all_info

    def DownloadPhoto(self):
        for photo_url, info in self.photo_info.items():
            url = photo_url
            filename = info

            image = requests.get(url).content

            with open(basename(filename), 'wb') as file_write:
                file_write.write(image)

    def Run(self):
        self.TakePageSource()
        self.SearchPhotoInstances()
        self.ExtractPhotoInfo()
        self.DownloadPhoto()


if __name__ == '__main__':
    c = MaiAlbumScraper()
    c.Run()
