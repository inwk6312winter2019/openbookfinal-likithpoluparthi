f1= open(r"access.log",'r')
def fire_chrome_els():
  frie=0
  chrome=0
  for line in f1:
      if "Firefox" in line:
         frie+=1
      elif "Chrome" in line:
         chrome+=1
  print (frie, chrome)

fire_chrome_els()
    
