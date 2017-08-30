from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.terminal256 import TerminalTrueColorFormatter
from pygments.lexers.python import Python3Lexer
import boto3
from datetime import datetime
import time
import os

for k in ["http_proxy", "https_proxy"]:
    if k in os.environ.keys():
        os.environ.pop(k)

U='\033[4m'
E='\033[0m'

def print_c(code):
    print(highlight(str(code), Python3Lexer(), TerminalTrueColorFormatter()), end='')
print()
print_c("import boto3")
f = open('/Users/lilfolr/Downloads/accessKeys.csv', 'r')
x = f.read()
AWS_ID, AWS_KEY = x.split('\n')[1].split(",")

sqs = boto3.client('sqs', aws_access_key_id=AWS_ID, aws_secret_access_key=AWS_KEY)
print_c("sqs = boto3.client('sqs')")

# CREATE A QUEUE
print()
input(U+"Creating the Queue"+E)
print_c("response = sqs.create_queue(QueueName='job_queue')")
response = sqs.create_queue(QueueName='job_queue')
print_c("QueueURL = response['QueueUrl']")
QueueURL = response['QueueUrl']
print_c("print(response)")
print_c(response)
