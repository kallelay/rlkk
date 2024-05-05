copy /y ..\..\README.md README.md
copy /y ..\rLKK.py src\rLKK\__init__.py
python -m pip install --upgrade build
python -m build
upload_twine
pause