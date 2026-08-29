import re
import math 
import getpass
def analyze_password(password):
  score = 0
  feedback = []
  # check length 
  if len(password) >= 12:
    score += 2
elif len(password) >=8:
    score += 1
else:
   feedback.append("Use at least 8 characters.")
  # check upppercase letters
  if re.search(r"[A-Z]", password):
    score += 1
  else:
   feedback.append("Add uppercase letters")
# check lowercase letters
if re.search(r"[a-z]", password):
  score += 1
else:
  feedback.append("Add lowercase letters")
  # check numbers
  if re.search(r"\d", password):
    score +=1 
else:
    feedback.append("Add numbers")
#check common passwords
common_passwords = [
  "password",
  "123456",
  "12345678",
  "qwerty",
  "abcdefg",
  "admin",
  "letmein",
]
if password.lower() in common_passwords:
                 score = 0
                feedback.append("Avoid common passwords.")
# check repeated characters 
if re.search(r"(.)\1\1",password):
  score -= 1
  feedback.append("Avoid repeating the same character many times.")
  # determine strength 
  if score <= 2:
    strength = "Weak"
elif score <= 4:
  strength = "Medium"
elif score <=5 
  strength = "strong"
else:
  strength = "Very strong"
# estimate entropy 
charset = 0
if re.search(r["a-z]", password):
  charset +=26
if re.search(r["A-Z]", password):
  charset += 26
if re.serach(r"\d", password):
  charset += 10
if re.search(r"[A-Za-z0-9]", password):
   charset += 32 
entropy = 0
 if charset > 0:
   entropy = len(password) *math.log2(charset)
   return strength, score, entropy, feedback
   print("=== Password Strength Analyzer ===")
   password = getpass.getpass("Enter your password: ")

  strength, score, entropy, feedback = analyze_password(password)
print("\nResult")
print("Strength:", strength)
print("Score:",max(score,0), "/7")
print("Estimated entropy:", round(entropy,2), "bits")

if feedback:
  print("\nSuggestions:")

for item in feedback:
  print("-", item)
else:
  print("\NGreat! Your password meets all the basic checks.")
