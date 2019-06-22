# Google Cloud Platform
### PoC Implementation of notejam on Google cloud Platform (GCP)

Notejam has been implemented using Google Kubernetes Engine (GKE) and CloudSQL on GCP.

This folder contains necessary artifacts for performing deploys.

`deployments/`

This folder contains Google deployment manager deployment files for deploying the CloudSQL
instance and also creates the database and associated user.
In a future full implementation it should also contain deployments for deploying the Kubernetes
cluster on GKE as well as projects, networking etc.


`kubernetes/`

This folder contains Kubernetes yaml files for deploying required services to GKE.


`kubernetes/ns.yml`

This file creates the isolated namespace that hosts one instance of of the notejam stack.
Namespaces can be used to isolate environments such as staging and production.


`kubernetes/service-deployment.yml`

This file is the deployment of the actual service pods to GKE.
You can control base number of replicas of the service here as well as the CloudSQL instance address to use.


`kubernetes/service.yml`

This is the definition of the service object that Kubernetes uses to expose a service outside of the cluster.
You can define a port that the service should listen to, and what targetPort on the actual service pods to forward traffic to.


`kubernetes/db-bootstrap-job.yml`

This file defines a Kubernetes job (run to completion) that bootstraps the SQL database for notejam.


`ingress.yml`

Here is the definition of a Kubernetes ingress resource which on GCP will create a loadbalancer that serves an
external IP and routes incoming traffic to the service object described above.



`secrets/`

This folder contains secrets that are needed for the service, encrypted with a GCP Key Management System (KMS) key.
