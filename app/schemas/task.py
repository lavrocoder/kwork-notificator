from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    price: int

    @property
    def url(self) -> str:
        url = f"https://kwork.ru/projects/{self.id}"
        return url

    @property
    def text_for_tg(self) -> str:
        text = f"<b>{self.title}</b>\n{self.description}"
        return text
