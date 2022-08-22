
import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order
from msa_sdk.orchestration import Orchestration



# List all the parameters required by the task
dev_var = Variables()


dev_var.add('device_id', var_type='Device')

context = Variables.task_call(dev_var)

# read the ID of the selected managed entity
device_id = context['device_id']

# extract the database ID
devicelongid = device_id[3:]

order = Orchestration(devicelongid)
order.read_service_instance(6)

# convert dict object into json
content = json.loads(order.content)

context['hoang'] = content


ret = MSA_API.process_content('ENDED', f'value get ', context, True)
print(ret)