ARGS=$@

main() {
    if [[ $1 == ps ]];
    then
        echo "Informacion de los dockers"
        echo ""
        sudo docker ps -a
        echo ""
    elif [[ $1 == down ]];
    then
        sudo docker-compose down --volumes
    elif [[ $1 == up ]];
    then
        sudo docker-compose up -d
    elif [[ $1 == into ]];
    then
        sudo docker exec -it $2 bin/bash
    fi
}

main $ARGS