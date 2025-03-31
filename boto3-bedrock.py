#imports
import boto3
import json

#create the bedrock
bedrock = boto3.client('bedrock-runtime')

#setting the prompt
prompt_data = """Command: Write me a blog about coaching employees as a leader.

Blog:
"""

#model specification

modelId = "amazon.titan-text-express-v1"
accept = "application/json"
contentType = "application/json"

#configuration parameters to invoke the model

body = json.dumps({
    "inputText" : prompt_data,
    "textGenerationConfig" : {
        "maxTokenCount" : 1000
    }
})


#invoke the model

response = bedrock.invoke_model(
    body = body, modelId = modelId, accept = accept, contentType = contentType
)

#parsing and displaying the output
response_body = json.loads(response.get('body').read())
output = response_body.get('results')[0].get("outputText")
print(output)