from abc import ABC, abstractmethod
import random 

class Runnable(ABC):
  @abstractmethod
  def invoke(self,input_data):
    pass


class NakliLLM(Runnable):

  def __init__(self):
    print('LLM created')
  def invoke(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}
  def predict(self, prompt):
    

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}
  
llm= NakliLLM()


class NakliPromptTemplate(Runnable):

  def __init__(self, template,input_variables):
   self.template= template
   self.input_variables = input_variables

  def invoke(self, input_dict):
    return self.template.format(**input_dict)
  
  def format(self, input_dict):
   return self.template.format(**input_dict)
 

class RunnableConnector(Runnable):
  def  __init__ (self,Runnable_list):
    self.Runnable_list= Runnable_list
 
  def invoke(self, input_data):
    for runnable in self.Runnable_list:
     input_data=  runnable.invoke(input_data)
    return input_data

template= NakliPromptTemplate(
  template = 'write a {length} on {topics}',
  input_variables=['length','topics']

)

class StrOuputParser(Runnable):
  def __init__(self):
    pass
  def invoke(self,input_data):
    return input_data['response']
    
# parser =StrOuputParser()
# llm = NakliLLM()
# chain = RunnableConnector([template,llm,parser])

# print(chain.invoke({'length':'short','topics':'india'}))

template1 = NakliPromptTemplate(
  template = 'write a joke in {topics}',
  input_variables= ['topics']  
)
template2 = NakliPromptTemplate(
  template='write a summary of the {response}',
  input_variables = ['response']
)
llm = NakliLLM()
parser  = StrOuputParser()
chain1= RunnableConnector([template1,llm])
print(chain1.invoke({'topics':'ai'}))
chain2 = RunnableConnector([template2,llm,parser]
)
result= chain2.invoke({'response':'good'})
final_chain = RunnableConnector([chain1,chain2])
result= final_chain.invoke({'topics':'cricket'})
print(result)


