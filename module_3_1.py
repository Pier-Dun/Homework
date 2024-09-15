calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.upper() == string.upper():
            return True
    return False

# test_string = ["банан", "Яблоко", "АнАнАс", "тОМАт"]
# test_string_2 = ["баНАН", "Яблоко", "ананас", "ТОМАТ", "груша"]
#
# for i in test_string:
#     print(string_info(i))
#
# for i in test_string_2:
#     print(is_contains(i, test_string))

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
