#!/usr/bin/python3

import json
import boto3
import sys


with open('/opt/aws_panel/parameters.json', 'r') as json_data:
     params = json.load(json_data)

ins_details = []
instance    = {}

access_id   = params.get('access_token').strip()
secret_key  = params.get('secret_token').strip()
#aws_region  = params.get('aws_region_name').strip()
# print (sys.argv[1])
aws_region  = sys.argv[1]


ec2client   = boto3.client('ec2',
                  aws_access_key_id=access_id,
                  aws_secret_access_key=secret_key,
                  region_name=aws_region,)

response    = ec2client.describe_instances()

for instance_data in response["Reservations"]:
    volumes                              =  []
    instance                             =  {}
    if instance_data.get('Instances')[0].get('State').get('Name') == 'terminated':
       instance['instance_id']           =  instance_data.get('Instances')[0].get('InstanceId')
       instance['instance_state']        = 'terminated'
       instance['region']                =  aws_region
       instance['instance_name']         =  ''
       instance['instance_private_ip']   = ''
       instance['instance_public_ip']    = ''
       instance['instance_vpc_id']       = ''
       instance['instance_volumes']      = ''
       instance['instance_type']         =  instance_data.get('Instances')[0].get('InstanceType')
       instance['instance_key_name']     =  instance_data.get('Instances')[0].get('KeyName')

    else:
       instance['instance_state']        = instance_data.get('Instances')[0].get('State').get('Name')
       instance['region']                =  aws_region
       instance['instance_id']           =  instance_data.get('Instances')[0].get('InstanceId')
       instance['instance_name']         =  instance_data.get('Instances')[0].get('Tags')[0].get('Value')
       instance['instance_private_ip']   =  instance_data.get('Instances')[0].get('PrivateIpAddress')

       if instance_data.get('Instances')[0].get('PublicIpAddress') == None:
          instance['instance_public_ip'] = ''
       else:
          instance['instance_public_ip'] = instance_data.get('Instances')[0].get('PublicIpAddress')

       instance['instance_vpc_id']       =  instance_data.get('Instances')[0].get('VpcId')
       instance['instance_type']         =  instance_data.get('Instances')[0].get('InstanceType')
       instance['instance_key_name']     =  instance_data.get('Instances')[0].get('KeyName')
       for volume in instance_data.get('Instances')[0].get('BlockDeviceMappings'):
           volumes.append(volume.get('DeviceName'))

       instance['instance_volumes']      =  volumes



    ins_details.append(instance)

print(ins_details)
