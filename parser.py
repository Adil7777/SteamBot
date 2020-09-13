from bs4 import BeautifulSoup
import requests
import os.path


class Parser:
    def __init__(self, last_key_file):
        self.url = 'https://store.steampowered.com/explore/new/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        self.last_key_file = last_key_file

        if os.path.exists(last_key_file):
            self.last_key = open(self.last_key_file, 'r').read()
        else:
            f = open(last_key_file, 'w')
            self.last_key_file = self.parse()
            f.write(self.last_key_file)
            f.close()

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

    def new_game(self):
        new = self.parse()
        old = open(self.last_key_file, 'r').read()

        if new != old:
            f = open(self.last_key_file, 'w')
            self.game = self.parse()
            f.write(self.game)
            f.close()
            return True
        else:
            return False

    def get_game(self):
        return open(self.last_key_file, 'r').read()
