# class Button:
#     type: str='Button'
#     color: str='red'
#     def __init__(self, text, link):
#         self.text=text
#         self.link=link
#
# home = Button('Home','/home')
# catalog_msk=Button('Catalog','/msk/catalog')
#
# print(home.text)
# print('Button '+home.text+' to lint '+home.link)
# print(home.type)
# print(home.color)

# class ButtonTwo:
#
#     def __init__(self, text, link, loc):
#         self.text=text
#         self.link=link
#         self.loc=loc
#
#     def click(self):
#         return 'Click on locator - {}'.format(self.loc,self.link)
#
# home_two = ButtonTwo('Home','/home', 'button#home')
# print(home_two.click())

# class Input:
#     def __init__(self, text, loc):
#         self.text=text
#         self.loc=loc
#
#     def click(self):
#         return 'Текст - {}, a  расположение - {}'.format(self.text, self.loc)
#
# class Button:
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
#     def click(self):
#         return 'Текст - {}, a  расположение - {}'.format(self.text, self.loc)
# class Title:
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
#     def click(self):
#         return 'Текст - {}, a  расположение - {}'.format(self.text, self.loc)
#
# class Link:
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
#     def click(self):
#         return 'Текст - {}, a  расположение - {}'.format(self.text, self.loc)
#
# input = Input('input','input#loc')
# button = Button('button','button#loc')
# title = Title('title','title#loc')
# link = Link('link','link#loc')
#
# print(input.click())
# print(button.click())
# print(title.click())
# print(link.click())

#задача 2
# class Page:
#     def __init__(self, url):
#         self.url = url
#     def get(self):
#         print(self.url)
#
# home = Page('dfewwer')
# home.get()

#задача 3
class Soda:
    def __init__(self, additive= None):
        self.additive=additive

    def show_my_drink(self):
        if self.additive:
            print(f'Газировка и {self.additive}')
        else:
            print('Обычная газировка')

soda = Soda()
soda.show_my_drink()
fanta = Soda('orange')
fanta.show_my_drink()
