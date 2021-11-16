class book():
    title: str
    author: str
    pages: int
    price: float

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price