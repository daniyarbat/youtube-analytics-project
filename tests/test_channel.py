from src.channel import Channel
import os
import pytest


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
    assert channel.channel_id is not None
    assert 'items' in channel.info
    assert len(channel.info['items']) == 1

@pytest.fixture
def moscowpython():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')

@pytest.fixture
def highload():
    return Channel('UCwHL6WHUarjGfUM_586me8w')

def test_greater_than(moscowpython, highload):
    result = moscowpython > highload
    assert result is False

def test_greater_than_or_equal(moscowpython, highload):
    result = moscowpython >= highload
    assert result is False

def test_less_than(moscowpython, highload):
    result = moscowpython < highload
    assert result is True

def test_less_than_or_equal(moscowpython, highload):
    result = moscowpython <= highload
    assert result is True

def test_equality(moscowpython, highload):
    result = moscowpython == highload
    assert result is False
