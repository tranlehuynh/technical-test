# Setting Up a Virtual Environment and Running Tests with Pytest

This guide will help you set up a Python virtual environment, install dependencies from `requirements.txt`, and run tests using `pytest`.

## 1. Create a Virtual Environment
A virtual environment isolates your dependencies to avoid conflicts with system-wide packages.

Run the following command to create a virtual environment:

```sh
python -m venv venv
```

## 2. Activate the Virtual Environment

### On Windows:
```sh
venv\Scripts\activate
```

### On macOS/Linux:
```sh
source venv/bin/activate
```

Once activated, you should see `(venv)` in your terminal prompt.

## 3. Install Dependencies
NOTES: Before install set env for USERNAME and PASSWORD
```sh
set USERNAME="your-username"
set PASSWORD="your-password"
```

After activating the virtual environment, install the required dependencies:

```sh
pip install -r requirements.txt
```

## 4. Run Pytest
To execute a specific tests using `pytest`, run:

```sh
pytest tests/{file_name.py}
```
Example: 

(Linux)
```sh
pytest tests/test_market_buy.py 
````
(Windows)
```sh
pytest tests\test_market_buy.py 
````

Run all files:

```sh
pytest
```

You can also generate a more detailed output with:

```sh
pytest -v
```

You can also use this command to see the output of the tests:

```sh
pytest -s
```
