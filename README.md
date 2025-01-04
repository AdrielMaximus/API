```markdown
# CRUD API with Flask

This project is a simple API built with Flask to manage fictional meals. It implements CRUD operations (Create, Read, Update, Delete), allowing you to list, view, update, and delete meals from a simulated dataset.

## Requirements

Before running the project, ensure you have installed:
- **Python 3.x**  
- **Flask**: Install it with the following command:
  ```bash
  pip install flask
  ```

## API Endpoints

### 1. Retrieve All Meals
- **Endpoint:** `GET /meals`  
- **Description:** Returns a list of all registered meals.  
- **Example Response:**
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

### 2. Retrieve a Single Meal
- **Endpoint:** `GET /meals/<id>`  
- **Description:** Returns a specific meal based on its `id`.  
- **Example Response:**
  ```json
  {
    "id": 1,
    "name": "whopper with fries and a shake",
    "franchise": "Burger King"
  }
  ```

### 3. Update a Meal
- **Endpoint:** `PUT /meals/<id>`  
- **Description:** Updates the data of a specific meal based on its `id`.  
- **Example Payload:**
  ```json
  {
    "name": "Updated Meal",
    "franchise": "Updated Franchise"
  }
  ```
- **Example Response:**
  ```json
  {
    "id": 1,
    "name": "Updated Meal",
    "franchise": "Updated Franchise"
  }
  ```

### 4. Delete a Meal
- **Endpoint:** `DELETE /meals/<id>`  
- **Description:** Removes a specific meal from the list based on its `id`.  
- **Example Response:** Returns the updated list of meals:
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

## How to Run

1. Save the code in a file named `app.py`.  
2. Open the terminal and navigate to the directory where the file is saved.  
3. Run the command:  
   ```bash
   python app.py
   ```
4. The API will be available at `http://localhost:5000`.

## Testing the API

You can test the endpoints using tools such as:  
- **Postman**  
- **cURL** in the terminal  
- Browser extensions like **Rest Client**  
- Scripts in programming languages like Python or JavaScript.  

## Code Structure

- **`meals`**: A simulated list acting as a database for meals.  
- **CRUD Endpoints:**  
  - `GET /meals`: Retrieves all meals.  
  - `GET /meals/<id>`: Retrieves a specific meal.  
  - `PUT /meals/<id>`: Updates a specific meal.  
  - `DELETE /meals/<id>`: Deletes a specific meal.  

## Additional Configuration

- **Port:** The API runs on port `5000` by default, but this can be changed directly in the code at the line `app.run(port=5000)`.  
- **Debug Mode:** The `debug=True` mode is enabled, allowing the server to reload automatically when the code is modified.  

## Challenges

While developing this project, I faced the following challenges:  
1. **Understanding Flask:** As a beginner, understanding how Flask handles routes and HTTP methods was challenging. I had to experiment and read documentation to properly configure the endpoints.  
2. **Managing JSON Data:** Manipulating JSON data, especially when updating or deleting specific items, required careful indexing and iteration through the list.  
3. **Debugging:** Some issues, such as incorrect data handling or forgetting to specify `Content-Type` in requests, caused errors that took time to resolve.  
4. **Learning API Basics:** This was my first experience building an API, and I had to learn concepts like HTTP status codes, request methods (GET, PUT, DELETE), and how to handle client-server communication.  
5. **Error Handling:** Adding error handling (e.g., handling invalid IDs) was something I initially overlooked, making the API prone to crashes with invalid input.  

## License

This project is free to use and modify.  
