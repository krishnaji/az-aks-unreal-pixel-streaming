# Metrics Server

# from fastapi import FastAPI
import time
import redis
import math as m
from kubernetes import client, config


# app = FastAPI()
# Get total pods where label is app=signallingserver
# load local kubeconfig
# config.load_kube_config()
# load incluster kubeconfig
config.load_incluster_config()
name = "signallingserver"
namespace = "default"

def getPods():
    ret = client.CoreV1Api().list_namespaced_pod("default", label_selector="app=signallingserver")
    totalPods = len(ret.items)
    return totalPods

# redis connection
r = redis.Redis(host="redis", port=6379, db=0)
r.set_response_callback('GET', int)

podCountBuffer=1

def trackConnections(r):
        totalConnections = r.get('CONNECTIONS')
        return totalConnections


# @app.get("/metrics")
# async def metrics():
def metrics():
    totalConnectionsCnt= trackConnections(r)
    desiredReplicasCnt = m.ceil(podCountBuffer + (totalConnectionsCnt*0.50));
    curretPodsCnt = getPods()
    if totalConnectionsCnt > 0:
        if curretPodsCnt < desiredReplicasCnt:
            # Scale up signallingserver pods to totalPodsCnt
            client.AppsV1Api().patch_namespaced_deployment_scale(name=name, namespace=namespace, body= client.V1Scale(spec=client.V1ScaleSpec(replicas=desiredReplicasCnt)))
            print("Scaling up to {} pods".format(desiredReplicasCnt))
        else:
            print("No need to scale up")
    else:
        print("No need to scale up")
    
    if curretPodsCnt > desiredReplicasCnt and curretPodsCnt > podCountBuffer:
        newPodsCnt = curretPodsCnt-1
        # Scale down signallingserver pods to newPodsCnt
        client.AppsV1Api().patch_namespaced_deployment_scale(name=name, namespace=namespace, body= client.V1Scale(spec=client.V1ScaleSpec(replicas=newPodsCnt)))

        print("Scaling down to {} pods".format(newPodsCnt))
    else:
        print("No need to scale down")

    
    return {"totalConnections": totalConnectionsCnt, "totalPods": getPods()}
    

if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app, host="localhost", port=8000)
    while True:
        print("Check for scaling {}".format(metrics()))
        time.sleep(3)

        
