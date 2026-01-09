def translate(phrase):
  translation = "" #empty string, dito aassign
  for letter in phrase: #titignan bawat letter sa phrase
    if letter.lower() in "aeiou": #if yung letter na yon ay may aeiou, 
      if letter.isupper():
        translation = translation + "G"#papalitan yun vowel ng "G"
      else:
        translation = translation + "g"#papalitan yun vowel ng "g"
    else:
      translation = translation + letter#kapag hindi vowel, pprint niya yung LETTER NA IYON ONLY
  return translation #ibabato ng return statement yung value sa function

print(translate(input("Enter a phrase: ")))#remember na argument ang "input("Enter a phrase: ")" dito