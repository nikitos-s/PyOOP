class Animal:

    def __init__(self,sup1 = '_____',sup2 = '_____',sup3 = '_____',sup4 = '_____',sup5 = '_____'):
        self.__spiece = sup1        #Порода
        self.__nick = sup2          #Кличка
        self.__weight = sup3        #Вес
        self.__voice = sup4         #Голос
        self.__sex = sup5           #Пол М/Ж


    def characts(self,spiece,nick,weight):
        self.__spiece = spiece
        self.__nick = nick
        self.__weight = weight

    def voice(self,voice,sex):
        self.__voice = voice
        self.__sex = sex

    def get_voice(self):
        if self.__sex == 'М':
            return (f'Он говорит {self.__voice}')
        else:
            return (f'Она говорит {self.__voice}')

    def get_characts(self):
        return (f'Собака породы {self.__spiece} по кличке {self.__nick} весит {self.__weight} кг')

print('---------------------------------------------------------------------')
Dog0 = Animal('спаниель','Снежинка',10,'вуф-вуф','Ж')
print(Dog0.get_characts())
print(Dog0.get_voice())
print('---------------------------------------------------------------------')
Dog1 = Animal('терьер','Бобик',12,'гав-гав','M')
print(Dog1.get_characts())
print(Dog1.get_voice())
print('---------------------------------------------------------------------')
Dog2 = Animal('бульдог','Рекс',15,'уууу','Ж')
print(Dog2.get_characts())
print(Dog2.get_voice())
print('---------------------------------------------------------------------')
Dog3 = Animal('хаски','Роза',18,'авава','Ж')
print(Dog3.get_characts())
print(Dog3.get_voice())
print('---------------------------------------------------------------------')
Dog4 = Animal('сиба-ину','Валера',9,'ав-ав','M')
print(Dog4.get_characts())
print(Dog4.get_voice())
print('---------------------------------------------------------------------')





