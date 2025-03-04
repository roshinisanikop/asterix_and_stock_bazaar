# Instructions on how to run Lab 1

This lab has been written and implemented by Isha Nilesh Gohel and Roshini Sanikop. Part-1 was implemnted my Roshini Sanikop. part-2 was implemented by Isha Nilesh Gohel. Part-3 was done by both together.
## Run Part 1
Start a docker container using this command. Let that docker container act as the server.
```
 ./cs677-run-docker
```
Run this command to start the server. Make sure you are in the part1 directory before running this command
```
 python3 server.py
```



Start another docker container using the below command in another terminal. Let that container act as the client.
```
 ./cs677-run-docker -f
```

Run the bash script to start multiple clients. Currently it is set to 5. Make sure you are in the part1 directory before running the script.
```
 ./run_multiple_clients.sh
```



## Run Part 2

Start a docker container using this command. Let that docker container act as the server.
```
 ./cs677-run-docker
```
Create a virtual environment using the below command
```
 python3 -m venv .venv
```
where `.venv` is name of your virtual environment. 

To activate the virtual environment, run 
```
 source .venv/bin/activate
```
Now, you should see a prefix `(.venv)` preceeding the terminal name. 

Run the requirement.txt file to install necessary libraries. You can use this command
```
 pip3 install -r requirement.txt
```

For creating the python files from the proto, use this command inside the docker container, after starting the virtual enviroment
```
 python3 -m grpc_tools.protoc -I/home/cs677-user/lab1/src/part2/ --python_out=/home/cs677-user/lab1/src/part2/ --grpc_python_out=/home/cs677-user/lab1/src/part2/ /home/cs677-user/lab1/src/part2/StockTrading.proto
```

Run this command to start the server. Make sure you are in the part2 directory before running this command
```
 python3 Server.py
```

Start another docker container using the below command in another terminal. Let that container act as the client.
```
 ./cs677-run-docker -f
```
Create a virtual environment using the below command
```
 python3 -m venv .venv
```
where `.venv` is name of your virtual environment. 

To activate the virtual environment, run 
```
 source .venv/bin/activate
```
Now, you should see a prefix `(.venv)` preceeding the terminal name. 

Run the requirement.txt file to install necessary libraries. You can use this command.
```
 pip3 install -r requirement.txt
```

Run the bash script to start multiple clients. Currently it is set to 5. Make sure you are in the part2 directory before running the script.
```
 ./runClients.sh
```

## Run Part 3
For the evaluating the latencies, run an extra command given below after running the bash script to get the overall average latency.

If you want to calculate part1 latencies make sure you run this command in that directory and same for part2 as well.
```
 python3 avg_latency.py
```

the values will be stored in `latency_results.txt`
