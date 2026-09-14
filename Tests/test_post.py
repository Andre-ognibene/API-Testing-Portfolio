import requests
url = "https://jsonplaceholder.typicode.com/posts"

##titulo= input("digite o titulo: ")
##corpo = input("digite o body: ")
##userID= input("digite o id: ")

dados = {
    "title": "teste",
        "body": "teste",
        "userId": int(2)
}

def test_envio_campo():
    Post = requests.post(url, json=dados)

    resposta = Post.json()

    print(Post.status_code)
    print(Post.json())

    assert Post.status_code == 201
    assert resposta["title"] == dados["title"]
    assert resposta["body"] == dados["body"]
    assert (resposta["userId"]) is not None and (resposta["userId"])!=""
    assert resposta["userId"] == dados["userId"]
