import requests
URL = "https://jsonplaceholder.typicode.com/users"
response = requests.get(URL)
postar = requests.post(URL)

DadosPython = response.json()   
print(type(DadosPython)) 

def test_requisicao_users():

    assert response.status_code == 200

    assert response.text !=""

  
    
def test_campos_users():
    for usuario in DadosPython:

        assert (usuario["id"]) is not None and (usuario["id"])!=""
        assert (usuario["name"]) is not None and (usuario["name"])!=""
        assert (usuario["username"]) is not None and (usuario["username"])!=""
        assert (usuario["email"]) is not None and (usuario["email"])!=""
        
def test_tipo_dado():
    for usuario in DadosPython:
        assert isinstance (usuario["id"], int) 
        assert isinstance (usuario["name"], str )
        assert isinstance (usuario["username"], str)
        assert isinstance (usuario["email"], str)
            
def test_ID_unico():
    ids = []
    
    for usuario in DadosPython:
        
        ids.append(usuario["id"])    
        
    assert len (ids) == len (set(ids))
    
def test_email_unico():
    emails = []
    
    for usuario in DadosPython:
        emails.append(usuario["email"])
    
    assert len(emails) == len (set(emails))
    
def test_username_unico():
    usernames = []
    
    for usuario in DadosPython:
        usernames.append(usuario["username"])
        
    assert len (usernames) == len (set(usernames))
    

postar = requests.post(URL)
    


