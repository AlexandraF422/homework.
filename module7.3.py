import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read()
                text = text.lower()
                text = text.strip('.,:;=!?- ')
                words = text.split()

                all_words[file_name] = words

        return all_words

    def find(self, word):
        word_found = {}

        for name, words in self.get_all_words().items():
            for i, w in enumerate(words):
                if w == word:
                    word_found[name] = i + 1
                    break

        return word_found

    def count(self, word):
        word_count = {}

        for name, words in self.get_all_words().items():
            count = 0
            for w in words:
                if w == word:
                    count += 1
            word_count[name] = count

        return word_count


# Пример использования
finder = WordsFinder('test_file.txt')
all_words = finder.get_all_words()
print(all_words)

found_word = finder.find('text')
print(found_word)

count_word = finder.count('text')
print(count_word)