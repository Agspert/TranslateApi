from googletrans import Translator
import googletrans


def print_output(sentence):
    translator = Translator()
    supported = ["hi","or","bn","kn","mr","ne", "pa","gu","ta","te", "as"]
    translated =[]
    for language in supported:
        translate= translator.translate(sentence, dest=language)
        print(translate.text)
        translated.append(translate)
    return translated

if __name__ == '__main__':
    print(print_output('Hello, world'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
