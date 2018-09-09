import pickle
import boto3

class PySwiss(object):
    def __init__(self):
        self.client = boto3.client('s3')
    
    def put(self, obj, bucket, key):
        pickled_obj = pickle.dumps(obj)
        self.client.put_object(Body=pickled_obj, Bucket=bucket, Key=key)
        
    def get(self, bucket, key):
        try:
            obj = self.client.get_object(Bucket=bucket, Key=key)
            new_pickled_obj = obj['Body'].read()
            return pickle.loads(new_pickled_obj)
        except Exception as e:
            # print(e)
            print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))