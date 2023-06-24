
import plivo

auth_id = 'MANJKWMTQ3YZLJOWI3MJ'
auth_token = 'ZTk0MzYwNTdkYTJkNTI2MzZlNjRlMTAyNmM0NjRj'
phlo_id = '71b3cd61-3d32-48e2-838f-497a4d06706e' # https://console.plivo.com/phlo/list/
phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
phlo = phlo_client.phlo.get(phlo_id)
response = phlo.run()
print(str(response))
