class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        split = []
        for file in self.file_names:
            with open(file, encoding='utf-8') as file_opened:
                for line in file_opened:
                    for char in [',', '.', '=', '!', '?', ';', ':']:
                        line = line.replace(char, '')
                    line = line.replace(' - ', ' ')
                    split += line.lower().split()
                all_words[file] = split
        return all_words

    def find(self, word):
        position = 0
        for k, v in self.get_all_words().items():
            for i in v:
                position += 1
                if word.lower() == i:
                    return {k: position}

    def count(self, word):
        count_of_words = 0
        for k, v in self.get_all_words().items():
            for i in v:
                if word.lower() == i:
                    count_of_words += 1
            return {k: count_of_words}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего