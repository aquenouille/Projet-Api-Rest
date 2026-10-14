#Créer tache pour employé existant 201
def test_create_task(client):
    employee_response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    response = client.post("/tasks/", json={
        "title": "frontend final",
        "description": "Finalize the tool",
        "employee_id": 1
    })
    assert employee_response.status_code == 201
    assert response.status_code == 201

#Créer tache pour employé inexistant 404
def test_create_task_no_employee(client):
    response = client.post("/tasks/", json={
        "title": "frontend final",
        "description": "Finalize the tool",
        "employee_id": 1
    })

    assert response.status_code == 404

#Lister les tâches d'un employé
def test_tasks_list(client):
    employee_response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    response = client.post("/tasks/", json={
        "title": "frontend final",
        "description": "Finalize the tool",
        "employee_id": 1
    })
    response = client.get("/tasks/employee/1")

    assert response.status_code == 200
    assert len(response.json()) == 1

#Mettre à jour le statut d'une tâche → 200
def test_update_task(client):
    employee_response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    task_response = client.post("/tasks/", json={
        "title": "frontend final",
        "description": "Finalize the tool",
        "employee_id": 1
    })

    update_response = client.patch("/tasks/1", json={
        "status": "in_progress"
    })

    assert update_response.status_code == 200

#Mettre à jour avec un statut invalide → 422
def test_update_task_invalid(client):
    employee_response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    task_response = client.post("/tasks/", json={
        "title": "frontend final",
        "description": "Finalize the tool",
        "employee_id": 1
    })

    update_response = client.patch("/tasks/1", json={
        "status": "not_started"
    })

    assert update_response.status_code == 422


#Supprimer une tâche → 204
def test_remove_task(client):
    employee_response = client.post("/employees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@company.com",
        "position": "Developer"
    })

    task_response = client.post("/tasks/", json={
        "title": "frontend final",
        "description": "Finalize the tool",
        "employee_id": 1
    })

    remove_response = client.delete("/tasks/1")

    assert remove_response.status_code == 204

#Supprimer une tâche inexistante → 404
def test_remove_task_invalid(client):
    remove_response = client.delete("/tasks/2")
    assert remove_response.status_code == 404

