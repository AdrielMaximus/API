```markdown
# CRUD API com Flask

Este projeto é uma API simples construída com Flask para gerenciar refeições fictícias (meals). Ele implementa as operações CRUD (Create, Read, Update, Delete), permitindo listar, visualizar, atualizar e deletar refeições de uma lista simulada.

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado:
- **Python 3.x**  
- **Flask**: Instale-o com o comando:
  ```bash
  pip install flask
  ```

## Endpoints da API

### 1. Obter todas as refeições
- **Endpoint:** `GET /meals`  
- **Descrição:** Retorna uma lista com todas as refeições cadastradas.  
- **Exemplo de Resposta:**
  ```json
  [
    {
      "id": 1,
      "name": "whopper with fries and a shake",
      "franchise": "Burger King"
    },
    {
      "id": 2,
      "name": "Mcchiken with extra ketchup",
      "franchise": "Mcdonalds"
    },
    {
      "id": 3,
      "name": "20 chicken tenders",
      "franchise": "KFC"
    }
  ]
  ```

### 2. Obter uma única refeição
- **Endpoint:** `GET /meals/<id>`  
- **Descrição:** Retorna uma refeição específica com base no seu `id`.  
- **Exemplo de Resposta:**
  ```json
  {
    "id": 1,
    "name": "whopper with fries and a shake",
    "franchise": "Burger King"
  }
  ```

### 3. Atualizar uma refeição
- **Endpoint:** `PUT /meals/<id>`  
- **Descrição:** Atualiza os dados de uma refeição específica com base no `id`.  
- **Payload de Exemplo:**
  ```json
  {
    "name": "Updated Meal",
    "franchise": "Updated Franchise"
  }
  ```
- **Exemplo de Resposta:**
  ```json
  {
    "id": 1,
    "name": "Updated Meal",
    "franchise": "Updated Franchise"
  }
  ```

### 4. Deletar uma refeição
- **Endpoint:** `DELETE /meals/<id>`  
- **Descrição:** Remove uma refeição específica da lista com base no `id`.  
- **Exemplo de Resposta:** Retorna a lista atualizada de refeições:
  ```json
  [
    {
      "id": 2,
      "name": "Mcchiken with extra ketchup",
      "franchise": "Mcdonalds"
    },
    {
      "id": 3,
      "name": "20 chicken tenders",
      "franchise": "KFC"
    }
  ]
  ```

## Como Executar

1. Salve o código em um arquivo chamado `app.py`.  
2. Abra o terminal e navegue até o diretório onde o arquivo foi salvo.  
3. Execute o comando:  
   ```bash
   python app.py
   ```
4. A API estará disponível em `http://localhost:5000`.

## Testando a API

Você pode testar os endpoints utilizando ferramentas como:  
- **Postman**  
- **cURL** no terminal  
- Extensões de navegador como **Rest Client**  
- Scripts em linguagens como Python ou JavaScript.  

## Estrutura do Código

- **`meals`**: Lista simulada que funciona como um banco de dados para as refeições.  
- **Endpoints CRUD:**  
  - `GET /meals`: Obtem todas as refeições.  
  - `GET /meals/<id>`: Obtem uma refeição específica.  
  - `PUT /meals/<id>`: Atualiza os dados de uma refeição.  
  - `DELETE /meals/<id>`: Remove uma refeição.  

## Configurações Extras

- **Porta:** A API roda na porta `5000` por padrão, mas pode ser alterada diretamente no código na linha `app.run(port=5000)`.  
- **Modo Debug:** O modo `debug=True` está ativado, permitindo recarregar o servidor automaticamente ao modificar o código.  

## Melhorias Futuras

1. Adicionar persistência de dados utilizando um banco de dados (SQLite, PostgreSQL, etc.).  
2. Implementar autenticação para proteger os endpoints.  
3. Adicionar validações mais robustas para os dados enviados pelo cliente.  
4. Criar uma interface web para facilitar o uso da API.  

## Licença

Este projeto é livre para uso e modificação.  
```
