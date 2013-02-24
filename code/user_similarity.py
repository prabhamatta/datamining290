from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches, 
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/
    def extract_users(self, _, record):
        """Take in a record, filter by type=review, yield <user_id, business_id>"""
        if record['type'] == 'review':
            yield [record['user_id'], record['business_id']] 
            
    def join_businesses(self, user_id, businesses):
        """Output user_id, list of businesses"""
        yield [user_id, list(businesses)]
        
    def dummy_mapper(self, user_id, list_businesses):
        #print user_id,businesses
        """for each user==> returns "dummy",  [user_id,Businesses]"""
        yield ["dummy", [user_id, list_businesses]]    
        
    def create_combinations(self, dummy_var, list_of_user_businesses):
        """ returns "dummy", list of  all [user_id,Businesses]"""
        yield "dummy",list(list_of_user_businesses)
        
                    
    def calculate_jaccard(self, dummy, list_of_user_businesses):
        """Output user_id1, user_id2 whose jaccard_coefficient > = 0.5"""
        #print user1_businesses,user2_businesses
        for i in range(len(list_of_user_businesses)):
            for j in range(len(list_of_user_businesses)):
                if i > j:                            
                    u1,b1 = list_of_user_businesses[i]
                    u2,b2 = list_of_user_businesses[j]
                    b1_set = set(b1) 
                    b2_set = set(b2)
                    
                    jaccard_coefficient =  float(len(b1_set.intersection(b2_set)))/float(len(b1_set.union(b2_set)))
                    
                    #import pdb; pdb.set_trace()
                    #yield [[ u1,u2],jaccard_coefficient]
                    if jaccard_coefficient >= 0.5:
                        yield u1,u2
                    

    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(mapper=self.extract_users ,reducer=self.join_businesses),
                self.mr(mapper=self.dummy_mapper,reducer=self.create_combinations),
                self.mr(mapper= self.calculate_jaccard)]


if __name__ == '__main__':
    UserSimilarity.run()
