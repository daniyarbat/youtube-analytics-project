import datetime
from src.channel import Channel
import isodate

class PlayList(Channel):
    def __init__(self, playlist_id: str) -> None:
        '''
        Инициализация по id плейлиста.
        Добавление данных по API
        '''
        self.playlist_id = playlist_id
        self.playlist_info = self.get_service().playlists().list(id=self.playlist_id, part='snippet').execute()
        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id

    @property
    def total_duration(self):
        '''
        Возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста
        '''
        playlist_items = self.get_service().playlistItems().list(
            playlistId=self.playlist_id, part='contentDetails').execute()

        total_duration = datetime.timedelta()

        for item in playlist_items['items']:
            video_id = item['contentDetails']['videoId']
            video_info = self.get_service().videos().list(
                id=video_id, part='contentDetails').execute()
            duration = video_info['items'][0]['contentDetails']['duration']
            duration_seconds = isodate.parse_duration(duration).total_seconds()
            total_duration += datetime.timedelta(seconds=duration_seconds)

        return total_duration

    def show_best_video(self):
        '''
        возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        '''
        playlist_items = self.get_service().playlistItems().list(
            playlistId=self.playlist_id, part='contentDetails').execute()

        best_video = None
        best_likes = 0

        for item in playlist_items['items']:
            video_id = item['contentDetails']['videoId']
            video_info = self.get_service().videos().list(
                id=video_id, part='statistics').execute()

            likes = int(video_info['items'][0]['statistics']['likeCount'])

            if likes > best_likes:
                best_likes = likes
                best_video = "https://youtu.be/" + video_id

        return best_video
