import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order



# List all the parameters required by the task
dev_var = Variables()

# dev_var.add('id')
# dev_var.add('icmp')
# dev_var.add('src_ip')
# dev_var.add('dst_port')
dev_var.add('list.0.object_id')
dev_var.add('list.0.password')
dev_var.add('list.0.user_id')
dev_var.add('list.0.chose')

context = Variables.task_call(dev_var)

# devices = context['device']

# context['list'] = devices


ret = MSA_API.process_content('ENDED', f'value get ', context, True)
print(ret)