import re

text = "<@!13698497280056574477> good"
pattern = r"<@!\d+>\s*(.*)"

match = re.search(pattern, text)
if match:
    extracted_text = match.group(1)
    print(extracted_text.strip())  # 去除前导和尾随空格
else:
    print("未找到匹配的内容")