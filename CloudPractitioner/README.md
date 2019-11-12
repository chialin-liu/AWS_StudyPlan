# Ch2-1.  What is cloud computing
##  advantage of cloud computing
    1. Trade captital expense for variable expense
    2. Benefits from massive economics of scale
    3. Stop guessing about capacity
    4. Increase speed and agility
    5. Stop spending money running and maintaining data centers
    6. Go global in minutes
##  Three types of cloud computing
    1. IaaS: Like AWS-EC2. Manage your own server
    2. PaaS: Let someone manages hardware/OS, like AWS-Elastic Beanstalk
    3. SaaS: We use gmail, google will handle everything
##  Three types of cloud computing deployments
    1. Public cloud: GCP, Azure, AWS
    2. Hybrid cloud
    3. Private cloud: VMware, openstack
# Ch2-2. Around the world with AWS
##  Global Infrastructure
    1. Available zone: think of as Data center
    2. An availablity zone may have many data centers
    3. edge location: consists of CloudFront, a CDN, for storing data cache
![image](https://github.com/chialin-liu/AWS_StudyPlan/blob/master/CloudPractitioner/AZRegion.png)
    
##  Choosing the right region?
    1. Data sovereinty law
    2. Latency to end user
    3. AWS services: us-east1 has numerous services

# Ch2-3 Let's log into AWS - LAB     
##  Support package
    1. Basic
    2. Developer 12-24 hr response, 29$/month
    3. Business: 1 hr response, 100$/month
    4. Enterprise: 15min response, $15000/month
# Ch2-4 Create a billing alarm
## LAB step
    1. Launch cloudWatch-> billing->create alarm->select SNS topic-> create new topic->enter email address-> subscribe topic

# Ch2-5 Identity Access Management
## LAB security status
    1. MFA
    2. modify the IAM users sign in link to be more friendly
    3. Three ways of accessing: 
    * programmatic access: access ID, secret key
    * AWS management console
    * AWS SDK
    4. Add user to permission: 
    * Add user to specified group
    * copy permission from other users
    * apply policy to user
    5. Create a group-> AdminAccess(JSON-format)->email the user passwd/id 
## Global     

# Ch2-6 S3
## Introduction
    1. Object-based storage
    2. Files stored in bucket
    3. share universal name space: globally
    4. Receive HTTP 200 (successful)
    5. Key-value store(key is file name, value is bytes)
    6. Version-ID

## Data consistency in S3
    1. if updating existing file, may or may not see immediately
    2. Read after write consistency for PUTS
    3. Eventual consistency for OVERWRITE PUTS and DELETES(take time to propagate)
## Gurantee
    1. (11x9) durability(won't lose access to the file)
## Features
    1. Tiered storage available
    2. Lifecycle management
    3. versioning
    4. encryption
    5. secure data using: Access Control Lists and Bucket policies
## storage class
    1. Standard: 99.99 available; (11x9) durability; stores redundantly multiple devices and designed for sustaining the loss
    2. IA(infrequent access): lower fee than standard, charged retrieval fee
    3. One-zone IA: lower cost; and no requirement for many AZs data resilience
    4. Intelligent Tiering: design to optimize cost by moving data automatically for cost-effective without performance impact
    5. Glacier: store data at cheaper costs than on-premise solutions. Retrieval times can be configured to minutes to hours
    6. Glacier deep archive: lowest cost storage, retrieval times may be 12 hours
    
     
