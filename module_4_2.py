def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# inner_function() является локальной функцией test_function(), к ней нельзя обращаться не из её объемлющего или локального пространства имен

test_function()
