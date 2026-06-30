#!/bin/bash

echo "Starting K3s core components..."

kubectl scale deployment coredns -n kube-system --replicas=1
kubectl scale deployment local-path-provisioner -n kube-system --replicas=1
kubectl scale deployment metrics-server -n kube-system --replicas=1
kubectl scale deployment traefik -n kube-system --replicas=1

echo "Starting database..."

kubectl scale deployment postgres -n backend --replicas=1

sleep 10

echo "Starting applications..."

kubectl scale deployment backend-api -n backend --replicas=2
kubectl scale deployment frontend-app -n backend --replicas=2

echo "Lab started."
