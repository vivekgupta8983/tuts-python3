## Boto3

Boto3 is the name of the Python SDK for AWS or simply boto3 is a python module or python library or python API to work with AWS Services.

Boto3 allows us to directly create update and delete AWS Services from Python Scripts.
Boto3 is built on the top of botocore modules.

The Core concepts of boto3 are:
    Session: It is an AWS Management Console and store configuration information(primarily credentials).it's allows us to create service clients and resources. boto3 creates a default session for us when needed.
    It's used to AWS create session for python boto3.

        aws_mgmt_con=boto3.session.Session(profile_name="root")

    there are 3 types of session:
        1. custom session: here we created a session for boto3. it used when we multiple aws profile
            aws_mgmt_con=boto3.session.Session(profile_name="root")

        2. default session: where boto3 will create session for us. it used when we have only one aws profile
            
    Resource and Client: we can create particular AWS service console like iam console, ec2.console,sns console,etc. to create those console we use either Resource or Client 
        Resource is higher-level object-oriented service access and it is available for some of AWS Services. In Resource output is in object.
        Client is a low-level service access. In client output is on terms of Dictionary.
    
    Meta
    Collections: It is useful to collect group of resource 
    Waiters: 
    Paginators



