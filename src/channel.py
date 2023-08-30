import os
import json
from googleapiclient.discovery import build


class Channel:
    """
    Класс для ютуб-канала
    """
    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id
        self.info = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.customUrl = self.info['items'][0]['snippet']['customUrl']
        self.subscriberCount = self.info['items'][0]['statistics']['subscriberCount']
        self.videoCount = self.info['items'][0]['statistics']['videoCount']
        self.viewCount = self.info['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        '''
        Класс-метод возвращающий объект
        для работы с YouTube API
        '''
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, yt_channel):
        '''
        Метод, сохраняющий в файл значения
        атрибутов экземпляра `Channel`
        '''
        channel_info = {
            'title': self.title,
            'description': self.description,
            'customUrl': self.customUrl,
            'subscriberCount': self.subscriberCount,
            'videoCount': self.videoCount,
            'viewCount': self.viewCount
        }
        with open(yt_channel, 'w', encoding='utf-8') as json_file:
            json.dump(channel_info, json_file, indent=2, ensure_ascii=False)


    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.info, indent=2, ensure_ascii=False))
