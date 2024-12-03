def all_variants(text):
    for len_ in range(1, len(text) + 1):
        for strt in range(len(text) - len_ + 1):
            yield text[strt:strt + len_]

a = all_variants("abc")
for i in a:
    print(i)