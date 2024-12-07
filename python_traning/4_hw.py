# class Rectangle:
#     def __init__(self, widht, height):
#         self.widht =widht
#         self.height= height
#
#     def square(self):
#         result = self.widht*self.height
#         print(f'Площадь прямоугольника - {result}')
#
#     def perimeter(self):
#         result = 2*(self.widht + self.height)
#         print(f'Периметр прямоугольника - {result}')
# rec1=Rectangle(4,5)
# rec2=Rectangle(10,10)
# rec3=Rectangle(5,7)
# rec1.square()
# rec1.perimeter()
# rec2.square()
# rec2.perimeter()
# rec3.square()
# rec3.perimeter()


# class Math:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def addition(self):
#         print(f'Сумма этих чисел равна {self.a+self.b}')
#     def multiplication(self):
#         print(f'Произведение этих чисел равно {self.a*self.b}')
#     def division(self):
#         print(f'Результат деления этих чисел равен {self.a/self.b}')
#     def subtraction(self):
#         print(f'Разность этих чисел равна {self.a-self.b}')
#
# obj = Math(5,10)
# obj.addition()
# obj.multiplication()
# obj.division()
# obj.subtraction()

class Button:
    type: str='Кнопка'
    def __init__(self, text, loc=None):
        self.text=text
        self.loc=loc

    def click(self):
        print(f'Клик по кнопке {self.text}')

text_box=Button('Text Box')
check_box=Button('Check Box')
radio_button=Button('Radio Button')
web_tables=Button('Web Tables')
buttons=Button('Buttons')
links=Button('Links')

broken_links_images=Button('Broken Links - Images')
upload_and_download=Button('Upload and Download')
dynamic_properties=Button('Dynamic Properties')
practice_form=Button('Practice Form')
browser_windows=Button('Browser Windows')
alerts=Button('Alerts')
frames=Button('Frames')
nested_frames=Button('Nested Frames')
modal_dialogs=Button('Modal Dialogs')
accordian=Button('Accordian')
auto_complete=Button('Auto Complete')
date_picker=Button('Date Picker')
slider=Button('Slider')
progress_bar=Button('Progress Bar')
tabs=Button('Tabs')
tool_tips=Button('Tool Tips')
menu=Button('Menu')
select_menu=Button('Select Menu')
sortable=Button('Sortable')
selectable=Button('Selectable')
resizable=Button('Resizable')
droppable=Button('Droppable')
dragabble=Button('Dragabble')
login=Button('Login')
book_store=Button('Book Store')
profile=Button('Profile')
book_store_api=Button('Book Store API')