# VPC
## VPC peering
1. use private network to connect other VPCs
2. Can peer other VPCs in other accounts
3. Can't to transistive peering
4. Can peer with multiple regions
## Feature
1. a subnet in an AZ; subnet cannot span multiple AZs
2. security group is statefull, only set allow rules
3. NACL is stateless, needs to set inbound/outbound rule
## Default VPC contains
1. Route tableed
2. Network ACL
3. security group
## Features
1. default created subnet is private IP; needs to auto-assign public ip if this subnet wants to be public
2. internet gateway can only attach one VPC
3. any subnet without assigning specified route table would be assigned to main route table; therefore, keep main route table as private.
4. if route table wants to connect internet, it needs to connect the target to internet gateway
5. set subnet association for the public subnet
6. <b>security group cannot span VPC </b>
## 65. NAT
1. NAT gateway is high available and redundancy
2. <b>NAT instance disable source/destination check</b>
3. by modifying the route-table for adding destination 0.0.0/0 through NAT instance, then the private subnet instance can reach internet through this route-table and NAT instance
4. the fallback of NAT instance would be single point failure
5. NAT instance should behind the security group
6. NAT gateway inside the AZ
7. <b>NAT gatway starts 5Gbs and scales to 45Gbs</b>; not associate securty group, no need to patch; auto assign public IP
8. create a NAT gateway in each AZ
## 69. Bastions
1. because NAT gateway doesn't need to be in the security group, and NAT instance needs
2. SSH or RDP forwards the network to route-table->NACL->Bastion->private subnet instance
3. Cannot use NAT gateway as Bastion host
## 70. Direct Connect
1. provide the private connectivity between AWS and datacenter
2. reduce network costs and increase bandwidth
3. useful for high throughput workloads and needs reliable and secure connection
## 71. VPC endpoints
1. there are two endpoints, interface endpoints, gateway endpoints
2. <b>interface endpoints</b> is elastic network interface(ENI) with private IP. Basically, just attach ENI to EC2, that will allow the EC2 to communicate with services using internal network
3. <b>gateway endpoints</b> supports S3/DynamoDB. First, generate a IAM role for EC2 to use S3. Second, apply this S3AdminAccess Role into private subnet instance, such as database server EC2. Third, remove the route to internet gateway in route-table, just try to simulate whether the public subnet instance EC2 can or cannot connect private subnet EC2 to use S3. Four, by creating the s3 gatway endpoint, and apply this to main route-table. Then, we will see the route path to S3 in the main route-table. Remember to specify the region where S3 is. 

