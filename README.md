# Text_Analysis_Project 
## Software and Requirement

1. [Github Account](https://github.com)
2. [heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)

Creating environment 

'''
conda create -p venv python ==3.7 -y
'''

Activating environment


'''
conda activate venv/
'''

'''
pip install -r requirements.txt
'''

1. HEROKU_EMAIL = ansarimohammadm17@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regressor17

 BUILD DOCKER IMAGE
 '''
 docker build -t <image_name>:<tagname> .
 '''
> Note: Image name for docker must be of lowercase

To list docker image
'''
docker images
'''

Run Docker image
'''
docker run -p 5000:5000 -e PORT=5000 74cb20b5901b
'''
here 74cb20b5901b is image id you can get it from running docker images command
TO check running container in docekr
'''
docker ps
'''
to stop running container in docker 
'''
docker stop <container_id>
'''

Install ipykernel
"""
pip install -U ipykernel
"""