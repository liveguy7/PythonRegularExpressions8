import re

txt = "The quick brown\nfox jumps*over the lazy dog."
tmp = re.split(';|,|\*|\n', txt)
print(tmp)

txt = "Clearly, there is no excuse for such behavior"
for m in re.finditer(r'\w+ly',txt):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

txt = "PHP Exercises"
redata = re.compile(re.escape('php'), re.IGNORECASE)
newText = redata.sub('php', 'PHP Exercises')
print(newText)

text = "JelloStoreOverThere"
tmp = re.findall('[A-Z][^A-Z]*', text)
print(tmp)



