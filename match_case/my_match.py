def status_code(code):
    match code:
        case 200:
            print("OK")
        case 400:
            print("BAD REQUEST")
        case 404:    
            print("NOT FOUND")
        case _:
            print("UNKNOWN STATUS")

status_code(200)
status_code(404)
status_code(300)


def is_vowel(vowel):
    match vowel.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("True")
        case _:
            print("False")
is_vowel('a')
is_vowel('U')
is_vowel('c')