def count_calls():
    global calls
    calls += 1



def string_info(stroka: str) -> tuple:
    count_calls()
    return len(stroka), stroka.upper(), stroka.lower()



def is_contains(stroka: str, spisok: list) -> bool:
    count_calls()
    # for word in spisok:
    #     if word.lower() == stroka.lower():
    #         return True
    #     else:
    #         return False
    return any(True if word.lower() == stroka.lower() else False for word in spisok)


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)