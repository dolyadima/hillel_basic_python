l1: list = [i for i in range(10)]
l2: list = [i+i for i in range(10)]
l3: list = [i if i % 2 == 0 else '#' for i in range(10)]
l4: list = [i//2 for i in range(10) if i % 2 == 0]
l5: list = [(i, i*10) for i in range(10)]
print(f'{l1=}\n{l2=}\n{l3=}\n{l4=}\n{l5=}\n')

d1: dict = {k: v for k, v in {1: 2, 3: 4, 5: 6}.items()}
d2: dict = {'key'+str(i): i for i in [1, 2, 3, 5, 8] if i != 3}
d3: dict = {i: len(i) for i in ['flower', 'bread', 'tea', 'meat']}
d4: dict = {i.lower(): i.upper() for i in ['Date', 'NamE', 'caR', 'diGiT']}
d5: dict = {i[0]: i[1] for i in [
    (1, 2.0),
    ('q', 'asd'),
    (hash('salt'), [1, 2, 3]),
    (frozenset('set'), 'text')
]}
print(f'{d1=}\n{d2=}\n{d3=}\n{d4=}\n{d5=}\n')

s1: set = {i for i in range(10)}
s2: set = {i.capitalize() for i in 'red green blue green blue red'.split()}
s3: set = {int(i) for i in [10, '20', 3.5, 30, '30', 2*15]}
s4: set = {0 if i % 2 == 0 else i for i in range(20)}
s5: set = {i['auto'] for i in [
    {'auto': 'BMW', 'year': 1992},
    {'auto': 'Mercedes', 'year': 2015},
    {'auto': 'Volvo', 'year': 2007},
    {'auto': 'Mercedes', 'year': 2021}
] if i['year'] > 2000}
print(f'{s1=}\n{s2=}\n{s3=}\n{s4=}\n{s5=}\n')
