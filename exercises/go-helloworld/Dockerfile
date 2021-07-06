FROM golang:alpine
LABEL mainatiner="Alexander Ramirez"
COPY . /go/src/app
WORKDIR /go/src/app
EXPOSE 6111
RUN go mod init
RUN go build -o helloworld
CMD ["./helloworld"]


# build an image using the Dockerfile from the current directory
#docker build -t go-helloworld .

# build an image using the Dockerfile from the `lesson1/python-app` directory
#docker build -t go-helloworld lesson1/python-app


#docker build -t lexsoul/go-helloworld:1.0.0-SNAPSHOT.01 .
#docker run -d -p 6111:6111 go-helloworld:1.0.0-SNAPSHOT.01
#docker-machine ip default
#http://192.168.99.100:6111/
#docker tag go-helloworld:1.0.0-SNAPSHOT.01 lexsoul/go-helloworld:1.0.0-SNAPSHOT.01
#docker push lexsoul/go-helloworld:1.0.0-SNAPSHOT.01 