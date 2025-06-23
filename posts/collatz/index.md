---
name: True to 1's values
date: 2025-06-23
tags: code, python
---

I've recently dug up a small code I submitted last year to
[International Obfuscated Python Code Competition](https://pyobfusc.com/).
It didn't win unfortunately, but I decided to post it nevertheless.
Below is how it looks (you can also download it [here](./script.py)):

{{: code "script.py" :}}

It should run on Python > 3.8, and accepts one optional integer argument:

```
$ python3 collatz.py 10
```

The code heavily uses `True` to obfuscate all the arithmetic and indexing operations.
This works because booleans in Python (unlike in some other languages) are a subclass
of the integer type, and `True` always evaluates to `1` in numeric contexts.
The same value `1` is mirrored throughout the whole implementation:
* the code is one long expression
* it implements [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
(operations that eventually transform all positive integers to 1)
* and it's a calligram that resembles the stylised digit.
