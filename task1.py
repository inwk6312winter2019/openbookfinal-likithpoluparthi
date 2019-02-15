f1= open('Book1.txt','r')
f1=f1.readlines()
def unique_words(f1):
  output=[]
  for line in f1:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in output:
        output.append(word)
  print(output)
def count_the_article(f1):
  count=0
  output=[]
  for line in f1:
    line=line.strip()
    line=line.split()
    for word in line:
      count+=1
  print(count)
count_the_article(f1)
  
