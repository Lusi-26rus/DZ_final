from Address import Address
from Mailing import Mailing

# Создаем адреса
from_addr = Address(
    index="123456",
    city="Москва",
    street="Ленина",
    house="15",
    apartment="78"
)

to_addr = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="25",
    apartment="12"
)

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="RF123456789RU"
)

# Форматируем и выводим информацию
print(f"Отправление {mailing.track} "
      f"из {mailing.from_address.get_full_address()} "
      f"в {mailing.to_address.get_full_address()}. "
      f"Стоимость {mailing.cost} рублей.")