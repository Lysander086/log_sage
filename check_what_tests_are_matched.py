import unittest
loader = unittest.TestLoader()
suites = loader.discover(".", pattern="*_test.py")
print("start")
for suite in suites._tests:
    for cls in suite._tests:
        for m in cls._tests:
            print(m.id())

