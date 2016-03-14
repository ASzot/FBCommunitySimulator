from Core.Singleton import Singleton

@Singleton
class FbDataMgr:
	def __init__(self):
		self.likeData = []	

	def addLikeData(self, addLikeData):
		self.likeData.append(addLikeData)
