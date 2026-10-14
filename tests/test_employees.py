#Créer employé avec données + validation
def test_create_employee(client):
    response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })
    assert response.status_code == 201

#Lister employé liste vide
def test_list_employees_empty(client):
    response = client.get("/employees/")

    assert response.status_code == 200
    assert len(response.json()) == 0

#Lister employé
def test_list_employees(client):
    client.post("/employees/", json={
        "first_name": "JOhn",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })
    
    response = client.get("/employees/")
    
    assert response.status_code == 200
    assert len(response.json()) == 1

#Récupérer employé existant -> 200
def test_get_employees(client):
    client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json()["first_name"] == "John"

#Récupérer employé inexistant == 404
def test_get_employee_not_found(client):
    response = client.get("/employees/1")

    assert response.status_code == 404

#Créer un employé avec email deja existant == 400
def test_create_employee_created(client):
    response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })
    response = client.post("/employees/", json={
        "first_name": "Jacques",
        "last_name": "Doer",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    assert response.status_code == 400      #400 pour email deja prise

#Créer un employé avec données manquantes == 422
def test_create_employee_missing(client):
    response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
    })

    assert response.status_code == 422