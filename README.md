# EPG_json_formatter
 Program used to translat EPG structured in json into human readable format as text. The file "lambda_function.py" is downloaded from AWS Lambda and runs there with the use of a trigger that is an API gateway, using REST. The code accepts a json formatted EPG in the body of the POST. The code have been tested both on AWS' own site and using the program Postman. 

# Thoughts on Input data model:
I think that the input data model works fine, it makes sense and is structured so that is easier for computers to work with.
