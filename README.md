# Json to Yaml converter

## Description
Http service that converts multiple json files to yaml string. 
Service is packed inside docker image which is build with gradle.
Written on Python3 with Flask framework.

## How to

### Run service
 - Build the docker image
`./gradlew Json2Yaml`
 - Run docker
`docker run -p 80:80 jsonapp`

### Send file
 - Send request to [http://localhost:80/convert] for converting multiple json files to yaml string
`curl -F 'myfiles[]=@text.json' -F 'myfiles[]=@text1.json' http://localhost:80/convert`