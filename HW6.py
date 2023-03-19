# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import string
string.punctuation

text = '''Исторический герб города был утверждён 17 марта 1804 года. Верхняя часть представляет собой герб Томской
# губернии: щит разделён на зелёное (верхнее) и золотое (нижнее) поля; по зелёному полю скачет белый конь; в нижней
# части, на золотом фоне — стоящая в поле натурального цвета кузница с орудиями кузнечного ремесла перед ней.
# 8 июля 1970 года решением горисполкома был утверждён новый вариант герба города, предложенный архитектором
# А. И. Выповым. Этот герб представляет собой геральдический щит. На белом поле щита, олицетворяющем сибирскую природу,
# помещено стилизованное изображение разреза доменной печи красного цвета и чёрный квадрат (символизирующий основные
# отрасли промышленности города — металлургическую и угольную), от которого исходят лучи, символизирующие энергию
# солнца, заключённую в угле. В верхней части щита помещается условное изображение стен Кузнецкой крепости, как дань
# уважения к историческому прошлому Кузнецкого края и символ преемственности поколений.После распада СССР городу был
# возвращён исторический герб, но герб советского периода (1970) так и не был отменён, так что одновременно у города
# официально было два герба. 24.04.2018 года официально был учреждён новый герб города. Геральдическое описание:
# В зелёном и золотом пересечённом поле в зелени — серебряный с золотыми гривой, хвостом, копытами и языком конь,
# скачущий по золотой стеннозубчатой, мурованной оконечности и сопровождённый вверху в углах серебряными с золотыми
# сердцевинами и чашелистиками розами; в золоте — червленый обращено бегущий волк; поверх всего — золотой щиток, в
# котором — стоящая на зелёной земле червлёная старинная кузница без видимой передней стены и со сквозным окном в
# задней, в которой — золотые инструменты кузнечного дела: наковальня на чурбаке, меха, вставленные в червлёную
# кирпичную печь, в которой горит золотой же огонь, и сложенные перед ними накрест клещи и молот. Щит увенчан
# муниципальной короной установленного образца.'''

for p in string.punctuation:
    if p in text:
        text = text.replace(p, '')
    text = text.replace('—', '').strip()
print(text)
words = text.lower().split()
count = {}
for element in words:
    if count.get(element, None):
        count[element] += 1
    else:
        count[element] = 1
sorted_values = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(dict(sorted_values[0:10]))




