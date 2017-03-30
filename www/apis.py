__author__='Lilian Cai'

'''
JSON API definition
'''

import json,logging,inspect,functools

class APIError(Exception):
	'''
	the base error class contains required error optional field and optional message
	'''
	def __init__(self,field,message=''):
		super(APIError,self).__init__(message)
		self.error=error
		self.data=data
		self.message=message
		#Field is a sql type means data type inter string or boolean


class APIValueError(APIError):
	'''
	Indicate the input value has error or invalid. 
	The data specifies the error field of input form.
	'''
	def __init__(self,field,message=''):
		super(APIValueError,self).__init__('value:invalid',field,message)

class APIResourceError(APIError):
	'''
	Indicate the resource was not found.the data specifies the resource name.
	'''
	def __init__(self,field,message=''):
		super(APIResourceError,self).__init__('value:notfound',field,message)

class APIPermissionError(APIError):

	"""indicate the api has no permission """
	def __init__(self, message=''):
		super(APIPermissionError, self).__init__('value:permissionforbidden','permission',message)



