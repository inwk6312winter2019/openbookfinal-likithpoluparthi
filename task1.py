f1= open('Book1.txt','r')
f1=f1.readlines()

"""	 	task 1.1	 """
def unique_words(f1):
  output=[]
  for line in f1:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in output:
        output.append(word)
  print(output)
#unique_words(f1)

""" 		task 1.2	"""
def count_the_article(f1):
  count=0
  output=[]
  for line in f1:
    line=line.strip()
    line=line.split()
    for word in line:
      count+=1
  print(count)
#count_the_article(f1)

"""           task 1.3            """
def sorted_words(f1):
  output=[]
  list2=[]
  for line in f1:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in output:
        output.append(word)
  print(sorted(output[::-1], key = len))
#sorted_words(f1)


"""             task 1.4             """ 
def character_word_count(f1):
  dict1=dict()
  for line in f1:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
             dict1[word]=1
      elif word in dict1:
             dict1[word]+=1
  print(dict1)

#character_word_count(f1)


"""		task1.5		"""

def starts_with_vow(f1):
  count=0
  vow=("a","e","i","o","u")
  for line in f1:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word[0] in vow:
        count+=1
  print count
starts_with_vow(f1)
