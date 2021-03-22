#/bin/bash

docker build . -t appins/learning-docker
echo "Built docker image appins/learning-docker"

echo -n "Run Docker? [Y/n]: "
read opt

if [[ $opt == "" ]] || [[ ${opt:0:1} == "Y" ]] || [[ ${opt:0:1} == "y" ]] 
then
	docker run --name learning-docker-test -p 8080:80 -d appins/learning-docker && \
		echo "Server running at localhost:8080"
fi
