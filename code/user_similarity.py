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
        yield [user_id, 2]#businesses]
        
    def dummy_mapper(self, user_id, list_businesses):
        #print user_id,businesses
        """ returns "dummy", list of [user_id,Businesses]"""
        yield ["dummy", [user_id, list_businesses]]    
        
    def create_combinations(self, dummy_var, list_of_user_businesses):
        """ returns "dummy", list of [user_id,Businesses]"""
        mydict = {}
        for u, b in list_of_user_businesses:
            if u not in mydict:
                mydict[u] = [b]
            else:
                mydict[u].append(b)
                
        myUserBussList = []
        for u, bs in mydict.items():
            myUserBussList.append([u, bs])
        
        for i in range(len(myUserBussList)):
            for j in range(len(myUserBussList)):
                if i > j:
                    yield [myUserBussList[i], myUserBussList[j]]   
                    
    def calculate_jaccard(self, user1_businesses, user2_businesses):
        """Output user_id1, user_id2 whose jaccard_coefficient > = 0.5"""
        #print user1_businesses,user2_businesses
        u1, b1 = user1_businesses
        u2, b2 = user2_businesses

        b1_set = set(b1) 
        b2_set = set(b2)
        
        jaccard_coefficient = float(len(b1_set.intersection(b2_set))/len(b1_set.union(b2_set)))      
        if jaccard_coefficient >= 0.5:
            yield [ u1,u2]
        

    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(mapper=self.extract_users ),#reducer=self.join_businesses)]
                self.mr(mapper=self.dummy_mapper, reducer=self.create_combinations),
                self.mr(mapper=self.calculate_jaccard)]


if __name__ == '__main__':
    UserSimilarity.run()
