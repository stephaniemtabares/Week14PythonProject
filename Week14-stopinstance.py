import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Stop instances
response = ec2.stop_instances(
    InstanceIds=['i-01eefec13b5b70d55', 'i-0d5e315a658cc66e8', 'i-01c43bc604d251d43']
)

# Print response
print(response)
