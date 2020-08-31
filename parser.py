from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self):
        self.url = 'https://store.steampowered.com/explore/new/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

    def parse(self):
        page = requests.get(self.url, self.headers)
        content = BeautifulSoup(page.content, 'html.parser')
        videos = content.findAll('div', {'class': 'tab_item_name'})
        video_list = []
        videos_link = content.findAll('a', {'class': 'tab_item'})
        video_link_list = []

        for video in videos:
            a = video.text
            video_list.append(a)

        for video in videos_link:
            a = video['href']
            video_link_list.append(a)

        return '{} - {}'.format(video_list[0], video_link_list[0])


a = Parser()
print(a.parse())
