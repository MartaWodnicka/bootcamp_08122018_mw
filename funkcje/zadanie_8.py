def bold(funkcja):
    def wrapper(*args, **kwargs):
        return f'<b>{funkcja(*args, **kwargs)}</b>'

    return wrapper


def italic(funkcja):
    def wrapper(*args, **kwargs):
        return f'<i>{funkcja(*args, **kwargs)}</i>'

    return wrapper

@bold
@italic
def foo(arg):
    return f'To jest {arg}'


def test_decorated_foo():
    assert foo("x") == '<b><i>To jest x</i></b>'