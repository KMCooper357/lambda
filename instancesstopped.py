import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    region = 'us-east-1'
    instance_ids = ['ami-0953476d60561c955', 'ami-084568db4383264d4']  # instance ID 
    
    ec2.stop_instances(InstanceIds=instance_ids)
    print(f'Stopping the instances!!!!!: {instance_ids}')
    
    return {
        'statusCode': 200,
        'body': f'Successfully stopped instances: {instance_ids}'
    }