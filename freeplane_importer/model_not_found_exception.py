class ModelNotFoundException(Exception):
	def __init__(self, model_name):
		self.model_name = model_name