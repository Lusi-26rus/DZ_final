from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 14 Pro", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 7 Pro", "+79567890123"))

# Выводим весь каталог
print("Каталог смартфонов:")
for phone in catalog:
    print(phone.get_info())