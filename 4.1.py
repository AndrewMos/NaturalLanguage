import re
scanner=re.Scanner([
  (r"[\w\.-]+@[\w\.-]+\.[\w\.-]+",  lambda scanner,token:("Mail", token)),
  (r"([0-9]+[\-][0-9]+)", lambda scanner,token:("Endash num", token)),
  (r"([0-9])+",           lambda scanner,token:("Int", token)),
  (r"[A-Za-z]+",          lambda scanner,token:("Word", token)),
  (r"[!?;:,'-]+",         lambda scanner,token:("Punct", token)),
  (r"[\(]",               lambda scanner,token:("LParen", token)),
  (r"[\)]",               lambda scanner,token:("RParen", token)),
  (r"[.]",                lambda scanner,token:("Dot", token)),
  (r"\s\-\s",             lambda scanner,token:("Em dash", token)),
  (r"(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])", lambda scanner,token:("Emoji", token)),
  (r"\s+", None),
])

results, remainder = scanner.scan("The Book! (Tue) 55-88 Milani-lop'ed mss. (-) 123 - test@test.com 😋 😎")
print(results)
