import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(GroupName='yorick_group_v2',
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
print('Ingress Successfully Set %s' % data)
