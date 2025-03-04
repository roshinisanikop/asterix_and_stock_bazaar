clientSize=5

for ((i=1; i<=clientSize; i++))
do
    echo "Starting client $i........"
    python3 Client.py & 
    python3 UpdateClient.py &
done

wait

echo "All clients have finished."