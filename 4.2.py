import re

text = 'Mr. and Mrs. Goodsirs diary entries. U.S. 1885 year. The story begins in the winter of 1847. For more than a year, HMS Terror and HMS Erebus have been trapped in ice, 28 miles north-northwest of King William Island. The weather has been much colder than normal, the ships tinned provisions are dwindling and often putrid, and the sea ice and landmasses are mysteriously devoid of any wildlife that can be hunted. In addition to the natural dangers, the crews are being stalked and attacked by a monster resembling an immense polar bear. '

print(re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]{2,2}\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', '\n', text))
