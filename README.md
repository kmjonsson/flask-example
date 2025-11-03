# flask-example

Basic flask example

# Setup

```
pip install -e .[dev]
```

# Init Database

```
python -c 'import fastapi_backend; fastapi_backend.initialize_database()'
```

# Run
```
flask --app flask_backend run --host 0.0.0.0 --reload
```

# Generate docs

```
pdoc -o docs flask_backend
```