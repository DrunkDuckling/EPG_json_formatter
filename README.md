# EPG_json_formatter
 Program used to translat EPG structured in json into human readable format as text. The file "lambda_function.py" is downloaded from AWS Lambda and runs there with the use of a trigger that is an API gateway, using REST. The code accepts a json formatted EPG in the body of the POST. The code have been tested both on AWS' own site and using the program Postman. 
 
 Had a bit of fun with it, so also created a Flask server that have more or less the same code as the AWS, but runs locally. Also created a python file that uses requests that can post to botht he local and online web service. 

# Thoughts on Input data model:
I think that the input data model works fine, it makes sense and is structured so that is easier for computers to work with. However if it where me, i would maybe make the time in epoch instead as it could provide aditional information. 
