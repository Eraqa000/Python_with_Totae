slovar = {
    'a' : '1',
    'b' : '2',
    'c' : '3',
    'd' : '4',
    'e' : '5'
}

slovar['a'] = 5
slovar.update({'e' : '1'})
print(slovar)

slovar.pop('b')
print(slovar)


slovar.update({'new_key' : 'new_value'})
print(slovar)
