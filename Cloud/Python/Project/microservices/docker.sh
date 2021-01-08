ARGS=$@

main() {
    if [[ $1 == ps ]];
    then
        echo -e "\n\e[36m\e[1m>> Informacion de los dockers. \e[0m"
        echo ""
        sudo docker ps -a
        echo ""
    elif [[ $1 == down ]];
    then
        echo -e "\n\e[91m\e[1m>> Desmontando dockers. \e[0m"
        sudo docker-compose down --volumes
        echo -e "\n\e[91m\e[1m>> Eliminando la imagen cloud_api. \e[0m"
        sudo docker image rm cloud_api
        sudo docker image rm microservices_front:latest
        echo ""
    elif [[ $1 == up ]];
    then
        echo -e "\n\e[92m\e[1m>> Montando docker MySQLServiceDB y CloudApi. \e[0m"
        sudo docker-compose up -d
        echo -e "\n\e[32m\e[1m>> Proceso exitoso. \e[0m\n"
        echo -e "\n\e[36m\e[1m>> Informacion de los dockers. \e[0m"
        echo ""
        sudo docker ps -a
        echo ""
    elif [[ $1 == into ]];
    then
        sudo docker exec -it $2 /bin/bash
    fi
}

main $ARGS