import requests
url = "https://jsonplaceholder.typicode.com/posts"

titulo= input("digite o titulo: ")
corpo = input("digite o body: ")
usuario= input("digite o id: ")

dados = {
    "title": titulo,
    "body": corpo,
    "id": int(usuario)
}


Post = requests.post(url, json=dados)

resposta = Post.json()

print(Post.status_code)
print(Post.json())

assert Post.status_code == 201
assert resposta["title"] == dados["title"]
assert resposta["body"] == dados["body"]
assert resposta["id"] is not None
