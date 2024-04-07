# # a = input().split()
# #
# # a = sorted(a)
# # dict_a = dict(map(lambda x:(x, len(x)), a))
# #
# # b = input().split()
# # rez = []
# #
# # for word in b:
# #     for dict_word, lens in dict_a.items():
# #         if word[:min(len(word), lens)] == dict_word:
# #             rez.append(dict_word)
# #             break
# #     else:
# #         rez.append(word)
# #
# # print(' '.join(rez))
#
#
# # Чтение и сортировка списка слов по длине, чтобы в первую очередь проверять самые короткие слова
# a = sorted(input().split(), key=len)
#
# # Создание словаря, где ключом является слово, а значением - его длина
# # Этот шаг можно оптимизировать, убрав избыточное хранение длины, так как она легко доступна через len()
# dict_a = {word: len(word) for word in a}
#
# # Чтение второго списка слов
# b = input().split()
# rez = []
#
# # Для каждого слова в списке b ищем возможное сокращение в словаре a
# for word in b:
#     for dict_word in a:  # Итерируемся по уже отсортированному списку
#         # Если слово из b начинается с слова из a, используем его как сокращение и прекращаем поиск
#         if word.startswith(dict_word):
#             rez.append(dict_word)
#             break
#     else:
#         # Если сокращение не найдено, оставляем слово без изменений
#         rez.append(word)
#
# print(' '.join(rez))
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def find_shortest_prefix(root, word):
    node = root
    prefix = ""
    for char in word:
        if char in node.children:
            prefix += char
            node = node.children[char]
            if node.is_end_of_word:
                return prefix
        else:
            break
    return word  # Возвращаем исходное слово, если подходящий префикс не найден

# Создание префиксного дерева и добавление в него слов из списка a
root = TrieNode()
for word in sorted(input().split(), key=len):
    insert(root, word)

# Чтение второго списка слов и поиск для каждого слова наиболее короткого префикса
b = input().split()
result = [find_shortest_prefix(root, word) for word in b]

print(' '.join(result))

