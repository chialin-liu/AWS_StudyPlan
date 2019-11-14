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
# EC2 LAB
    1. Launch instance->Free tier only
    2. Use private key to connect EC2
    3. Let anyone in 0.0.0.0/0
    4. let one ip in x.x.x.x/32
    5. security group are virtual walls
    6. SSH(22), HTTP(80), HTTPS(443), RDP(3389)
    7. Design for failure. Put EC2 in AZs
    
# EC2 Command Line
    1. use access key & access ID to connect
# Using Role
    1. connect role to EC2
    2. more safe to use than access key/id
    3. Universal
# LoadBalancer
    1. EC2->load balancer
    2. application lb(7-layer, make intelligent decision); 
    3. network lb(extreme performance, static ip address); 
    4. classic lb(test, develope, keep costs low)
# DB
## RDS Type
    1. SQL server
    2. Oracle
    3. MySQL Server
    4. PostgreSQL
    5. Aurora
    6. MariaDB
## Feature
    1. Multi-AZs for disaster recovery
    2. Read-replicas for performance
## Non-relational
    1. DynamoDB
## Difference between OLTP/OLAP
    1. OLTP: online transaction processing: order a number and return a row of data
## What is data warehousing
    1. Amazon is redshift
    2. redshift for business intelligence or data warehousing
## What is Elastic Cache
    1. a web service makes it easy to deploy operate and scale in-memory in the cloud
    2. speed up performance of existing databases (Frequenct identical queries)
    2. two open-source engines: memcached/redis
# DB-LAB
![image](https://github.com/chialin-liu/AWS_StudyPlan/blob/master/CloudPractitioner/ec2_script.png)

# Route53
    1. build a DNS or register domain name
    2. Global same as IAM/S3
# Elastic Beanstalk
    1. build automatically
    2. Is limited and not programmable
# CloudFormation
    1. Elastic Beanstalk and cloud formation are free services
    2. the resources they provision are not free(EC2)
    3. can provision and progrmmable
# Global AWS services
## Services are global  
    1. IAM
    2. Route53
    3. CloudFront
    4. SNS
    5. SES
## some services are global views but are regional
    1. S3
# Which AWS service can be used on-premise
    1. snowball
    2. snowball edge
    3. storage gateway
    4. codedeploy
    5. opswork
    6. iot greengrass
# Cloudwatch
## monitor things
    1. Compute: EC2/Autoscaling group/Elastic load balance/Route 53 health checks
    2. Storage/content delivery: EBS volumn/storage gateway/cloudfront
    3. Host Level metrics: CPU/network/disk/status check
## Remember
    1. cloudwatch with ec2 monitor events every 5 min
    2. can have 1 min intervals by turning on detailed monitor
    3. create cloudwatch alarm which trigger notifications
    4. cloudwatch is all about performance
#  AWS system manager
    1. manage fleets of EC2 and virtual machine
    2. a piece of software is installed in virtual machine
    3. can be inside AWS and on-premise
    4. run command to install/patch
    5. integrate with cloudwatch to your dashboard entire estate
    
# Ch3 price model
## Difference in CAPEX & Opex
    1. Capex: capital expenditure, pay upfront, fixed, sunk cost
    2. Opex: Operational expenditure, pay for what you use. Like utility billing
## Pricing policy
    1. pay as you go
    2. pay less where you reserve
    3. pay even less per unit by using more
    4. pay even less as AWS grows
    5. custom pricing
    $ understand the fundamentals of pricing; start early with cost opitmization; maximize the power of flexibilty
## three fundamental drivers of pricing
    1. comput 
    2. storage
    3. data outbound
## pricing models
    1. On-demand
    2. reservation
    3. dedicated instances
    4. spot instances
## Free services
    1. VPC: virtual data center in the cloud
    2. Elastic beanstalk
    3. cloudformation
    4. IAM
    5. auto scaling
    6. Opsworks
    7. consolidated billing
## what determines the price
    1. clock hours of server time
    2. instance type
    3. price model
    4. number of instances
    5. load balance
    6. detailed monitor
    7. auto scale
    8. elastic IP address
    9. operating system/software packages
## Price for Lambda
    1. Request pricing:
        free tier: 1M per month
    2. Duration pricing: xxx GB-sec per month
    3. additional charge: if Lambda uses other AWS services or transfer data, like s3
## Price for EBS
    1. Volumes(per GB)
    2. Snapshots(per GB)
    3. data transfer
## Price for S3
    1. storage class
    2. storage
    3. requests(GET/PUT/COPY)
    4. data transfer
## Price for glacier
    1. storage
    2. data retrieval times
## Snowball
    1. data transport solution to transfer large data in/out AWS
    2. Price for snowball: service fee per job; daily charge: first 10d are free; Data transfer: in to S3 free, but out is not
## Price for RDS
    1. clock hours of server time2
    2. database character
    3. db purchase type
    4. number of db instances
    5. provisioned storage
    6. additional storage
    7. requests
    8. deployment type
# AWS budget  and cost explorer
## budget
    1. set custom budget which alert you when exceed
    2. use budget cost before they have been incurred
## Cost explorer
    1. has easy-to-use interface that lets you visualize, understand, and manage
    2. use explore costs after they have been incurred
## support plans
![image](https://github.com/chialin-liu/AWS_StudyPlan/blob/master/CloudPractitioner/pricemodel.png)
