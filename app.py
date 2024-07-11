from flask import Flask, request, jsonify
from models.task import Task

#cria aplicação Flask
app = Flask(__name__)

#Armazena as tarefas na lista tasks = []
tasks = []

#Variavel para iniciar a tarefa com id 1
task_id_control = 1

# Criação da rota task com o metodo POST
# Metodo para criar as tarefas (creat_task())
@app.route('/tasks', methods=['POST'])
def creat_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

# Metodo para listar todas as tarefas (get_tasks())
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)        
            }
    return jsonify(output)

# Metodo para listar somente uma tarefa (get_task())
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
#    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message:" "Tarefa não encontrada"}), 404 

# Metodo para atualização de tarefa (update_task())
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    #função para percorrer a lista de tarefas para verificar se existe ou não
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        
    #condição caso a tarefa não for encontrada
    if task == None:
        return jsonify({"message:" "Tarefa não encontrada"}), 404 
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

# Metodo para atualização de tarefa (delete_task())
@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    #função para percorrer a lista de tarefas para verificar se existe ou não
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        
    #condição caso a tarefa não for encontrada
    if not task:
        return jsonify({"message:" "Tarefa não encontrada"}), 404 
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

#modo de execução de desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)
