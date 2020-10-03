'''
Example only!!
static method - decorates with @staticmethod
class method - similar to static method,differ access to methods and class attributes, but no access to instance attributes, decorates with @classmethod
instance/object method - keyword self


'''

class Learning:
    score=0
    class_name="Learning"
    def __init__(self,subject):
        self.subject=subject
    @staticmethod
    def strategy(subject):
        print("*"*20,"Begin==>Method:strtegy","*"*20)
        print("Strategy==>hands on and application of :",subject)
        print("*"*20,"End==<Method:strtegy","*"*20,end="\n\n")
        
    @classmethod
    def get_the_class_name(cls):
        print("*"*20,"Begin==>classmethod","*"*20)
        print("The class is:",cls.class_name)
        try:
            print("Can i access instance attribute, subject:",subject)
        except Exception as e:
            print("sorry, could  not get instance attribute,got exception as:",str(e))
        print("*"*20,"End==<classmethod","*"*20,sep="\n")
    def i_am_learning(self):
        print("My class is:", self.class_name)
        print("The subject is:",self.subject)

if __name__=="__main__":
    rl=Learning("RL")
    Learning.strategy("RL-AgentEnvironment")
    Learning.get_the_class_name()
    rl.i_am_learning()
    
 '''
 output as:
 

******************** Begin==>Method:strtegy ********************                                                                                                                                                                                  
Strategy==>hands on and application of : RL-AgentEnvironment                                                                                                                                                                                      
******************** End==<Method:strtegy ********************                                                                                                                                                                                    
                                                                                                                                                                                                                                                  
******************** Begin==>classmethod ********************                                                                                                                                                                                     
The class is: Learning                                                                                                                                                                                                                            
sorry, could  not get instance attribute,got exception as: name 'subject' is not defined                                                                                                                                                          
********************                                                                                                                                                                                                                              
End==<classmethod                                                                                                                                                                                                                                 
********************                                                                                                                                                                                                                              
My class is: Learning                                                                                                                                                                                                                             
The subject is: RL                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                  
Program finished with exit code 0                                                                                                                                                                                                              
 '''
