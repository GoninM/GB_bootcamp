def read_file(file_name, ) -> list:
    with open(f'./{file_name}', 'r', encoding='UTF-8') as file:
        text = file.read()

        symbols = [",", ".", "!", ";", "?", "-", "«", "»", "—", "\n", "(", ")"]
        text = text.lower()
        for s in symbols:
            text = text.replace(s, "")

        ls = text.split(" ")
        ls = set(ls)
        ls = list(ls)
        ls.remove("")

        ls.sort()
        return ls


def save_file(file_name, words_list):
    with open(f'./{file_name}', 'w', encoding='UTF-8') as file:
        n_words = f'кол-во уникальных слов: {len(words_list)}\n'
        file.write(n_words)
        file.write("Список слов:\n")
        for i, w in enumerate(words_list):
            file.write(f'{i+1}: {w}\n')