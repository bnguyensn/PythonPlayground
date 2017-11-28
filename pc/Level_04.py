import urllib.request
import urllib.error
import re

p = re.compile(r"nothing is (\d+)").search

max_iteration = 400
# n = 16044 // 2
# n = 63579
# n = 4620
# n = 66831 // The end
n = 12345
counter = 0

for i in range(0, max_iteration):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % n
    try:
        res = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        if hasattr(e, "reason"):
            print("We failed to reach a server.")
            print("Reason: ", e.reason)
        elif hasattr(e, "code"):
            print("The server couldn\'t fulfill the request.")
            print("Error code: ", e.code)
        break
    else:
        html = res.read()
        print(html)

        match = p(str(html, encoding="utf-8"))  # The returned html is a byte object, so need to convert to str
        if match:
            counter += 1
            n = match.group(1)
            print(n)
        else:
            break

print(counter)
