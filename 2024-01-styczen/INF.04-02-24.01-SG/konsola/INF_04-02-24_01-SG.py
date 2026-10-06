"""
************************************************
 klasa: ToolLibrary
 opis: Klasa nie posiada żadnych pól i posiada 2 metody statyczne: jedna służy do zliczania wszystkich samogłosek
 w wyrazie, a druga usuwa powtórzenia znaków występujące obok siebie w wyrazie
 metody: count_vowels - zwraca ilość samogłosek w wyrazie
 remove_same_letters -  zwraca wyraz bez powtórzeń liter koło siebie
 autor: <numer zdającego>
************************************************
"""


class ToolLibrary:
    @staticmethod
    def count_vowels(text):
        vowels = "aąeęiouóyAĄEĘIOUÓY"
        if text == "" or text is None:
            return 0
        else:
            vowels_amount = 0
            for i in range(len(text)):
                for j in range(len(vowels)):
                    if text[i] == vowels[j]:
                        vowels_amount += 1
            return vowels_amount

    @staticmethod
    def remove_same_letters(text):
        if text == "" or text is None:
            return ""
        else:
            result = [text[0]]
            for i in range(1, len(text)):
                if text[i] != text[i-1]:
                    result.append(text[i])
            return ''.join(result)


if __name__ == '__main__':
    word = input("Enter a word: ")
    print(ToolLibrary.count_vowels(word))
    print(ToolLibrary.remove_same_letters(word))
