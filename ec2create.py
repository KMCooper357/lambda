import boto3


# Create an EC2 instance client
ec2 = boto3.client('ec2')

def create_instances():
    instances = ec2.run_instances(
        ImageId='ami-0953476d60561c955, ami-084568db4383264d4',  # Replace your AMI ID 
        InstanceType='t2.micro',  # instance type is the free tier
        MinCount=3,
        MaxCount=3,
        KeyName='lambdaproject2025',  # Input a key pair name
        SecurityGroupIds=['sg-001f91dc415319676'],  # Replace with your security group ID
        SubnetId='subnet-0f90bb8daa333f236'  # Replace it with your subnet ID
    )

    for instance in instances['Instances']:
        print(f"Created instance with ID: {instance['InstanceId']}")

if __name__ == '__main__':
    create_instances()