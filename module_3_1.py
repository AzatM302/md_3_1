calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    a = string
    b = (len(a), a.upper(), a.lower())
    count_calls()
    return b

def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            a = True
            break
        else:
            a = False
            continue
    return a

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)