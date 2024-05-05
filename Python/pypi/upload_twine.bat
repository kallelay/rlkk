python  -m twine upload --repository pypi dist/*
python  -m pip install --index-url https://www.pypi.org/simple/ --no-deps rlkk
pause