book = {}
book['tom']= {
    'name': 'tom',
    'address':'1 green street NY',
    'phone':65765761
}
book['joe']= {
    'name':'joe',
    'address':'1 res street NY',
    'phone':865743678
}
import json
s=json.dumps(book)
print(s)
with open("C://pycharmpractice//book.txt","w") as f:
    f.write(s)