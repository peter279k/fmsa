# Introduction

We proposed the FMSA (FHIR-based Microservice Architecture), a new open-source software architecture designed for medical informatics systems.
And we developed this architecture to address the current lack of standardized microservice solutions in healthcare information systems.

# Architecture

<img width="984" height="823" alt="圖片1" src="https://github.com/user-attachments/assets/6bdf20c1-6e7a-4a38-8e83-6f4280081b67" />


# Development Steps

- If using the HTTP to expose FMSA, copying the `docker-compose-http.yml` to the `docker-compose.yml` file.
- Complete the `docker compose` environment building.
- Complete the `api_gateway` development and features including login, register, OAuth2 and rate time limit.
- Complete the `PA` implementation guide about scenario 1.

# Docker Compose

- Running the `docker compose up --build` to run the FMSA.

# Docker Swarm Cluster Mode

- Firstly, running the `docker swarm --init --advertise-addr <MANAGER-IP>` command on the Manager node.
- Running the `docker swarm join --token <TOKEN> <MANAGER-IP>:2377` command on each Worker node.
- Running the `docker node ls` to check all nodes status in this cluster. The expected output is as follows:

```bash
ID                            HOSTNAME         STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
jsp7dfuhsxx6hx8l2m8jkp987 *   docker-manager   Ready     Active         Leader           29.4.0
u2zwqgyk0qnyz93ywwc5bcr9b     docker-worker1   Ready     Active                          29.4.0
5c920sxqo9smmuaburxsxgnur     docker-worker2   Ready     Active                          29.4.0
5f8tw70zz8f5a2y8c7y688coi     docker-worker3   Ready     Active                          29.4.0
```

# Docker Stack Deployment (Single Cluster)

- Before running the `docker stack deploy` command, it should ensure the local Docker image has been built.
- If they're not deployed, it should run the `docker compose build` command firstly.
- If presenting `Error response from daemon: This node is not a swarm manager.` message, it should run the `docker swarm init`.
- If the FMSA is running via the `docker compose up` command, it should use the `docker compose down`.
- Running `docker stack deploy -c docker-compose-stack-deploy.yml fmsa` command to deploy the Docker stack.

**The docker-compose-stack-deploy.yml is only for testing Docker Stack deployment**

# Docker Stack Deployment (Multiple Clusters)

- Running the `docker service create --name registry --publish published=5000,target=5000 registry:2` command to setup the Docker Registry.
- Running the `docker compose build` to build FMSA Docker image.
- Running the `docker compose push` to publish Docker images to the registry.
- Running the `` command to deploy FMSA to the Docker Swarm Clusters.

# Development server (for Conference)

- The worker server is deployed in the PureVoltage (KVM-based VPS)
  - CPU: 4 cores
  - RAM: 16GB
  - HDD: QEMU HARDDISK 200GB
- The FMSA is deployed in the ColoCrossing (A dedicated server)
  - CPU: Intel(R) Xeon(R) CPU E3-1271 v3
  - RAM: 16GB
  - HDD: Samsung SSD 850 EVO 1TB

# References

The proof of concept paper is as follows:

- C.-S. Li, S.-P. Ma, and T.-H. Lin, ["FMSA: A Universal Microservice Architecture Based on FHIR Medical Informatics Standard,"](https://ieeexplore.ieee.org/document/11326732) 2025 Second International Conference on Artificial Intelligence for Medicine, Health and Care (AIxMHC), pp. 42–49, Oct. 2025.

1. HAPI FHIR server installation and usage

- https://confluence.hl7.org/display/FHIR/Open+Source+Implementations
- https://confluence.hl7.org/display/FHIR/SMART+on+FHIR+server+implementations
- https://medium.com/impelsys/0f12c0cbbfdd

- https://medblocks.com/blog/terminologies-in-fhir#how-to-set-up-snomed-ct-on-hapi-fhir--8
- https://medblocks.com/blog/how-to-enable-fhir-profile-validation-with-hapi-fhir-jpa-server
- https://hapifhir.io/hapi-fhir/docs/v/7.6.0/tools/hapi_fhir_cli.html
  - https://hapifhir.io/hapi-fhir/docs/tools/hapi_fhir_cli.html

2. microservice scalability

- https://milaan.hashnode.dev/scaling-docker-containers-with-nginx-a-guide-to-reverse-proxy-and-load-balancing

3. Docker container hardware metrics

- https://gcore.com/learning/sysdig-what-it-is-and-how-to-use-it
- https://gcore.com/learning/troubleshooting-containers-with-sysdig-inspect
- https://www.cnblogs.com/apink/p/15767687.html
- https://onairotich.medium.com/understand-container-metrics-and-why-they-matter-9e88434ca62a

4. KeyCloak admin API

- https://medium.com/@imsanthiyag/44beb9011f7d
- https://www.stefaanlippens.net/keycloak-programmatically-create-clients-and-users.html
  - Tested versions are `21.0.2`, `22.0.5` and `23.0.7`.
- https://stackoverflow.com/questions/75776236/keycloak-session-and-token-timeouts

5. Upload file with FastAPI

- https://stackoverflow.com/questions/63048825/how-to-upload-file-using-fastapi

6. Docker stack deployment approach

- https://stackoverflow.com/questions/58666953
- https://docs.docker.com/engine/swarm/stack-deploy

# Troubleshooting

1. FHIR server hostname setting (Tomcat issue)

- `The character [_] is never valid in a domain name`
- https://blog.csdn.net/janet1100/article/details/121639158
- https://silcoet.ntunhs.edu.tw/FHIRSampleCode/Manual/HAPI%20FHIR%20Server_Linux.pdf

2. FHIR server upload-terminology issues

- https://github.com/hapifhir/hapi-fhir/issues/3276
- https://github.com/hapifhir/hapi-fhir/issues/4715
