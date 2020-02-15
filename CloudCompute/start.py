import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-022017f418bd76450').reboot()
