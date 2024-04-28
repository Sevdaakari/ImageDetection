## Build application on local  

`apt-get update`   
  
`apt-get upgrade`  

`sudo apt install python3-pip -y`  

`sudo apt-get update && sudo apt-get install ffmpeg libsm6 libxext6  -y`  

`pip install --no-cache-dir -r requirements.txt`   

`!wget "https://pjreddie.com/media/files/yolov3.weights"` *Download yolov3.weights file*   

`mv 'yolov3.weights.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com@kaggle-161607.iam.gserviceaccount.com%2F20240428%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240428T162133Z&X-Goog-Expires=259200&X-Goog-SignedHead' /appUI/yolov3.weights`  *rename file name to the correct one and move to appUI folder*   

`python3 manage.py runserver`  

## Check module version 

Example:  PIL module   

```
#In command line

python
>>> import PIL               
>>> PIL.__version__ 
```

## Build application docker image  

`docker build -t imgdet .`   

`docker images ` - проверить появился ли докер образ с именем `imgdet`   

## Run the docker container of the application  

`docker run --name imgdet-c1 -p 80:8000 -d imgdet`   

- имя контейнера: `imgdet-c1`,   

- имя образа: `imgdet`  


### Rebuild the image

`sudo docker stop imgdet-c1`  *Останавливает контейнер*  

`sudo docker rm imgdet-c1` *Удаляет контейнер*  

`git pull`

`sudo docker build -t imgdet .` *Пересобирает образ*  

`sudo docker images` *List images* 

`sudo docker rmi <your_container_id>` *Remove old image to extend disk space*  

`sudo docker run --name imgdet-c1 -p 80:8000 -d imgdet` *Run new container*
