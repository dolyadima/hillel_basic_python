def test_function(function, value):
    try:
        assert function() == value, 'expected value not equal function result'
        return value
    except AssertionError as e:
        print(f'error: "{e}" in function: "{function.__name__}"')
        return ''

x = 123
y = 456
