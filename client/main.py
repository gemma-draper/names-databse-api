import requests
import json

# GET
get_response = requests.get()


# POST
name_to_post = {
    'id': '',
    'first_name': '',
    'last_name': ''
}
post_response = requests.post(url, data=json.dumps(name_to_post))

# PUT
name_to_update = {}
put_response = requests.put(url, data=name_to_update)

# DELETE
name_to_delete = {}
del_response = requests.delete(url, name_to_delete)

