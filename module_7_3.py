class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.args = args
        for i in self.args:                 # в примере было сказано, что объекты класса создаются таким образом:
            if ',' not in i:                # WordsFinder('file1.txt, file2.txt', 'file3.txt', ...)
                self.file_names.append(i)   # поэтому, чтобы два имени не считались за одно, решил разделить их
            elif ',' in i:
                while ',' in i:
                    self.file_names.append(i[0:i.index(',')])
                    i = i[i.index(',') +2:]
                self.file_names.append(i)

    def create_file(self, lines):
        self.lines = lines
        for i in self.file_names:
            with open(i, 'w', encoding='utf-8') as file:
                for j in self.lines:
                    file.write(f'{j}\n')

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                _list2 = []
                for line in file:
                    punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for j in punctuation_marks:
                        if j in line:
                            line = line.replace(j, '')
                    line = line.lower()
                    _list = line.split()
                    _list2 += _list
                all_words[i] = _list2
        return all_words

    def find(self, word):
        self.word = word.lower()
        _dict = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                all_words = self.get_all_words()
                if self.word in all_words[i]:
                    index = all_words[i].index(self.word)
                    _dict[i] = index + 1
                else:
                    _dict[i] = None
        return _dict

    def count(self, word):
        self.word = word.lower()
        _dict = {}
        for name, words in self.get_all_words().items():
            _dict[name] = words.count(self.word)
        return _dict

lines = [
    "It's a text for task Найти везде,",
    "Используйте его для самопроверки.",
    "Успехов в решении задачи!",
    "text text text"
    ]

finder2 = WordsFinder('test_file.txt')
finder2.create_file(lines) # Этой функции нет в условии, но не сказано, откуда в файле текст, так что я добавил его сам
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего