import boto3
import os

def lambda_handler(event, context):
    glue_client = boto3.client("glue")

    # either set as env var in Lambda console or just hardcode here
    job_name = os.environ.get("GLUE_JOB_NAME", "s3-etl-dak")

    try:
        job_args = event.get("job_args", {})

        response = glue_client.start_job_run(
            JobName=job_name,
            Arguments=job_args
        )

        return {
            "statusCode": 200,
            "body": f"Started Glue job {job_name} with JobRunId: {response['JobRunId']}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error starting Glue job {job_name}: {str(e)}"
        }
