valid_email = 'y4dyvptjiq@bheps.com'
valid_password = 'Qwerty!23'
valid_phone = '79366199804'
valid_login = 'rtkid_1676103160736'
valid_ls = '123456789012'
long_phone = '7981725890080'
short_phone = '787531755'
temp_phone_service_url = 'https://receive-smss.com/sms/'
free_phone_url = 'https://receive-sms-free.cc/Free-Russia-Phone-Number/'
not_valid_password = 'VbirfYfCtdtht'
not_valid_firstname = '3g4h5b6d'
free_phones = ['79209199346', '79636792239', '79636791921', '79262772512', '79262748972', '79262266015']


"""Действующие данные для авторизации в системе"""

from faker import Faker
import random

def get_free_phone():
    num = random.randint(0,5)
    return free_phones[num]

def get_confirm_code_from_phone():
    pass

def generate_fake_number():
    number = '7'
    for _ in range(10):
        number = number + str(random.randint(0, 9))
    return number




"""Фейковые данные для авторизации в системе"""

fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()



import settings


#test = settings.fake_email


#settings.fake_phone()






