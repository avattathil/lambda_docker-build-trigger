# lambda_docker-build-trigger
Triggers Automated Builds in docker hub via AWS Lambda



Json input
```json
{
  "build_trigger": "https://registry.hub.docker.com/u/<docker-repo>/<docker-image>/trigger/token/",
  "branch": "develop"
}
```
