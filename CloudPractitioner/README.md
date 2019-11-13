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
    1. Object-based storage(Not suitable to install operating system)
    2. Files stored in bucket
    3. share universal name space: globally
    4. Receive HTTP 200 (successful)
    5. Key-value store(key is file name, value is bytes)
    6. Version-ID
    7. files can be 0Byte - 5TBytes
    8. unlimited storage
    7. s3-eu-west-1.amazonaws.com/acloudguru

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
![image](https://github.com/chialin-liu/AWS_StudyPlan/blob/master/CloudPractitioner/s3_class.png)    

## Charge
    1. storage
    2. requests
    3. storage management pricing
    4. data transfer
    5. transfer acceleration(Utilize cloudfront and edge location)
    6. cross region replication
    
# Ch2-7 S3 LAB
    1. Actions->make public (because by default, the uploaded file can be blocked)
    2. Cannot share bucket name with someone else
    3. View the bucket in globally, can have bucket in indivisual region
    4. can change storage class and encryption on the fly
## Restricting Bucket Access    
    1. bucket policy: apply to whole bucket
    2. object policy: apply to indivisual files
    3. IAM policies to user/group
# Ch2-8 S3 LAB website
    1. choose bucket -> Edit public access setting-> cancel block all public access->confirm
    2. properties->static website hosting
    3. use bucket polices to make bucket entire public
    4. website using DB cannot use s3
# Ch2-9 CloudFront
## Key terminolgy
    1. Origin: all the files that CDN will distribute. S3 bucket, EC2, Elastic load balancer or Route53
    2. Distribution: give the CDN2 which consists of collections of edge location
    3. Web distribution
    4. RTMP: for media streaming
    5. deploying...[06:54]
    6. Edge location can be written 
    7. Objects are cached for the TTL(Time to Live)
    8. Can clear objects but will be charged
![image](https://github.com/chialin-liu/AWS_StudyPlan/blob/master/CloudPractitioner/cloudfront.png) 

# Ch2-10 EC2
## What is EC2
    1. virtual server in cloud
## Pricing models
    1. On-demand: fixed rate by the hour or second
    2. Reserved: discount on the hourly charge. Contract term are 1y or 3y
    3. Spot: bit what price 
    4. Dedicated host: use your own server-bound software licences
## On-demand
    1. flexible and low cost, no upfront cost and no long-term contract
    2. app which is short-term, spiky or unpredictable workloads cannot be interrupted
    3. app built or tested on EC2 for the first time
## Reserved
    1. app with steady and predictable usage
    2. app requires reserved capacity
    3. able to make upfront payments to reduce more
    4. standard/convertible/schedualed types
## Spot
    1. app has flexible start/end time
    2. users with urgent computing needs for large amounts of additional capacity
    3. if spot is terminated by EC2, no charge.
    4. if you terminated your self, you will be charged
## Dedicate host
    1. for regulatory requirements that may not support multi-tenant virtualization
    2. great for licensing which does not support multi-tenant or cloud deployment
    3. can be purchased on Demand
    4. can be purchased as Reservation for up to 70% off on Demand
## What is EBS?
    * virtual disk in the cloud
    1. create storage volumes and attach them to EC2
    2. once attached, create a file system, run database
    3. placed in AZs, automatically replicated to protect from failure
    4. General Purpose SSD(GP2): balance price/performance for wide range
    5. Provision IOPS SSD(IO1): highest performance SSD
    6. Throughput optimized HDD(ST1): low cost for throughput-intensive or frequent access
    7. Cold HDD(SC1) : less frequent access workloads(File server)
    8. Magnetic
## EC2 LAB
    1. Launch instance->Free tier only
    2. Use private key to connect EC2
    3. Let anyone in 0.0.0.0/0
    4. let one ip in x.x.x.x/32
    5. security group are virtual walls
    6. SSH(22), HTTP(80), HTTPS(443), RDP(3389)
    7. Design for failure. Put EC2 in AZs
    
    
