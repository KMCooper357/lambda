import boto3 # type: ignore

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    region = 'us-east-1'
    instance_ids = ['']  # instance ID 
    
    response = ec2.describe_instances( 
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
        ec2.stop_instances(InstanceIds=instance_ids)
        return {
            'statusCode': 200,
            'body': f'Stopped instances: {instance_ids}'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No running instances found.'
        }