from address import Address
from mailing import Mailing

to_address = Address( "123456", "Москва", "Примерная", "10", "20")
from_address = Address( "365489", "Челябинск", "Ленина", "10", "30")
mailing = Mailing(to_address, from_address, 20000, "ABCD123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, \
{mailing.from_address.home} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, \
{mailing.to_address.street}, {mailing.to_address.home} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей..")



