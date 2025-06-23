from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    if hour <= 11:
        message = f'Good morning, {name}-san!'
    elif hour <= 17:
        message = f'Hello, {name}-san!'
    else:
        message = f'Good evening, {name}-san!'
    print(message)

greet('Inoue')

