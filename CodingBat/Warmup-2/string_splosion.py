def string_splosion(str):
    splosion = ''
    for i in range(len(str)):
        splosion += str[:i]
    print splosion + str
string_splosion('Code')
# Solution
'''
def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
'''
