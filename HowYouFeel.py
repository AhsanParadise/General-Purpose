#  ========== ========== ============ Useful python code for beginners ============ ========= =========  #


# Intro ====
def my_name(name, age):
    print(f"Hi,{name}. Nice to meet you.")
    print(
        f"You are {age} years old. Maybe you will feel the flavors of youth.")


name = input("What is your name: ")
birth_year = input('Birth year: ')
age = 2020 - int(birth_year)
my_name(name, age)

# Extra ====

if len(name) < 3:
    print("Name must be at least 3 characters. But you are done.")
elif len(name) > 50:
    print("Name can't be more than 50 characters. But it's okay.")


if 0 < age < 5:
    print("You are a badass. Also, you are cute.")
elif age > 100:
    print("You are a Ghost. How can you live more than 100 years?")
else:
    print('You never exist.')

# Weight ===

weight = int(input('Your weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted_to_kilo = weight * 0.45
    print(f"You are {converted_to_kilo} kilos")
elif unit.upper() == "K":
    converted_to_pound = weight // 0.45
    print(f"You are {converted_to_pound} pounds")
else:
    print("You entered an invalid option")

# Emojis ====


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "You are happy.",
        ":(": "You are sad.",
        ":[": "You are angry.",
        ":/": "You are confused.",
        "zzz": "You are sleeping.",
        ":|": "You have nothing to say."
    }
    output = ""
    for word in words:
        output += emojis.get(word, "(⌐■_■) Bad Luck") + " "
    return output


message = input("How you feel? (show some emojis) : ")
print(emoji_converter(message))


# G O O D   L U C K # +++++++++++++++
