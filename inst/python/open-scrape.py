from sys import version_info

if version_info >= (3,0):
    exec(open("scrape.py"))
else:
    vars = {}
    execfile("scrape.py", vars)
