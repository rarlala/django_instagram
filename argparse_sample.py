# ./docker-run-secrets.py <cmd> 뒤에 <cmd>내용을 docker run <cmd>처럼 실행해주기
# 지정하지 않으면 /bin/bash를 실행
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cmd", type=str, nargs='*',default='')
args = parser.parse_args()
print(args.cmd)