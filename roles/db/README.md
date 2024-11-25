# README: PostgreSQL Setup with Ansible  

This Ansible playbook automates the setup of PostgreSQL on a target host. It performs the following tasks:  

1. Adds the PostgreSQL repository to the system's sources list.  
2. Installs PostgreSQL and its dependencies, including `python3-psycopg2`.  
3. Ensures the PostgreSQL service is enabled and running.  
4. Creates a database user `postgres` with a predefined password.  
5. Sets up a database named `myappdb` with specific locale settings.  
6. Creates a table named `example` within the `myappdb` database.  

To execute, run the playbook using Ansible on the target machine with the necessary permissions.  