import requests
import re


my_rec = requests.get('http://www.columbia.edu/~fdc/sample.html')
labels = re.findall(r'<h3.*/h3>', my_rec.text)

for i in range(len(labels)):
    labels[i] = re.findall(r'>.*<', labels[i])[0][1:-1]

print(labels)
