import boto3

ec2 = boto3.resource('ec2')

# Create 3 instances
instances = ec2.create_instances(
        ImageId="ami-0103f211a154d64a6",
        MinCount=3,
        MaxCount=3,
        InstanceType="t2.micro",
    )

# Print instance IDs
for instance in instances:
    print(instance.id)
