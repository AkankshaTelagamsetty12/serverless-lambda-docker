# serverless-lambda-docker

## Built docker images for Text Summarization and Named Entity Recognition using Hugging Face.

Steps involved:

-  create a Python Lambda function with the Serverless Framework.
-  add the respective summarization and ner models to our function and create an individual inference pipeline.
-  Create a custom docker image for both
-  Deploy a custom docker image to Amazon ECR
-  Deploy AWS Lambda function with a custom docker image
-  Test Serverless APIs

![arch](https://user-images.githubusercontent.com/91446801/163518703-e9c06353-4bae-402a-84df-3cfe0739c533.png)


Follow the tutorial at https://www.philschmid.de/serverless-bert-with-huggingface-aws-lambda-docker to create docker images.
## Creating docker images:

<img width="1272" alt="Screen Shot 2022-04-15 at 12 11 55 AM" src="https://user-images.githubusercontent.com/91446801/163517295-d5839159-d3f0-4694-9f47-3ce8b5f5bf49.png">

<img width="1272" alt="Screen Shot 2022-04-15 at 12 12 41 AM" src="https://user-images.githubusercontent.com/91446801/163517859-9265c6d2-8468-4d53-aece-e9c2afae4f34.png">

## Deploying on AWS ECR

<img width="1439" alt="Screen Shot 2022-04-15 at 12 13 08 AM" src="https://user-images.githubusercontent.com/91446801/163517906-38a84493-f8c8-490d-9a5a-e12c36a20dc2.png">

## Testing using Postman
### Summarization

<img width="1431" alt="Screen Shot 2022-04-13 at 7 38 47 PM" src="https://user-images.githubusercontent.com/91446801/163517967-4828a9df-f0da-4ae8-82f8-98721ab4fc8c.png">

### Named Entity Recognition
<img width="1431" alt="Screen Shot 2022-04-13 at 8 36 38 PM" src="https://user-images.githubusercontent.com/91446801/163517972-a33e580a-65a9-4c85-9ef8-0d3d7d448a2b.png">


### Link for the codelabs:
https://codelabs-preview.appspot.com/?file_id=1376pofyspTVM8YhhbUKDEpiNaxczACY9KN0wI6lGPEg#0

## References:
 1. https://github.com/philschmid/serverless-bert-huggingface-aws-lambda-docker
 2. https://huggingface.co/dslim/bert-base-NER
 3. https://huggingface.co/sshleifer/distilbart-cnn-12-6
