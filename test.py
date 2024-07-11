import requests
import pytest

BASE_URL = 'HTTP://127.0.0.1:5000'
tasks = []

#função para testar a criação de uma tarefa
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa criada",
        "description": "Descrição da nova tarefa criada"
    }
    #metodo para enviar a requisição
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    #verificando o status da requisição
    assert response.status_code == 200
    response_json = response.json()
    #verificando se a mensagem e id existem
    assert "message" in response_json
    assert "id" in response_json
    
    #adiciona o id na lista de tarefas (tasks = [])
    tasks.append(response_json['id'])
    
#função para testar a listagem das tarefa 
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    #Valida se a tarefa (chaves) existe
    assert "tasks" in response_json
    #Valida se todas as tarefa (chaves) existe
    assert "total_tasks" in response.json

#função para testar a listagem de uma tarefa 
def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']
        
#função para testar a alteração de uma tarefa 
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Titulo atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        
        #Nova requisição a tarefa específica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json ["title"] == payload["title"]
        assert response_json ["description"] == payload["description"]
        assert response_json ["completed"] == payload["completed"]
        
#função de teste para deletar de uma tarefa 
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200
        
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 404