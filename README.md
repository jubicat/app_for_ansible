# Project Setup and Execution Guide  

## How to Run the Project  

Follow these simple steps to set up and run the project:  

### 1. **Generate an SSH Key**  
Use the following command to generate an SSH key:  
```bash  
ssh-keygen  
```  

### 2. **Establish SSH Connection**  
Connect to the target machine by copying your SSH key:  
```bash  
ssh-copy-id root@192.168.211.129  
```  

### 3. **Run the Ansible Playbook**  
Start the Ansible playbook by running the command below. You will be prompted for the vault password:  
```bash  
ansible-playbook playbook.yaml --ask-vault-pass  
```  

### 4. About Application
Simple UI and back-end application works on 18.209.56.22:1010/data endpoint.
