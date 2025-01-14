# Development Steps

- Complete the `docker compose` environment building.
- Complete the `api_gateway` development and features including login, register, OAuth2 and rate time limit.
- Complete the `PA` implentation guide about scenario 1.

# Development server

- The worker server is deployed in the purevoltage (KVM-based VPS)
- The FMSA is deployed in the colocrossing (A dedicated server)

# References

1. FHIR server

- https://confluence.hl7.org/display/FHIR/Open+Source+Implementations
- https://confluence.hl7.org/display/FHIR/SMART+on+FHIR+server+implementations
- https://medium.com/impelsys/0f12c0cbbfdd

2. microservice scalability

- https://milaan.hashnode.dev/scaling-docker-containers-with-nginx-a-guide-to-reverse-proxy-and-load-balancing

3. Docker container hardware metrics

- https://gcore.com/learning/sysdig-what-it-is-and-how-to-use-it
- https://gcore.com/learning/troubleshooting-containers-with-sysdig-inspect

4. KeyCloak admin API

- https://medium.com/@imsanthiyag/44beb9011f7d
- https://www.stefaanlippens.net/keycloak-programmatically-create-clients-and-users.html
  - Tested versions are `21.0.2`, `22.0.5` and `23.0.7`.
- https://stackoverflow.com/questions/75776236/keycloak-session-and-token-timeouts

# Troubleshooting

1. FHIR server hostname setting (Tomcat issue)

- `The character [_] is never valid in a domain name`
- https://blog.csdn.net/janet1100/article/details/121639158
- https://silcoet.ntunhs.edu.tw/FHIRSampleCode/Manual/HAPI%20FHIR%20Server_Linux.pdf
