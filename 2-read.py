from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.terminal256 import TerminalTrueColorFormatter
from pygments.lexers.python import Python3Lexer
import boto3
import time
from datetime import datetime
import os

for k in ["http_proxy", "https_proxy"]:
    if k in os.environ.keys():
        os.environ.pop(k)

U='\033[4m'
B='\033[1m'
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

QueueURL = input("Enter Queue URL:")
print()
input(U+"Poll Queue"+E)
try:
    i=0
    print_c("response = sqs.receive_message(QueueUrl=QueueURL)")
    while True:
        response = sqs.receive_message(QueueUrl=QueueURL)
        if "Messages" not in response.keys():
            print(U+str(i)+": 0 message(s) to process."+E)
        else:
            print()
            print(U+"{} message(s) to process".format(str(len(response['Messages'])))+E)
            msg = response['Messages'][0]
            RH, data = msg['ReceiptHandle'], msg['Body']
            print_c("msg = response['Messages'][0]")
            print_c("RH, data = msg['ReceiptHandle'], msg['Body']")
            print_c("print(data)")
            print(data)
            print_c("sqs.delete_message(QueueUrl=QueueURL, ReceiptHandle=RH)")
            sqs.delete_message(QueueUrl=QueueURL, ReceiptHandle=RH)
        i+=1
        time.sleep(1)
except KeyboardInterrupt:
    pass

