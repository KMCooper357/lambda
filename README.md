This project is a powerful, automated solution designed to optimize your AWS cloud usage by shutting down EC2 instances after business hours — saving money and reinforcing security without lifting a finger.

Automated Intelligence –- A Lambda function scans and stops all running EC2 instances daily.
Cloud-Native Efficiency -– Built with AWS Lambda, EventBridge, and CloudFormation for seamless integration and deployment.
Security & Savings –- Avoid unnecessary costs and reduce exposure from idle resources.

Just deploy, schedule, and relax — your cloud is now on autopilot.
Let your infrastructure work smarter, so you can focus on what truly matters.



Deployment Instructions
Get up and running with AWS CloudFormation in just a few steps:

1. Clone the Repository
Start by pulling the project to your local machine:

bash
Copy
Edit
git clone https://github.com/KMCooper357/lambda.git  
cd LUIT-Python3

2. Launch the CloudFormation Stack
Deploy the Lambda function and its scheduled rule using the AWS CLI:

bash
Copy
Edit
aws cloudformation create-stack \
  --stack-name Lambda \
  --template-body file://lambda.yaml \
  --capabilities CAPABILITY_IAM

3. Confirm Successful Deployment
Head to your AWS Console to verify:

- CloudFormation → Check the stack status

- Lambda Console → Ensure the function is listed and active

- EventBridge (CloudWatch Events) → Confirm the scheduled trigger is set
