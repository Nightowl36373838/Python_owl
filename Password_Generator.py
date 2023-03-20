"""Generate Passwords that are Hard to Break or Compromise"""

import random

numbers = '0123456789'
Lower_case = 'qwertyuioplkjhgfdsazxvcvbnm'
Upper_case = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
Symbol = '!@#%$&*^()+_?/><|\}{.*'

target = numbers + Lower_case + Upper_case + Symbol
Length_for_Pass = 15

Password = "".join(random.sample(target, Length_for_Pass))
print("Your Generated Password is :", Password)
