#imports
import boto3
from langchain.llms.bedrock import bedrock
#from bedrock_langchain import bedrock

#create bedrock client 

boto3_client = boto3.client('bedrock-runtime')

#setting model inference parameters

inference_modifier = {
    "temperature" : 0.5,
    "top_p" : 1,
    "max_tokens_to_sample" : 100
}


#create the llm

llm = bedrock(
    model_id="",
    client = boto3_client,
    model_kwargs = inference_modifier
)

#generate the response

response = llm.invoke (""""
    Human: Write an email from Diogo, Hiring Manager,
    welcoming a new employee "Favour Tar" to the company on his first day.
                       
                    
    Answer:""")

#display the result
print(response)