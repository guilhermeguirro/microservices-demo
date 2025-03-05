# Microservices Demo

This project demonstrates a simple microservices architecture with two Python FastAPI services communicating with each other in a Kubernetes environment.

## Project Structure

```
.
├── service_a/              # Service A - Simple greeting service
│   ├── main.py            # FastAPI application
│   ├── Dockerfile         # Container definition
│   └── requirements.txt   # Python dependencies
├── service_b/              # Service B - Proxies requests to Service A
│   ├── main.py            # FastAPI application
│   ├── Dockerfile         # Container definition
│   └── requirements.txt   # Python dependencies
└── helm/                  # Helm chart for Kubernetes deployment
    ├── Chart.yaml         # Chart metadata
    ├── values.yaml        # Configuration values
    └── templates/         # Kubernetes manifests
```

## Prerequisites

- Docker
- Kubernetes (Minikube for local development)
- Helm
- Python 3.11+

## Building and Deploying

### 1. Start Minikube

```bash
minikube start
```

### 2. Build Docker Images

```bash
# Build Service A
docker build -t service-a:latest ./service_a

# Build Service B
docker build -t service-b:latest ./service_b

# Load images into Minikube
minikube image load service-a:latest
minikube image load service-b:latest
```

### 3. Deploy with Helm

```bash
# Create namespace
kubectl create namespace microservices

# Install/upgrade the Helm chart
helm upgrade --install microservices ./helm --namespace microservices
```

### 4. Verify Deployment

```bash
# Check pod status
kubectl get pods -n microservices

# Check services
kubectl get services -n microservices

# Port forward Service B
kubectl port-forward svc/service-b 8012:8012 -n microservices

# Test the services
curl http://localhost:8012/ping_service_a
```

Expected response:
```json
{
    "message": "Greetings from Service A! (via Service B)"
}
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

1. Builds and tests the Docker images
2. Runs security scans (Trivy for container vulnerabilities)
3. Validates Helm charts
4. Performs linting and code quality checks

### Handling Secrets

In a production environment, sensitive data should be managed using:

1. Kubernetes Secrets for application-level secrets
2. HashiCorp Vault or AWS Secrets Manager for external secrets
3. Sealed Secrets for GitOps workflows
4. Environment-specific values files for Helm

## Production Considerations

For a production environment, consider:

1. **High Availability**:
   - Multiple replicas for each service
   - Pod disruption budgets
   - Anti-affinity rules

2. **Security**:
   - Network policies
   - Service mesh (e.g., Istio)
   - Pod security policies
   - Regular security scans

3. **Monitoring**:
   - Prometheus for metrics
   - Grafana for visualization
   - Distributed tracing (e.g., Jaeger)

4. **Logging**:
   - ELK stack or similar
   - Structured logging
   - Log aggregation

5. **CI/CD Improvements**:
   - Automated testing
   - Canary deployments
   - Blue/green deployments
   - Automated rollbacks 