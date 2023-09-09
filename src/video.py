import os
from googleapiclient.discovery import build

class Video:
    def __init__(self, video_id: str) -> None:
        """
        Экземпляр инициализируется id видео.
        Дальше все данные будут подтягиваться по API.
        """
        self.video_id = video_id
        self.video_info = self.get_service().videos().list(id=video_id, part='snippet,statistics').execute()
        self.title = self.video_info['items'][0]['snippet']['title']
        #self.customUrl = self.video_info['items'][0]['snippet']['customUrl']
        self.viewCount = self.video_info['items'][0]['statistics']['viewCount']
        self.likeCount = self.video_info['items'][0]['statistics']['likeCount']

    @classmethod
    def get_service(cls):
        '''
        Класс-метод возвращающий объект
        для работы с YouTube API
        '''
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def __str__(self):
        return f'{self.title}'
