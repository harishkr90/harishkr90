#create a virtual env
python3 -m venv myfirstimage

# activate the venv, (test the code, install required dependency -> repeat until all requirements are satisfied)
pip freeze > requirements.txt

# build image from current directory
docker build -t my_first_app_image .

# run docker compose file and bring up myapp, mongodb, mongodb-ui
docker-compose -f myapp.yaml up
