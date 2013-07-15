'''
Created on Jul 8, 2013

@author: nirmal
'''

class Aspects(object):
    ''' Constants that will be used to associate a category
    with and generate a tag for a Narrative Entry.
    '''
    # User Profile
    USER_IP = 'User-IP'

    
    @classmethod
    def generator_aspects(cls, context):
        aspect = {}
        aspect[cls.USER_IP] = context.get('x-forwarded-for', None)
        return aspect
        
        
    
