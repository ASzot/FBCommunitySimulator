class FbDataMgr:
	__instance = FBDataMgr()

	def __init__(self):
		self.likeData = []
	
	@staticmethod
	def getInstance():
		return self._instance

	def addLikeData(self, addLikeData):
		self.likeData.append(addLikeData)
