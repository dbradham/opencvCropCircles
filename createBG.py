import os

for filename in os.listdir('C:/Users/daveb_000/Desktop/Classes/remoteSensing/project/neg'):
    s = 'neg/' + filename + '\n' + '\n'
    with open('bg.txt','a') as f:
      f.write(s)
    
