#Тест, проверяющий работу функции add

from src.app import add

def test_add():
    assert add(2, 3) == 5