# SuperBenchmark

SuperBenchmark is a **FastAPI application** for managing and querying benchmarking results of a Large Language Model (LLM). 
The application provides endpoints to calculate average performance statistics and supports both full dataset queries and time-based filtering.

## Features

- **Store and manage benchmarking results**:
  - Includes details such as token counts, generation times, and timestamps for benchmarking requests.
- **Query average statistics**:
  - Calculate averages across all results or within a specified time range.
- **JSON-based testing mode**:
  - Supports a `DEBUG` mode to fetch results from a JSON file for easy testing.

## API Endpoints

### 1. **GET `/results/average`**
Returns the average performance statistics across all benchmarking results.

### 2. **GET `/results/average/{start_time}/{end_time}`**
Returns the average performance statistics for results recorded within a specific time range.

#### URL Parameters:
- **`start_time`**: Start of the time range in ISO 8601 format (e.g., `2024-06-01T12:00:00`).
- **`end_time`**: End of the time range in ISO 8601 format (e.g., `2024-06-01T14:00:00`).

#### Example Request:
```plaintext
GET /results/average/2024-06-01T12:00:00/2024-06-01T14:00:00
```

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/IraMladanovych02/SuperBenchmark.git
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   alembic upgrade head
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. Visit the application in your browser:
   ```plaintext
   http://127.0.0.1:8000
   ```

---

## Environment Variables
You can define the DEBUG variable in your main FastAPI application file (e.g., main.py)

- **`SUPERBENCHMARK_DEBUG`**: Enables DEBUG mode (default: `True`).
  - If `True`, the application fetches data from the `superbenchmark_db_data.json` file.
  - If `False`, the application works with the SQLite database.

To change the environment variable:
```bash
export SUPERBENCHMARK_DEBUG=False  # On Linux/Mac
set SUPERBENCHMARK_DEBUG=False     # On Windows
```

---

## Example JSON Data (for DEBUG mode)

The file `superbenchmark_db_data.json` contains example benchmarking results

---

## Testing the Endpoints

Use tools like **Postman** or **curl** to test the endpoints.

### Example Request with `curl`:
1. Test `/results/average`:
   ```bash
   curl -X GET http://127.0.0.1:8000/results/average
   ```

2. Test `/results/average/{start_time}/{end_time}`:
   ```bash
   curl -X GET "http://127.0.0.1:8000/results/average/2024-06-01T12:00:00/2024-06-01T14:00:00"
   ```

---



