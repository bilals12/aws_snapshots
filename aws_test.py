import boto3
import aws_sso

session = aws_sso.session_sso()

my_ec2 = session.client('ec2', region_name = session.region_name)
reservations = my_ec2.describe_instances(Filters=[{"Name": "instance-state-name","Values": ["running"],}]).get("Reservations")
for reservation in reservations:
  for instance in reservation["Instances"]:
    instance_id = instance["InstanceId"]
    instance_type = instance["InstanceType"]
    state = instance["State"]["Name"]
    print(f'{reservation}')