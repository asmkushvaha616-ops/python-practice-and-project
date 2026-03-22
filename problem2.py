# WAP to fill in a letter template given below with name and date
letter='''Dear <|Name|>,
        You are selected!
        <|Date|>'''
# here  used chaning of replace function
print(letter.replace("<|Name|>","Ashmi").replace("<|Date|>","12/10/2025"))