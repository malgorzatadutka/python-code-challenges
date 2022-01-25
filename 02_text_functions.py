import re
import collections


# counting given sign in a text file
def count_sign(path, sign):
    file = open(path, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    counter = 0
    for letter in text:
        if letter == sign:
            counter += 1
    print(f'\nTotal count of sign {sign} in text is {counter}')


# counting words in a text file
def count_words(path, num_frequent):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print('Total Words:', len(all_words))

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(num_frequent):
            print(word[0], '\t', word[1])


# sorting words in a text file
def sort_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        sorted_words = ' '.join(sorted(all_words))
        print(f'\nSorted words form file "{path}":\n {sorted_words}')


if __name__ == '__main__':
    print('How many top words do you want to have? (pass number):')
    try:
        num = int(input())
    except ValueError:
        print("That's not an int!")
    count_words('02_example.txt', num)
    print('Which sign do you look for?:')
    sign = str(input())
    count_sign('02_example.txt', sign)
    sort_words('02_example.txt')