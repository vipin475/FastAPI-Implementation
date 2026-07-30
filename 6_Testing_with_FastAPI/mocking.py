# tests/unit/test_task_service.py
from unittest.mock import patch, Mock
from service import task as task_service
from service.task import TaskNotFoundError
import pytest

def test_get_task_exists():
    fake_task = Mock()
    fake_task.id = 1
    fake_task.title = "Test"

    with patch("service.task.task_data.get_one", return_value=fake_task):
        result = task_service.get_task(1)
        assert result.id == 1

def test_get_task_not_found():
    with patch("service.task.task_data.get_one", return_value=None):
        with pytest.raises(TaskNotFoundError):
            task_service.get_task(999)
            
# patch replaces task_data.get_one with a fake that returns what you specify. Your code under test doesn't know the difference.









# mocking using pytest-mock library

def test_get_task_exists(mocker):
    fake_task = Mock(id=1, title="Test")
    mocker.patch("service.task.task_data.get_one", return_value=fake_task)
    result = task_service.get_task(1)
    assert result.id == 1


