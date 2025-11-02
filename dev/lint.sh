if [[ "${1}" == "--fix" ]]; then
	ruff check --select I --fix
	ruff check --fix
	ruff format
else
	ruff check
	ruff check --select I
	ruff format --check
	mypy -p flask_backend
fi
