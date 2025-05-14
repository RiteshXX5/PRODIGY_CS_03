import string

def evaluate_password(password):
    length_score = 0
    upper_score = 0
    lower_score = 0
    digit_score = 0
    special_score = 0

    #score components

    if len (password)>=8:
      length_score =1

    for ch in password:
      if ch.isupper():
        upper_score =1
      elif ch.islower():
        lower_score =1
      elif ch.isdigit():
        digit_score = 1
      elif ch in string.punctuation:
        special_score = 1

    #total strength score out of 5
    total_score = length_score + upper_score + lower_score + digit_score + special_score

    # feedback

    suggestions = []
    if not length_score:
      suggestions.append("Password must be at least 8 characters long.")
    if not upper_score:
      suggestions.append("Password must contain at least one uppercase letter.")
    if not lower_score:
      suggestions.append("Password must contain at least one lowercase letter.")
    if not digit_score:
      suggestions.append("Password must contain at least one digit.")
    if not special_score:
      suggestions.append("Use Spacial characters like @, !, #, etc")

    #final evaluation

    if total_score == 5:
      strength = "Very Strong"
    elif total_score >=4:
      strength="strong"
    elif total_score >=3:
      strength="Moderate"
    else:
      strength="Weak"

    return strength, suggestions



def main():
  print("Passwore strength checker")
  user_password= input("Enter a password to evaluate:")

  strength, feedback= evaluate_password(user_password)

  print(f"\nPassword Strength: {strength} ")
  if feedback:
    print("suggestions to improve:")
    for suggestion in feedback:
      print("-", suggestion)

  else:
    print("Your password looks great")

if __name__=="__main__":
  main()
