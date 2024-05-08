#!/usr/bin/env bash
# Script run-example.sh reaches from app1 to app2.

docker compose build
docker compose up --wait
docker compose exec app1 bash -c 'curl -s http://app1/reach?app=app2'
docker compose down

