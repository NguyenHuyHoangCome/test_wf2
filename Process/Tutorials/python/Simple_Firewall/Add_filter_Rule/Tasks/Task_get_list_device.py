# import json
# from msa_sdk.variables import Variables
# from msa_sdk.msa_api import MSA_API
# from msa_sdk.order import Order
# from msa_sdk import util


# # List all the parameters required by the task
# dev_var = Variables()
# # dev_var.add('id')
# # dev_var.add('icmp')
# # dev_var.add('src_ip')
# # dev_var.add('dst_port')
# # dev_var.add('list.0.id')
# context = Variables.task_call(dev_var)

# devices = context['device']




# ret = MSA_API.process_content('ENDED', f'value get  {devices}', context, True)
# print(ret)