from english_words import english_words_set
import random
import string

words = list(english_words_set)


def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word or '\'' in word or "\"" in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    lives = 10
    word = get_valid_word()
    word_letters = set(word)
    word_len = len(word)
    #alphabet = set(string.ascii_uppercase)
    used_letters = set()
    guessed_letters = set()

    while len(guessed_letters) != word_len and lives > 0:
        word_letters_list = [letter if letter in used_letters else '-' for letter in word]
        if not('-' in word_letters_list):
            print('You win!!!','word is', ''.join(word_letters))
            exit(0)
        print('Current word:', ' '.join(word_letters_list))
        user_letter = input('Write letter: ').upper()
        if not(user_letter in used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                guessed_letters.add(user_letter)
            else:
                lives -= 1
                print('Wrong letter. You have {} liver'.format(lives))
                if lives == 0:
                    print('You lost. The word was ', word)
                    exit(0)
        elif user_letter in used_letters:
            print('You used this letter')
    print('you win! word is {}'.format(word))

if __name__ == '__main__':
    hangman()
