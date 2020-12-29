ARGS=$@

main() {
    if [[ $1 == init ]];
    then
        echo -e "\n\e[96m\e[1m>> Montando el BackEnd. \e[0m"
        echo ""
        cd microservices
        bash docker.sh up
        cd ..
        echo -e "\n\e[94m\e[1m>> Montado el FrontEnd. \e[0m"
        cd front/cloud
        echo ""
        ng serve --open
        echo ""
    elif [[ $1 == stop ]];
    then
        echo -e "\n\e[91m\e[1m>> Desmontando el BackEnd. \e[0m"
        echo ""
        cd microservices
        bash docker.sh down
        echo ""
        cd ..
    elif [[ $1 == back ]];
    then
        echo -e "\n\e[96m\e[1m>> Montando el BackEnd. \e[0m"
        echo ""
        cd microservices
        bash docker.sh up
        cd ..
    fi
}

main $ARGS