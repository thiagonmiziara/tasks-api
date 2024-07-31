# Aplicação de Gerenciamento de Tarefas

Esta é uma aplicação simples desenvolvida em Python utilizando o framework Flask. Ela permite que você gerencie tarefas, criando, visualizando, atualizando e removendo-as.

## Funcionalidades

- **Criar Tarefa**: Você pode criar uma nova tarefa enviando uma solicitação POST para `/tasks`. O corpo da solicitação deve conter um JSON com os campos `title` (obrigatório) e `description` (opcional).

- **Listar Tarefas**: Você pode obter a lista de todas as tarefas existentes enviando uma solicitação GET para `/tasks`. A resposta será um JSON contendo uma lista de tarefas e o total de tarefas.

- **Obter Tarefa por ID**: Você pode obter os detalhes de uma tarefa específica enviando uma solicitação GET para `/tasks/<id>`, onde `<id>` é o ID da tarefa desejada. A resposta será um JSON com os detalhes da tarefa.

- **Atualizar Tarefa**: Você pode atualizar uma tarefa existente enviando uma solicitação PUT para `/tasks/<id>`, onde `<id>` é o ID da tarefa a ser atualizada. O corpo da solicitação deve conter um JSON com os campos `title`, `description` e `completed` atualizados.

- **Remover Tarefa**: Você pode remover uma tarefa existente enviando uma solicitação DELETE para `/tasks/<id>`, onde `<id>` é o ID da tarefa a ser removida.

## Instalação

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
3. Instale as dependências necessárias executando o seguinte comando:

### - `pip install flask`

## Execução

1. Navegue até o diretório do projeto.
2. Execute o seguinte comando para iniciar o servidor:

### - `python app.py`

3. O servidor estará em execução em `http://localhost:5000`.

## Uso

Você pode usar uma ferramenta como o Postman ou o cURL para enviar solicitações HTTP para a API. Aqui estão alguns exemplos:

### Criar Tarefa

```json
curl -X POST -H "Content-Type: application/json" -d '{"title":"Tarefa de Exemplo","description":"Esta é uma tarefa de exemplo"}' http://localhost:5000/tasks
```

### Listar Tarefas

```json
curl http://localhost:5000/tasks
```

### Obter Tarefa por ID

```json
curl http://localhost:5000/tasks/1
```

### Atualizar Tarefa

```json
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Tarefa Atualizada","description":"Descrição atualizada","completed":true}' http://localhost:5000/tasks/1
```

### Remover Tarefa

```json
curl -X DELETE http://localhost:5000/tasks/1
```

Certifique-se de substituir os IDs de exemplo pelos IDs reais das tarefas em sua aplicação.

Divirta-se gerenciando suas tarefas!
