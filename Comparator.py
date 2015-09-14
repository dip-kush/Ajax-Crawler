from difflib import SequenceMatcher


text1 = open("a.html").read()
text2 = open("c.html").read()
m = SequenceMatcher(None, text1, text2)
print m
print m.ratio()
