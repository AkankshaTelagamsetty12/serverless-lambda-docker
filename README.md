# serverless-lambda-docker

## Built docker images for Text Summarization and Named Entity Recognition using Hugging Face.

Steps involved:

-  create a Python Lambda function with the Serverless Framework.
-  add the respective summarization and ner models to our function and create an individual inference pipeline.
-  Create a custom docker image for both
-  Deploy a custom docker image to Amazon ECR
-  Deploy AWS Lambda function with a custom docker image
-  Test Serverless APIs

<img width="1272" alt="Screen Shot 2022-04-15 at 12 11 55 AM" src="https://user-images.githubusercontent.com/91446801/163517295-d5839159-d3f0-4694-9f47-3ce8b5f5bf49.png">


References:
 1. https://github.com/philschmid/serverless-bert-huggingface-aws-lambda-docker
 2. https://huggingface.co/dslim/bert-base-NER
 3. https://huggingface.co/sshleifer/distilbart-cnn-12-6
