def is_isogram(word):
  word = word.lower()
  return "true" if len(set(word)) == len(word) else "false"

word = input("Enter a word to know if its a Isogram: ").strip()
print(is_isogram(word))
