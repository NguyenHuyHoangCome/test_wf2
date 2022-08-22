from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()

dev_var.add('devices.0.id', var_type='Device')

dev_var.add('device')
dev_var.add('drop')
dev_var.add('list_device')


context = Variables.task_call(dev_var)


devices = context['devices']
# context['drop'] = devices

# context['list'] = devices

ret = MSA_API.process_content('ENDED',
                              f'Firewall service created. {len(context["devices"])} Managed Entity selected',
                              context, True)
print(ret)
