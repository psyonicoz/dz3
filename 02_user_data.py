def info(name, surname, year_birth, city, e_mail, phone):
    return f'имя {name}, фамилия {surname}, год рождения {year_birth}, город проживания {city}, email {e_mail}, телефон {phone}'


name, surname, year_birth, city, e_mail, phone = list(map(str, input('Введите данные пользователя через пробел: \nимя, фамилия, год рождения, город проживания, email, телефон ').split()))

print(info(name, surname, year_birth, city, e_mail, phone))
