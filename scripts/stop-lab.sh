#!/bin/bash

echo "Stopping applications..."

kubectl scale deployment backend-api -n backend --replicas=0
kubectl scale deployment frontend-app -n backend --replicas=0
kubectl scale deployment postgres -n backend --replicas=0

echo "Stopping K3s addons..."

kubectl scale deployment coredns -n kube-system --replicas=0
kubectl scale deployment local-path-provisioner -n kube-system --replicas=0
kubectl scale deployment metrics-server -n kube-system --replicas=0
kubectl scale deployment traefik -n kube-system --replicas=0

echo "Lab stopped."
