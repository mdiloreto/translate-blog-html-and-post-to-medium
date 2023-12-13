![Image](https://madsblog.net/wp-content/uploads/2023/11/image-65.png)


Kubernetes has established itself as the tool of choice for deploying, scaling, and managing applications in the cloud. One of the main reasons for its robustness and flexibility is its volume management system, designed to address one of the biggest challenges in containerization: data persistence.

In this case, we will be making an introduction to Ephemeral and Persistent Volumes in GKE.
# 

Types of Volumes


In this case, we are going to be classifying them into 2 types: Ephemeral and Persistent.
# 

Ephemeral volumes:


This type of Volume is allocated at the pod level and depends on the lifecycle of the pods. They are used when data or information should not be kept over time (i.e. it should not be resistant).

With these types of volumes, when the pod's lifecycle ends, the data lifecycle ends as well. Volumes will not maintain data persistence.

Some examples:


emptyDir: When a storage pod is defined as this volume type, it is created when the pod is assigned to a node in the cluster. An empty directory is assigned (as the name implies). It is shared for all Containers within the pod. When the pod's lifecycle ends. It also terminates the emptyDir volume and its data is deleted. When a container crashes, the data is not deleted. Some possible uses:Scratch space. Save checkpoints in long calculations to recover from failures. Maintain files that a Content-Manager container fetches while a web server container provides the data.

   - When a storage pod is defined this volume type, it is created when the pod is assigned to a node in the cluster.
   - An empty directory is assigned (as the name implies).
   - It is shared for all Containers within the pod.
   - When the pod's lifecycle ends. It also terminates the emptyDir volume and its data is deleted.
   - When a container crashes, the data is not deleted.
   - Some possible uses:Scratch space. Save checkpoints in long calculations to recover from failures. Maintain files that a Content-Manager container fetches while a web server container provides the data.
      - Scratch space.
      - Save checkpoints in long calculations to recover from failures.
      - Maintain files that a Content-Manager container fetches while a web server container provides the data.




When a storage pod is defined this volume type, it is created when the pod is assigned to a node in the cluster.





An empty directory is assigned (as the name implies).





It is shared for all Containers within the pod.





When the pod's lifecycle ends. It also terminates the emptyDir volume and its data is deleted.





When a container crashes, the data is not deleted.





Some possible uses:Scratch space. Save checkpoints in long calculations to recover from failures. Maintain files that a Content-Manager container fetches while a web server container provides the data.

   - Scratch space.
   - Save checkpoints in long calculations to recover from failures.
   - Maintain files that a Content-Manager container fetches while a web server container provides the data.




Scratch space.





Save checkpoints in long calculations to recover from failures.





Maintain files that a Content-Manager container fetches while a web server container provides the data.




Ephemerals with particular purposes:


ConfigMaps: This is a way to inject configuration data into pods. It is referenced within the pod specifications.

   - It's a way to inject configuration data into pods.
   - It is referenced within the pod specifications.




Secrets: Used to pass sensitive information such as passwords to pods.

   - It is used to pass sensitive information such as passwords to pods.




It's a way to inject configuration data into pods.





It is referenced within the pod specifications.





It is used to pass sensitive information such as passwords to pods.



# 

Persistent Volumes:



They are independent.





They do not depend on the life cycle of the Pods.





They can be either PersistenVolumes or PersistentVolumesClaim.




The types we'll be looking at today:


PersistenVolume (PV): This is the persistent storage statement presented in the cluster. It is provisioned using Storage Classes. They have a life independent of pods. The type of Storage is defined by the StorageClasses.

   - This is the statement of the persistent storage presented in the cluster. It is provisioned using Storage Classes. They have a life independent of pods.
   - The type of Storage is defined by the StorageClasses.




PersistentVolumeClaim (PVC):This is the requester configured at the pod level to consume the PV. The request can specify specific resource levels, sizes, and access models.

   - This is the requester configured at the pod level to consume the PV.
   - The request can specify specific resource levels, sizes, and access models.




This is the statement of the persistent storage presented in the cluster. It is provisioned using Storage Classes. They have a life independent of pods.





The type of Storage is defined by the StorageClasses.





This is the requester configured at the pod level to consume the PV.





The request can specify specific resource levels, sizes, and access models.



# 

What is a StatefulSet?


It is a type of K8s declarative object that is used to manage applications with persistent state.

It manages the deployment and scaling of a set of Pods and provides guarantees on the order and uniqueness of each Pod.

The difference with deployments is that an identity is handled for each pod. They are created with the same specifications but are not interchangeable. Persistent identifiers are set and maintained during reschedules.

They are used for apps that require:


Unique Network Identifiers.





Storage Persistent and stable.





One-time deployment and scaling in an orderly manner.





Automatic rolling updates.



# 

Lab: Testing PersistentVolumes on GKE


Let's start with the lab!

First, we can confirm that we have a GKE Standard Cluster deployed in our GCP lab environment:
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-48-1024x359.png)

# 

Connect to the cluster


As we should always do in Cloud Shell or Gcloud, we will use the Environmental Variables to save the zone and the name of the GKE Cluster:

```
export my_zone=us-central1-a
export my_cluster=standard-cluster-1
```

Next, let's set up Kubectl autocomplete in cloud shell:

```
source <(kubectl completion bash)
```

Now, we're going to connect to our cluster using the following command:

```
gcloud container clusters get-credentials $my_cluster --zone $my_zone
```

Here's the output that should be generated:
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-49.png)

# 

Create PVC


Now we'll use the following yaml file to declare our PersistenVolumeClaim:

```
apiVersion: v1
kind: PersistentVolumeClaim
Metadata:
  name: hello-web-disk
Spec:
  accessModes:
    - ReadWriteOnce
  Resources:
    requests:
      storage: 30Gi
```

As we will see in the following image, PVC is created in K8s:
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-52.png)


We will be able to verify the correct deployment using the following command:

```
Kubectl get persistentvolumeclaim
```
# 

Create Pod


Now we will create a Pod to be able to mount the PV using the PVC. Pod Statement:

```
kind: Pod
apiVersion: v1
Metadata:
  Name: PVC-Demo-Pod
Spec:
  Containers:
    - name: frontend
      Image: Nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        Name: PVC-Demo-Volume
  Volumes:
    - Name: PVC-Demo-Volume
      persistentVolumeClaim:
        claimName: hello-web-disk
```

As we can see, PVC is declared in


specs.containers.frontend.mountPath: where we reference the mount path and the PVC.





specs.volumes: here we declare the volumeb by referencing the PVC created in the previous step.




To deploy it, we'll use the following command:

```
kubectl apply -f nginx-fronted.yaml
```
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-55-1024x58.png)


We can see the deployed pods
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-60.png)

# 

Persistence Test


We'll run a small persistence test.

First, we'll enter the bash of the created pod using the following command:

```
Kubectl exec -it pvc-demo-pod -- sh
```

Then we'll create an html file in our mountPath:

```
echo Test webpage in a persistent volume!>/var/www/html/index.html
chmod +x /var/www/html/index.html
```
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-56.png)


Now we'll delete the pod:

```
Kubectl delete pod pvc-demo-pod
```
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-58.png)


We verify the existence of PVC:

```
Kubectl get persistentvolumeclaim
```
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-59.png)


We re-created the pod:

To deploy it, we'll use the following command:

```
kubectl apply -f nginx-fronted.yaml
```

And we check for persistence by reading the file created in the previous step.

```
cat /var/www/html/index.html
```
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-61.png)

# 

Create StatefulSet


Now let's create a StatefulSet.

We'll use the following yaml:

```
kind: Service
apiVersion: v1
Metadata:
  name: statefulset-demo-service
Spec:
  Ports:
  - Protocol: TCP
    Port: 80
    targetPort: 9376
  type: LoadBalancer
---
apiVersion: apps/v1
kind: StatefulSet
Metadata:
  name: statefulset-demo
Spec:
  selector:
    matchLabels:
      app: MyApp
  serviceName: statefulset-demo-service
  Replicas: 3
  updateStrategy:
    type: RollingUpdate
  template:
    Metadata:
      Labels:
        app: MyApp
    Spec:
      Containers:
      - name: stateful-set-container
        Image: Nginx
        Ports:
        - containerPort: 80
          name: http
        volumeMounts:
        - name: hello-web-disk
          mountPath: "/var/www/html"
  volumeClaimTemplates:
  - Metadata:
      name: hello-web-disk
    Spec:
      accessModes: [ "ReadWriteOnce" ]
      Resources:
        requests:
          storage: 30Gi
```

The distinct feature of this yaml is that instead of declaring the volume at the pod level, we declare the volumeClaimTemplates, where we specify the data of our PVC directly within this same yaml.

This will result in new PVCs being created from the application of this file.

We deployed it using the "kubectl apply" command executed earlier, but changing the file:

```
Kubectl apply -f statefulset-demo.yaml
```
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-62.png)


We can see the pods created:
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-63.png)


And as we mentioned before, the PVCs created.
![Image](https://madsblog.net/wp-content/uploads/2023/11/image-64.png)


This, as in the previous point, will give us disk persistence, but a StatefulSet gives us other features of a larger abstraction layer.
