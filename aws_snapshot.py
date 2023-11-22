import argparse
import boto3
import aws_sso

# setting up argparse for cli input
parser = argparse.ArgumentParser(description='create ec2 snapshots')
parser.add_argument('--region', help='aws region', default='us-east-1')
parser.add_argument('--state', help='filter instance state', default='running')
args = parser.parse_args()

# get aws session
session = aws_sso.session_sso()

# setup ec2 client with a specified region
my_ec2 = session.client('ec2', region_name=args.region)

# get instances based on state
reservations = my_ec2.describe_instances(Filters=[{"name": "instance-state-name", "values": [args.state]}]).get("reservations")
for reservation in reservations:
  for instance in reservation["Instances"]:
    instance_id = instance["InstanceId"]
    for var in instance["BlockDeviceMappings"]:
      vol_id = var["Ebs"]["VolumeId"]
    for tag in instance["Tags"]:
      if tag["Key"] == "Name":
        name = tag["Value"]
    print("-"*50)
    print(f"{name}: {instance_id}, {vol_id}")
    response = my_ec2.create_snapshot(Description=f'snapshot for {name}: {instance_id}.', VolumeId=vol_id, TagSpecifications=[{'ResourceType': 'snapshot','Tags':[{'Key': 'Name', 'Value': f'{name} snapshot'}]}])
    print(response)
    print("-"*50)
    













