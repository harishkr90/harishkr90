#create a virtual env
python3 -m venv myfirstimage

# activate the venv, (test the code, install required dependency -> repeat until all requirements are satisfied)
pip freeze > requirements.txt

# build image from current directory
docker build -t my_first_app_image .

# run docker compose file and bring up myapp, mongodb, mongodb-ui
docker-compose up -d # (-f filename.yaml) to be added before 'up' if file is not named as docker-compose.yml in the '.' dir

