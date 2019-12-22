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
1. Route table
2. Network ACL
3. security group
## Features
1. default created subnet is private IP; needs to auto-assign public ip if this subnet wants to be public
2. internet gateway can only attach one VPC
3. any subnet without assigning specified route table would be assigned to main route table; therefore, keep main route table as private.
4. if route table wants to connect internet, it needs to connect the target to internet gateway
5. set subnet association for the public subnet
<b> 6. security group cannot span VPC </b>
