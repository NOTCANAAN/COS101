from languages import hausa
from languages import yoruba
from languages import igbo
from languages import swahili
from languages import zulu

languages = {
"hausa": hausa.translations,
"yoruba": yoruba.translations,
"igbo": igbo.translations,
"swahili": swahili.translations,
"zulu": zulu.translations
}

print("Choose a language")
for lang in languages:
    print(lang)

choice = input("Enter language: ").strip().lower()

if choice not in languages:
    print("Language missing")
    exit()

word = input("Enter English word: ").strip().lower()

if word in languages[choice]:
    print("Translation:", languages[choice][word])
else:
    print("Word missing")