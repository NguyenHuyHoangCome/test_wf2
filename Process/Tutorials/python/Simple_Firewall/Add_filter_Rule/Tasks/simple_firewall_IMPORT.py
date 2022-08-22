import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order

# List all the parameters required by the task
dev_var = Variables()

dev_var.add('device_id')
# dev_var.add('drop')
context = Variables.task_call(dev_var)

# read the ID of the selected managed entity
device_id = context['device_id']

# extract the database ID
devicelongid = device_id[3:]

# build the Microservice JSON params
#{"Gateway":"0"}
#micro_service_vars_array = {"object_id":object_id}
object_parameters = {}

object_parameters['user'] = '0';


# call the CREATE for the specified MS for each device
order = Order(126)
order.command_execute('READ', object_parameters)

# convert dict object into json
content = json.loads(order.content)
hi = []

# for i in range(len(json.loads(content['message'])['user'])):
# 	h = {"id" : json.loads(content['message'])['user'][''+str(i+1)+'']['object_id']}

# 	hi.append(h)

# context['list'] = json.loads(content['message'])['user']
#########################################
# for i in json.loads(content['message'])['user']:
# 	h = {"user_id" : json.loads(content['message'])['user'][''+str(i)+'']['user_id'],
# 		 "password" : json.loads(content['message'])['user'][''+str(i)+'']['password'],
# 		 "object_id" : i
# 	}
# 	hi.append(h)
	
#context['list'] = 0
context['list'] = json.loads(content['message'])
#context['list'] = hi
# check if the response is OK

if order.response.ok:
    ret = MSA_API.process_content('ENDED',
                                  f'STATUS: {content["status"]}, \
                                    MESSAGE: successfull',
                                  context, True)
else:
    ret = MSA_API.process_content('FAILED',
                                  f'Import failed \
                                  - {order.content}',
                                  context, True)


print(ret)

