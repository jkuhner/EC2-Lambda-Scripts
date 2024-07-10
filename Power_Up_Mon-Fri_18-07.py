import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': 'tag:Power',
            'Values': ['Mon-Fri-18:00-07:00']
        },
#        {
#            'Name': 'instance-state-name', 
#            'Values': ['stopped']
#        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all instances
    RunningInstances = [instance.id for instance in instances]
    
    #print the instances for logging purposes
    #print RunningInstances 
    
    #make sure there are actually instances to Power on. 
    if len(RunningInstances) > 0:
        #Power on
        poweringOn = ec2.instances.filter(InstanceIds=RunningInstances).start()
        print (poweringOn)
    else:
        print ("Nothing to see here") 
