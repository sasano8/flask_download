from app import FILE_NAME, DIR_PATH

import requests

res = requests.get("http://localhost:5000/download", stream=True)
res.raise_for_status()

# actual = b"".join(res.iter_lines(1))  # linesは改行コードが消えてしまうので駄目
actual = b"".join(res.iter_content(1))

with open(DIR_PATH + "/" + FILE_NAME, "rb") as f:
    expect = f.read()

# print(expect)
# print(actual)
assert actual == expect
