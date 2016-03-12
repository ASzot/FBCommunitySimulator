from Core.Singleton import Singleton

@Singleton
class FbDataMgr:
	def addLikeData(self, addLikeData):
		self.likeData.append(addLikeData)
