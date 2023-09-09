from src.video import Video


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        '''
         """
        Инициализируем id плейлиста.
        Дальше все данные будут подтягиваться по API.
        """
        '''
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.video_info = self.get_service().videos().list(id=video_id, part='snippet,statistics').execute()
        self.title = self.video_info['items'][0]['snippet']['title']
        self.viewCount = self.video_info['items'][0]['statistics']['viewCount']
        self.likeCount = self.video_info['items'][0]['statistics']['likeCount']
        # self.pl_info = self.get_service().playlistItems().list(id=video_id, part='snippet,contentDetails').execute()

    def __str__(self):
        return f'{self.title}'
