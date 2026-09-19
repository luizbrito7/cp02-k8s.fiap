#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
export KUBECONFIG="$PWD/kubeconfig"

kind get clusters | grep -qx fiap-store || kind create cluster --config 00-kind-cluster.yaml
kind load docker-image store-api:1.0 --name fiap-store
kubectl create ns store-dev --dry-run=client -o yaml | kubectl apply -f -
