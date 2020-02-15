import boto3
import os, sys, stat
ec2 = boto3.client('ec2')
# Generate key pair
# key_delete = ec2.delete_key_pair(KeyName='aaakeypair_tmp')
# outfile = open('aaabbbcckeypair_tmp.pem','w')
# key_pair = ec2.create_key_pair(KeyName='aaabbbcckeypair_tmp')
# KeyPairOut = str(key_pair.key_material)
# outfile.write(KeyPairOut)
# print(KeyPairOut)
# os.chmod("aaabbbcckeypair_tmp.pem", stat.S_IRUSR)

## Create SG
# response = ec2.create_security_group(GroupName='yorick_group_v8',
#                                      Description='this is yorick group')
# print (response)
# security_group_id = response['Id']
# print('Security Group Created %s' % (security_group_id))
# data = ec2.authorize_security_group_ingress(
#     GroupId=security_group_id,
#     IpPermissions=[
#         {'IpProtocol': 'tcp',
#          'FromPort': 80,
#          'ToPort': 80,
#          'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
#         {'IpProtocol': 'tcp',
#          'FromPort': 22,
#          'ToPort': 22,
#          'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
#     ])
# print('SG Successfully %s' % data)
#
instances = ec2.run_instances(
     ImageId='ami-0a887e401f7654935',
     InstanceType='t2.micro',
     MinCount=1,
     MaxCount=1,
     KeyName='ec2-keypair',
     SecurityGroups=['yorick_group_v3'
     ]
     # SecurityGroupIds='sg-0087d34d0316f2bf4',

 )
#
