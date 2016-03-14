import base64
import uuid

def get_a_uuid():
	r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
	r_uuid = r_uuid.replace('=', '')
	r_uuid = r_uuid.replace('-', '')
	return r_uuid
