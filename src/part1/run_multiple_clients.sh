#!/bin/bash

numClients=1  #number of clients to be run

for ((i=1; i<=numClients; i++)) #mutiple clients run 
do
    echo "starting client $i..."
    python client.py &  
done

# wait for all background processes to complete
wait

echo "all clients have finished."

