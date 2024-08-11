#Напишите программу, которая берет исходное количество евро, записанное в переменную euros_count,
#переводит евро в доллары и выводит на экран. Затем полученное значение переводит в юани и выводит 
#на новой строчке.

#Пример вывода для 100 евро:
#125.0
#863.75

#Считаем, что:
#- 1 евро = 1.25 долларов
#- 1 доллар = 6.91 юаней


euros_count = 100


dollar_per_euros = 1.25
yuans_per_dollar = 6.91

dollar_count = euros_count * dollar_per_euros
print(dollar_count)

yuans_count = dollar_count * yuans_per_dollar
print(yuans_count)

