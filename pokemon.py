class Pokemon:
    def __init__(self, num, name, page_link):
        self.num = num
        self.name = name
        self.page_link = page_link

    def __str__(self):
        return f"Pokemon(num={self.num}, name={self.name}, link={self.page_link})"