import abc, math, pprint

class Tree( metaclass = abc.ABCMeta ):
	"""abstract base class for tree nodes """

	@abc.abstractmethod
	def insert( self, value ):
		"""insert a value in subtree rooted at this node"""
		"""a possibly new subtree is returned"""
		return

	@abc.abstractmethod
	def delete( self, value ):
		"""delete a value from subtree rooted at this node"""
		"""a possibly new subtree is returned"""
		return

    @abc.abstractmethod
    def search(self, value):
        """ search tree for a given value""""
        return 

	@abc.abstractmethod
	def get( self ):
		"""return in an array (in ascending order) values in subtree rooted at this node"""
		return

	@abc.abstractmethod
	def depth( self ):
		"""return max depth of subtree rooted at this node"""
		return

	@abc.abstractmethod
	def check( self ):
		"""verify the subtree is internally consistent"""
		return

	@abc.abstractmethod
	def walk( self ):
		"""print subtree to terminal; for debugging only"""
		return
