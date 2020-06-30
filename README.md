# Face Recognition App
- Web app to for identifying faces
- uses the [face-recognition](https://github.com/ageitgey/face_recognition#face-recognition) library



## Run with Docker
- Make sure [Docker](https://docs.docker.com/install/ "Docker") & [Docker-Compose](https://docs.docker.com/compose/install/ "Docker-Compose") are installed
- run
```bash
$ docker-compose up -d
```
- exec into the app container and make DB migrations
```bash
$ docker exec -it CONTAINER_ID bash
```
- create an admin using **phpmyadmin**, use credentials from **docker-compose.yml** file
```bash
localhost:8090
```
- head over to 
```bash
localhost:5000
localhost:5000/admin
```
- see app logs
```bash
$ docker logs -f CONTAINER_ID
```
- clean up
```bash
$ docker-compose down -v
```
