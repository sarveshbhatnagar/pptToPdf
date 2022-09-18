import boto3
import os


def lambda_handler(event, context):
    if("bucket" in event):
        s3Client = boto3.client("s3")
        obj = s3Client.get_object(
            Bucket=event["bucket"], Key=event["fileName"])
        with open('/tmp/' + event["fileName"], "wb") as f:
            f.write(obj["Body"].read())
        cmd = f'cd /tmp && libreoffice7.4 --headless --invisible --convert-to pdf "{event["fileName"]}"'
        tes = os.popen(cmd).read()
        print(tes)
        temp = event["fileName"].split(".")[:-1]
        newFileName = ".".join(temp) + ".pdf"
        print("Starting upload")
        res = s3Client.upload_file(
            '/tmp/'+newFileName, event["bucket"], newFileName)
        print(res, "Uploaded successfully")
        os.remove('/tmp/'+event["fileName"])

        return {
            'statusCode': 200,
            'msg': "successfully created pdf file."
        }
    return {
        'statusCode': 404,
        'msg': "Incorrect parameters sent!"
    }
