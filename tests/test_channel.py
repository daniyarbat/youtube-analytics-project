from src.channel import Channel
import os


def test_print_info():
    # Создаем экземпляр канала для тестирования
    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # Запускаем метод print_info()
    channel.print_info()

def test_successful_channel_info():
    # Создаем экземпляр канала для тестирования
    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # Запускаем метод print_info()
    channel.print_info()

    # Проверяем, что информация о канале успешно получена
    assert channel.channel is not None
    assert 'items' in channel.channel
    assert len(channel.channel['items']) == 1

def test_invalid_channel_id():
    # Создаем экземпляр канала с недопустимым ID
    channel = Channel('invalid_channel_id')

    # Запускаем метод print_info()
    channel.print_info()

    # Проверяем, что вывод содержит сообщение об ошибке, связанное с недопустимым ID

def test_no_api_key():
    # Сохраняем текущий API ключ (если он существует)
    original_api_key = os.getenv('YT_API_KEY')

    # Удаляем API ключ из переменных окружения
    os.environ['YT_API_KEY'] = ''

    # Создаем экземпляр канала без установленного API ключа
    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # Запускаем метод print_info()
    channel.print_info()

    # Восстанавливаем исходный API ключ
    os.environ['YT_API_KEY'] = original_api_key
