# # salary = 1000
# # print('Ваша месячная зарплата составляет ' + str(salary) + ' y. e.')

# #print(1 + True) # True = 1 | 1 + 1 = 2




# # my_string = 'Hello World!'
# # print(my_string.upper())
# # print(my_string.lower())
# # print(my_string.capitalize())
# # print(my_string.replace('Hello', 'Goodbye'))
# # #print(len(my_string))
# # print(my_string.title())
# # print(my_string)
# # #print() # выводит пустую строку (разрыв строки)
# # new_string = my_string.upper()


# # форматирование строк (f-строки)
# # name = 'andrey'
# # age = 25
# # print(f'Меня зовут {name}. Я родился в {2022-age} году.')
# # lang = 'python'
# # my_string = f'Hello, my name is {name.title()}, I know {lang} a bit'
# # print(my_string)

# # Срезы
# # my_string = 'Hello World'
# # print(my_string[2])
# # print(my_string[-4])
# # print(my_string[0:5])
# # print(my_string[0:8:2])
# # print(my_string[6:])
# # print(my_string[:5])
# # print(my_string[::-1]) # перевернет строку справа-налево
# # print(my_string[:5:-1])

# # Списки
# # Списки можно складывать
# # del(list[index]) # удаляет элемент из списка по индексу
# # .remove(el) # удаляет указанный элемент из списка
# # .append(el) # позволяет добавить элемент в список
# # .count(el) # считает количество вхождений элемента в список
# # .index(el) # позволяет узнать индекс элемента в списке
# # .reverse() # разворачивает список
# # sorted(list) # сортирует список

# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
# income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]
# # print(month_list[0])
# # print(month_list[-1])
# # print(income_by_month[-4][0]) # чтобы достать из списка элемент - надо поставить еще одни квадратные скобки с указанием индекса нужного элемента

# # print(income_by_month[0:2])
# # print(income_by_month[-8:-6][1])

# # income_by_months[0][1] = 13100
# # print(income_by_months)

# #my_string = 'Hello World'
# #my_string[0] = 'h'
# #print(my_string)
# # income_by_months_2 = [['Nov', 15400], ['Dec', 17000]]
# # income_by_months = income_by_months + income_by_months_2
# # #print(income_by_months)
# # # del(income_by_months[-1])
# # # print(income_by_months)
# # month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# # month_list.remove('Jan') # удаляет элемент январь
# # #print(month_list)
# # income_by_months.append(['Dec', 17000]) # добавляет элемент в КОНЕЦ
# # #print(income_by_months)
# # income_by_months.insert(2, 111111) # добавляем элемент(на какую позицию вставить, что вставить)
# # print(income_by_months)
# income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]
# # income_by_months[0].remove('Jan')
# #income_by_months.insert(2, 1111,)

# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
# # print(income_list.index(14000))

# # # month_list.reverse()
# # # print(month_list)
# # # print(sorted(income_list, reverse=True))
# # # print(income_list)
# # income_list.sort()
# # print(income_list)

# # queries_string = "смотреть сериалы онлайн, новости спорта, афиша кино, курс доллара, сериалы этим летом, курс по питону, сериалы про спорт"

# # print(queries_string.split(','))
# # print('\t'.join(['Столбец 1', 'Столбец 2', 'Столбец 3']))

#user_data = ('Петров', 'Николай', 'Иванович', 25)
# company_tuple = ('Orange', 100000, 20000)
# company_name, capitalization, personal = company_tuple
# print(company_name)
# print(capitalization)
# print(personal)










# x = 7
# while x != 0:
#     if x % 2 == 0:
#         print(x, '- even number')
#     else:
#         print(x, '- odd number')
#     x -= 1w

# x = ''
# count = 0
# while x != 0:
#     x = int(input('insert the number'))
#     count += x
# print(count)    

# while True:
#     x = input('insert the command')
#     if x == '1':
#         pass
#     elif x == '2':
#         pass
#     elif x == 'quit':
#         break

# company_name = 'Orange'
# for letter in company_name:
#     letter  = letter.capitalize()
#     print(letter)

# companies_capitalization = [['orange', 1.3], ['maxisoft', 1.5], ['headbook', 0.8], ['nicola', 2.2 ]]
# # for company in companies_capitalization:
# #     print(company)
# #     print(f"{company[0]}'s capitalization is {company[1]} ")

# for company, cap in companies_capitalization:
#     print(f"{company}'s capitalization is {cap} ")    




#ДЗ1 Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Andrey']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# boys.sort()
# girls.sort()
# pair = zip(boys, girls)
# if len(boys) != len(girls):
#     print('someone can be left alone')
# else:
#     for love in pair:
#         print(list(love))

#phrase = '640кб должно хватить для любых задач. Билл Гейтс (по легенде)'

# for letter in phrase:
#     if letter == ' ':
#         break
#     print(letter, end='')

# for letter in phrase:
#     if letter == ' ':
#         continue
#     print(letter, end='')

# for letter in phrase:
#     if letter == ' ':
#         pass
#     print(letter, end='')

# professions = ['IT', 'Physics', 'Math']
# persons = [['Гейтс', 'Джобс', 'Возняк'], ['Эйнштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]
# for pro, names in zip(professions, persons):
#     print(f' {pro}:')
#     for name in names:
#         print(name)
#     print()


# ДЗ2 Имеется структура данных cook_book, в которой хранится информация об ингредиентах блюд и их количестве в расчете на одну порцию:
# cook_book = [['салат',[['картофель', 100, 'гр.'],['морковь', 50, 'гр.'],['огурцы', 50, 'гр.'],['горошек', 30, 'гр.'],['майонез', 70, 'мл.'],]],['пицца',  [['сыр', 50, 'гр.'],['томаты', 50, 'гр.'],['тесто', 100, 'гр.'],['бекон', 30, 'гр.'],['колбаса', 30, 'гр.'],['грибы', 20, 'гр.'],],],['фруктовый десерт',[['хурма', 60, 'гр.'],['киви', 60, 'гр.'],['творог', 60, 'гр.'],['сахар', 10, 'гр.'],['мед', 50, 'мл.'],  ]]]
# persons = 5
# for dish in cook_book:
#     print(dish[0] + ':')
#     for ingridients in dish[1]:
#         print(ingridients[0], persons * int(ingridients[1]), ingridients[2])
#     print()

# for dish, ingridients in cook_book:
#     print(f' {dish}:')
#     for ingridient in ingridients:
#         to_print =''
#         for i in ingridient:
#             to_print = to_print + f"{i} |"
#         print(to_print)

# for dish, ingridients in cook_book: 
#     print(f' {dish}:') 
#     for ingridient in ingridients: 
#         for el in [ingridient][0]: 
#           print(el, end=', ') 
#         print() 
#     print()

# def menu():
#   for menu in cook_book:
#     print("\n" + "-" * 21 + "\n")
#     print(menu[0].capitalize() + ":" + "\n")

#     for product, quantity, unit in menu[-1]:
#       print(f"{product.lower()}, {str(round(quantity * person, 2))} {unit}")