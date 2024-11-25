# Docker Setup and Deployment with Ansible  

This Ansible playbook automates the setup of Docker and deployment of a containerized application.  

### Key Tasks:  
1. **System Package Installation:** Installs essential tools, including Docker dependencies.  
2. **Docker Setup:** Adds Docker's GPG key and repository, installs Docker CE, and configures the Docker group.  
3. **Application Deployment:** Copies the application to the remote host, builds a Docker image, and starts a container named `app-devops`.  
4. **Container Configuration:** Configures the container with `host` network mode and ensures Docker services are restarted for changes to take effect.  
