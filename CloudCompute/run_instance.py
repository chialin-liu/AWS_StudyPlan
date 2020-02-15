import boto3
import os, sys, stat
ec2 = boto3.resource('ec2')
# Generate key pair
outfile = open('aaakeypair_tmp.pem','w')
# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='aaakeypair_tmp')
# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
print(KeyPairOut)
# os.chmod("ec2-keypair-tmp.pem", stat.S_IRUSR)

## Create SG
response = ec2.create_security_group(GroupName='yorick_group_v3',
                                     Description='this is yorick group')
security_group_id = response['GroupId']
print('Security Group Created %s' % (security_group_id))
data = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 80,
         'ToPort': 80,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp',
         'FromPort': 22,
         'ToPort': 22,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ])
print('SG Successfully %s' % data)
#
# instances = ec2.run_instances(
#      image_id='ami-0a887e401f7654935',
#      intance_type='t2.micro',
#      key_name='ec2-keypair',
#      security_groups = 'yorick_group_v3'
#  )
#
