import boto3
region = 'us-east-1'
instances = ['ami-0953476d60561c955', 'ami-084568db4383264d4']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances!!!: ' + str(instances))
    