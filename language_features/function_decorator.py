def requireToken(func):
    def wrapper():
        func('xxx')
    return wrapper

@requireToken
def test(token):
    print(f'hello {token}')



test()