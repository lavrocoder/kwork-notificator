import json

import requests
from bs4 import BeautifulSoup

from app.schemas import Task, File


class KWork:
    def __init__(self, text: str):
        self.soup = BeautifulSoup(text, "html.parser")

    @classmethod
    def get_response(cls, url: str):
        response = requests.get(url, timeout=10)
        return response

    def get_tasks(self) -> list[Task]:
        """
        Получает задачи.
        Задачи передаются в html файле в скрипте в переменной window.stateData.
        :return: Список задач.
        """
        tasks = []
        scripts = self.soup.select("script")
        data = None
        for script in scripts:
            text = script.text
            if 'window.stateData' in text:
                text = text[text.find('window.stateData'):]
                text = text[text.find('{'):]
                text = text[:text.find("};") + 1]
                data = json.loads(text)
        if data is None:
            return []

        for want in data.get("wants", []):
            title = want.get("name", "Без названия")
            price = int(want.get('priceLimit', '0').replace(".00", ""))
            description = want.get("description", "")
            want_id = want.get("id", "")
            files = []
            for file in want.get("files", []):
                url = file.get("url", "")
                name = file.get("fname", "")
                files.append(File(url=url, name=name))

            task = Task(id=want_id, title=title, description=description, price=price, files=files)
            tasks.append(task)
        return tasks