## README.MD

#1.Remediation use cases - AWS Elastic Kubernetes Service (EKS):
  - AWS EKS security groups allow incoming traffic only on TCP port 443.

#2. Remediation Solution:
  - First part of this solution fetch the eks security group details and its configuration.
  - In testing, we are checking that all the security group should be configured with port number 443 Only.

#3. # TestCase details:
  - Test cases will get successfull only when all the security groups port is configured with port 443.

#4. Setup Infrastrucutre for testing:
  - create eks cluster on aws server, to create eks cluster it require SECURITY GROUP & ROLE, so you need to create both security group and roles and         assign them to eks cluster. 
  - create user key pair of secret key and access key, This credentials is required while executing the code.

#5. How to run script:
    
    Pre-Requisite
    1. Put Cloud credential in credentials file, please find the file on mentioned path ->
      /app/credentials (you can change it)
    2. Put credentials file path in dev.env
    3. insert you eks host name on ansible host file inside eks_host group. Find the syntax below.

    [eks_hosts]
    <>your EKS host api<>
    
    Install all required module from requirements.txt ==> pip install -r requirements.txt
    
    Execute below command to get security group details of all cluster present in your aws account.
      - python main.py
      - it fetch the security group details and store it in /test/data/ in json format, later we use this file to perform testing.
      
    Execute belwo command to start testing:
      - python run_test_cases
        - Test case get passed only if all the ports are configured with port 443, else it will get failed.
        
    if Test cases failed then we will run ansible script to update the security group configuration as required, Execute below command to run remediation     ansible script.
      
      ansible-playbook /remediation_scripts/aws_security_group_policy.yml 
      --extra-vars '{"aws_access_key":"access_key","aws_secret_key":"secret_key","region":"us-east-     1","name":"eks_cluster_name","vpc_id":"vpc_id","from_port":"fromPort","to_port":"toPort", "security_group_id":"security_group_id"}'



**Config Details:**
1. aws_security_group_policy.yml is security group configuration file, it can be used to check existing configuration and update the configuration if required through ansible


**Features:**
1. logger is implemented to maintain logs.
2. code files are distributed across directories depends on their uses to ease of read and understanding.




Path check configuration file path before executing. check you yml file location and correct if required.

**Find the project Structure**\
- __eks\_implementation__
   - __app__
     - __constant__
       - [\_\_init\_\_.py](app/constant/__init__.py)
       - [constant.py](app/constant/constant.py)
     - __credentials__
       - [aws\_role\_account.json](app/credentials/aws_role_account.json)
     - __discovery__
       - [\_\_init\_\_.py](app/discovery/__init__.py)
       - [aws\_discovery.py](app/discovery/aws_discovery.py)
       - [aws\_network.py](app/discovery/aws_network.py)
       - [connection.py](app/discovery/connection.py)
       - [eks_discovery.py](app/discovery/eks_discovery.py)
     - __utils__
       - [eks\_exceptions.py](app/utils/eks_exceptions.py)
       - [logger\_util.py](app/utils/logger_util.py)
       - [\_\_init\_\_.py](app/__init__.py)
   - __remediation\_scripts__
     - [aws\_security\_group\_policy.yml](remediation_scripts/aws_security_group_policy.yml)
   - __tests__
     - __data__
       - [test\_aws\_security\_group\_policy.json](tests/data/test_aws_security_group_policy.json)
     - [test\_aws\_policy\_resource.py](tests/test_aws_policy_resource.py)
     - [\_\_init\_\_.py](tests/__init__.py)
   - [main.py](main.py)
   - [run\_test\_cases.py](run_test_cases.py)
   - [config.py](config.py)
   - [dev.env](dev.env)
   - [requirements.txt](requirements.txt)
   - [readme.md](readme.md)

