# docker-compose

> Illustrate reaching from app1 to app2.

## Getting started

Run the `run-example.sh` script. Your output should look like the following:

```
% ./run-example.sh
# ...
 ✔ Network docker-compose_default   Cr...                                  0.0s
 ✔ Container docker-compose-app2-1  H...                                   0.0s
 ✔ Container docker-compose-app1-1  H...                                   0.0s
{"app":"app1","reached":"app2"}
[+] Running 3/2
 ✔ Container docker-compose-app2-1  R...                                   0.1s
 ✔ Container docker-compose-app1-1  R...                                   0.1s
 ✔ Network docker-compose_default   Re...                                  0.0s
```
