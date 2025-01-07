class Analyze_text:
    def __init__(self):
        pass

    @staticmethod
    def count_vowel(text):
        if not text:
            return 0

        sum = 0
        vowels = ["a", "e", "i", "o", "u", "y", "ę", "ą"]
        for i in text.lower():
            if i in vowels:
                sum += 1
        return sum

    @staticmethod
    def remove_duplicates(text):
        if not text:
            return ""

        result = [text[0]]
        for i in range(1, len(text)):
            if text[i] != text[i - 1]:
                result.append(text[i])

        return ''.join(result)


text = input("Wprowadź łańcuch do przetestownia: ")
print(f"Ilość samogłosek: {Analyze_text.count_vowel(text)}")
print(f"Bez powtórzeń: {Analyze_text.remove_duplicates(text)}")
