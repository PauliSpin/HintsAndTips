# https://www.youtube.com/watch?v=yr6E7FwK_Hw&list=TLPQMTUwNTIwMjCoy-WyKiwQdA&index=2

c = compile('a + b', 'a.py', 'eval')
print(c)
print(eval(c, {'a': 1, 'b': 2}))
