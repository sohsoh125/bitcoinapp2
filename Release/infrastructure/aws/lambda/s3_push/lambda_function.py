import boto3
import os
import tempfile
from urllib.request import urlretrieve
import time
from datetime import datetime
from time import time

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    # 解析生データのURLスクレイピング情報
    UA = 'https://api.blockchain.info/charts/n-unique-addresses?timespan=2years&format=csv'
    TR_num = 'https://api.blockchain.info/charts/n-transactions?timespan=2years&format=csv'
    TR_qa = 'https://api.blockchain.info/charts/output-volume?timespan=2years&format=csv'
    VA = 'https://api.blockchain.info/charts/market-price?timespan=2years&format=csv'

    # 解析生データ名称
    UA_name = 'uniqueaddress_2years.csv'
    TR_num_name = 'transaction_num_2years.csv'
    TR_qa_name = 'transaction_qa_2years.csv'
    VA_name = 'transaction_qa_2years.csv'

    # 一時ディレクトリのパス
    tmpdir = '/tmp/'
    file1 = tmpdir + UA_name
    file2 = tmpdir + TR_num_name
    file3 = tmpdir + TR_qa_name
    file4 = tmpdir + VA_name

    # スクレイピングの実施
    urlretrieve(UA, file1)
    urlretrieve(TR_num, file2)
    urlretrieve(VA, file3)
    urlretrieve(TR_qa, file4)

    # S3保管名
    today = datetime.fromtimestamp(time())
    t = today.strftime('%Y-%m-%d-')
    UA_save_name = 'unique_address' + '/' + t + UA_name
    TR_save_num_name = 'transaction_number' + '/' + t + TR_num_name
    TR_save_qa_name = 'transaction_quantity' + '/' + t + TR_qa_name
    VA_save_name = 'value' + '/' + t + VA_name

    # S3にファイルをアップロード
    backet_name = 'bitcoinforecast-storage'
    s3.meta.client.upload_file(file1, backet_name, UA_save_name)
    s3.meta.client.upload_file(file2, backet_name, TR_save_num_name)
    s3.meta.client.upload_file(file3, backet_name, TR_save_qa_name)
    s3.meta.client.upload_file(file4, backet_name, VA_save_name)