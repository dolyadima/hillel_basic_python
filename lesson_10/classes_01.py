class Cat:
    """I'm increment one to the variable int"""
    pows = 4

    def __init__(self, name, color='black'):
        self.name = name
        self.color = color
        self.home = 'Village'

    def home_cat(self):
        self.home = 'flat'


my_cat = Cat('Barsik', color='Red')
print(vars(my_cat))

print(f'{Cat.pows=}')

file_my = open('temp_03.txt', 'w')
print(my_cat.__dict__, file=file_my)
file_my.close()
