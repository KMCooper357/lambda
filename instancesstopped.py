import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    region = 'us-east-1'
    instance_ids = ['ami-0953476d60561c955', 'ami-084568db4383264d4']  # instance ID 
    
    response = ec2.describe_instance( 
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']

            }
        ]
    )

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if instance_ids:
        ec2.stop_instances(InstanceIds=Instance_ids)
        return {
            'statusCode': 200,
            'body': f'Stopped instances: {Instance_ids}'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No running instances found.'
        }