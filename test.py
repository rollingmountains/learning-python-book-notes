# interactive loop
# while True:
#     reply = input('Enter a number: ')
#     if reply == 'stop':
#         break
#     try:
#         num = int(reply)
#     except:
#         print('bad! ' * 8)

#     else:
#         print(num ** 2)

# print('bye')

# while True:
#     reply = input('Enter a number: ')
#     try:
#         num = float(reply)
#         print(num / 10)
#     # raises ZeroDivisionError
#     except Exception as e:
#         # only catches ValueError, not ZeroDivisionError
#         print(f'An error has occured. Details: {e}')

while True:
    reply = input('enter a number: ')
    if reply == 'stop':
        break

    try:
        num = float(reply)
    except:
        print('Bad! ' * 8)
    else:
        if num < 20:
            print(f'{num} is too low')
        else:
            print(num ** 2)
