import boto3


# Create an EC2 instance client
ec2 = boto3.client('ec2')

def create_instances():
    instances = ec2.run_instances(
        ImageId='',  # Replace your AMI ID 
        InstanceType='t2.micro',  # instance type is the free tier
        MinCount=3,
        MaxCount=3,
        KeyName='',  # Input a key pair name
        SecurityGroupIds=[''],  # Replace with your security group ID
        SubnetId=''  # Replace it with your subnet ID
    )

    for instance in instances['Instances']:
        print(f"Created instance with ID: {instance['InstanceId']}")

if __name__ == '__main__':
    create_instances()