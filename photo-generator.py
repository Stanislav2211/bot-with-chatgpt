import requests
key='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'

def generate(message):
    url='https://api.openai.com/v1/images/generations'

    headers={
        'Authorization':f'Bearer {key}',
        'Content-Type':'application/json'
    }
    response = requests.post(url,json={'prompt':message},headers=headers)

    if response.status_code==200:
        result = response.json()
        print(result)
    else:
        print("Whooops",response.text)

text='Roronoa Zoro in realistic style'
generate(text)