Taken from: https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions

To upload the image to Amazon ECR and create the Lambda function
Run the get-login-password command to authenticate the Docker CLI to your Amazon ECR registry.

Set the --region value to the AWS Region where you want to create the Amazon ECR repository.

Replace 111122223333 with your AWS account ID.

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-east-1.amazonaws.com
Create a repository in Amazon ECR using the create-repository command.

aws ecr create-repository --repository-name hello-world --region us-east-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
Note
The Amazon ECR repository must be in the same AWS Region as the Lambda function.

If successful, you see a response like this:

{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:111122223333:repository/hello-world",
        "registryId": "111122223333",
        "repositoryName": "hello-world",
        "repositoryUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world",
        "createdAt": "2023-03-09T10:39:01+00:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": true
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
Copy the repositoryUri from the output in the previous step.

Run the docker tag command to tag your local image into your Amazon ECR repository as the latest version. In this command:

docker-image:test is the name and tag of your Docker image. This is the image name and tag that you specified in the docker build command.

Replace <ECRrepositoryUri> with the repositoryUri that you copied. Make sure to include :latest at the end of the URI.

docker tag docker-image:test <ECRrepositoryUri>:latest

Example:

docker tag docker-image:test 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest
Run the docker push command to deploy your local image to the Amazon ECR repository. Make sure to include :latest at the end of the repository URI.

docker push 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest
Create an execution role for the function, if you don't already have one. You need the Amazon Resource Name (ARN) of the role in the next step.