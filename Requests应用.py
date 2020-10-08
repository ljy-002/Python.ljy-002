import requests


Web_gitignore=requests.get('https://ljy-002.github.io/Web-gitignore.github.io/')

print(Web_gitignore)
print(type(Web_gitignore))
try:
    print(int(Web_gitignore),'int')
except :
    print(str(Web_gitignore),'str')
else:
    print(float(Web_gitignore),'float')

for i in range(len(str(Web_gitignore))):
    print(Web_gitignore[i])
