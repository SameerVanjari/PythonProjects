import re

strr = '''Hello bro, my name is deepak tiwari and my email id is deepak@gmail.com,
And I am learning programming on code with harry youtube channel and I have one more
email:"deepak@dt.com"
and some more
email id:<dt@codewithharry.com>

email:"deepak@dt.com.in" and I have one more harrybhai@codewithharry.com
'''

pattern = re.compile(r'\w+@\S+\w')

matches = re.finditer(pattern,strr)
for index,match in enumerate(matches): 
    print(match)
    with open('emails.txt', 'a') as f:
        f.write(f'{index}{match}\n')
    
print("the emails are",matches)

