# 🚀 DevSecOps Notes API Pipeline

A secure CI/CD pipeline for a Flask Notes API demonstrating modern **DevSecOps practices** by integrating automated testing, security scanning, containerization, and Kubernetes security validation.

The project follows a **Shift Left Security** approach by detecting vulnerabilities before deployment.

---

# 🏗️ Architecture

```
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI/CD
    |
    +--> Unit Testing
    |
    +--> SAST Scanning
    |
    +--> Secret Detection
    |
    +--> Dependency Security
    |
    +--> Container Security
    |
    +--> Kubernetes Security
    |
    v
Docker Image
    |
    v
Kubernetes Deployment
```

---

# 🛠️ Tech Stack

### Application
- Python Flask API
- PostgreSQL Database
- SQLAlchemy

### DevOps
- Git & GitHub
- GitHub Actions
- Docker
- Docker Compose
- Kubernetes

### Security Tools
- Bandit
- Semgrep
- CodeQL
- Gitleaks
- Trivy

---

# 🔄 CI/CD Pipeline

Every push triggers an automated security pipeline:

## 1. Testing

✅ Unit Tests

Validates application functionality before deployment.

---

# 🔐 Security Scanning

## SAST (Static Application Security Testing)

Tools:

- **Bandit**
- **Semgrep**
- **CodeQL**

Detects:

- insecure Python patterns
- code vulnerabilities
- security weaknesses

---

## Secret Scanning

Tool:

- **Gitleaks**

Protects against accidentally committing:

- API keys
- passwords
- tokens
- private credentials

---

## Dependency Security

Checks application dependencies for known vulnerabilities and outdated packages.

---

## Filesystem Security Scan

Tool:

- **Trivy Filesystem Scan**

Scans:

- source code
- configuration files
- dependencies

for known vulnerabilities.

---

# 🐳 Container Security

## Docker Image Build

The application is containerized using Docker.

Pipeline:

```
Dockerfile
    |
    v
Docker Image
    |
    v
Security Scan
```

---

## Container Vulnerability Scan

Tool:

- **Trivy Container Scan**

Scans Docker images for:

- OS vulnerabilities
- package CVEs
- insecure components

---

# ☸️ Kubernetes Security

The application is deployed using Kubernetes with security best practices.

Implemented:

✅ Kubernetes Manifest Validation  
✅ Kubernetes Configuration Scan  

Security hardening:

- Run containers as non-root
- Disable privilege escalation
- Drop unnecessary Linux capabilities
- Apply security contexts

Example:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
```

---

# 📂 Project Structure

```
notes-api/

├── app.py
├── models.py
├── database.py
├── requirements.txt

├── Dockerfile
├── docker-compose.yml

├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── postgres.yaml

├── tests/

├── .github/
│   └── workflows/
│       └── pipeline.yml

└── .gitignore
```

---

# 📊 Security Coverage

| Category | Tool | Status |
|---|---|---|
| Unit Testing | PyTest | ✅ |
| SAST | Bandit | ✅ |
| SAST | Semgrep | ✅ |
| Code Analysis | CodeQL | ✅ |
| Secret Detection | Gitleaks | ✅ |
| Dependency Scan | GitHub Security | ✅ |
| Filesystem Scan | Trivy | ✅ |
| Container Scan | Trivy | ✅ |
| Kubernetes Validation | Kubernetes Tools | ✅ |
| Kubernetes Security Scan | Kubescape/Tools | ✅ |

---

# 🎯 Skills Demonstrated

This project demonstrates practical experience with:

- Secure CI/CD pipelines
- DevSecOps automation
- Application security testing
- Container security
- Kubernetes security
- Vulnerability management
- Infrastructure security concepts

---


# 👨‍💻 Author

**Abdallah Hegazy**

DevOps / DevSecOps Engineer Portfolio Project