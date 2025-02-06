# Development Steps

- Complete the `docker compose` environment building.
- Complete the `api_gateway` development and features including login, register, OAuth2 and rate time limit.
- Complete the `PA` implentation guide about scenario 1.

# Development server

- The worker server is deployed in the purevoltage (KVM-based VPS)
- The FMSA is deployed in the colocrossing (A dedicated server)

# References

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

4. KeyCloak admin API

- https://medium.com/@imsanthiyag/44beb9011f7d
- https://www.stefaanlippens.net/keycloak-programmatically-create-clients-and-users.html
  - Tested versions are `21.0.2`, `22.0.5` and `23.0.7`.
- https://stackoverflow.com/questions/75776236/keycloak-session-and-token-timeouts

5. Upload file with FastAPI

- https://stackoverflow.com/questions/63048825/how-to-upload-file-using-fastapi

# Troubleshooting

1. FHIR server hostname setting (Tomcat issue)

- `The character [_] is never valid in a domain name`
- https://blog.csdn.net/janet1100/article/details/121639158
- https://silcoet.ntunhs.edu.tw/FHIRSampleCode/Manual/HAPI%20FHIR%20Server_Linux.pdf

2. FHIR server upload-terminology issues

- https://github.com/hapifhir/hapi-fhir/issues/3276
- https://github.com/hapifhir/hapi-fhir/issues/4715
