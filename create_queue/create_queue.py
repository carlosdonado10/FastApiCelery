import boto3


if __name__ == '__main__':

    queue = boto3.client(
                'sqs',
                endpoint_url="http://queue2:9324",
                region_name='elasticmq',
                aws_secret_access_key='x',
                aws_access_key_id='x',
            )

    queue_url=queue.create_queue(QueueName='dev')['QueueUrl']
    queue_url=queue.get_queue_url(QueueName='dev')['QueueUrl']
    print(queue_url)