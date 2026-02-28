rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_str)

if (rate< 1):
    rate = 1

if (rate > 5):
    rate = 5

feedback = ""

if rate ==1:
    feedback=input("Раскажите, что нам улучшить?:")
elif rate ==2:
    feedback=input("Что Вам не понравилось?:")
elif rate ==3:
    feedback=input("Что Вам не понравилось?:")
elif rate ==4:
    feedback=input("Почему не пять?:")
else:
    feedback=input("Что больше всего понравилось?:")

print(feedback)