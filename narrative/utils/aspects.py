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
    NO_LOGIN_SESSION='No-Login-Session'
    
    @classmethod
    def generator_aspects(cls, context,no_login_session=None):
        aspect = {}
        aspect[cls.USER_IP] = context.get('x-forwarded-for', None)
        if no_login_session:
            aspect[cls.NO_LOGIN_SESSION] = no_login_session
        return aspect
        
        
    
