# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

my_text = 'наиабвопре  ыволрабв оавпроапабв абвыцгрыгвр'

def words_delete(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = words_delete(my_text)
print(my_text)
