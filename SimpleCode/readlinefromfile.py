content = open("dummy", "r").read().splitlines()
for line in content:
    open("dummy", "a").write('\n'+line.upper())

print(content)