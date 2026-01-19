from pydantic import BaseModel

from app.utils import replace_symbols


class File(BaseModel):
    name: str
    url: str


class Task(BaseModel):
    id: int
    title: str
    description: str
    price: int
    files: list[File] = []

    @property
    def url(self) -> str:
        url = f"https://kwork.ru/projects/{self.id}"
        return url

    @property
    def text_for_tg(self) -> str:
        title = replace_symbols(self.title)
        description = replace_symbols(self.description)
        text = f"<b>{title}</b>\n{description}"
        if self.files:
            text += f"\n\n<b>Файлы:</b>\n"
            text += "\n".join([f'- <a href="{file.url}">{file.name}</a>' for file in self.files])
        return text
