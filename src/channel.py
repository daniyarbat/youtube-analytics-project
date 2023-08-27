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
        self.api_key = os.getenv('YT_API_KEY')
        self.channel = None

    def print_info(self) -> None:

        """
        Выводит в консоль информацию о канале.
        """
        if not self.api_key:
            print("Ошибка: API ключ не установлен. "
                  "Убедитесь, что вы добавили ключ в переменные окружения.")
            return

        youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.printj(self.channel)

    def printj(self, dict_to_print: dict) -> None:

        """
        Выводит словарь в json-подобном удобном формате с отступами
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
