#!/usr/bin/env sh

# EC2에 DOCKER 배포

IDENTIFY_FILE="$HOME/.ssh/wps12th.pem"
HOST="ubuntu@54.180.97.157"
ORIGIN_SOURCE="$HOME/projects/wps12th/instagram"
DOCKER_REPO="devsuji/wps-instagram"
SSH_CMD="ssh -i ${IDENTIFY_FILE} ${HOST}"

echo "== Docker 배포=="

# 서버 초기설정
echo "apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt update && sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y && apt -y autoremove'
echo "apt install docker.io"
${SSH_CMD} -C 'sudo apt -y install docker.io'

# pip freeze
echo "pip freeze"
"$HOME"/.pyenv/versions/3.7.5/envs/wps-instagram-env/bin/pip freeze > "${ORIGIN_SOURCE}"requirements.txt

echo "poetry export"
poetry export -f requirements.txt > requirements.txt

# docker build
echo "docker build"
# 이 과정에서 poery export를 사용해서 requirements.txt 생성
# > dev 패키지는 설치하지 않도록 한다. (공식문서 또는 사용법 보기)

docker build -q -t ${DOCKER_REPO} -f Dockerfile "${ORIGIN_SOURCE}"

# docker push
echo "docker push"
docker push ${DOCKER_REPO}

# docker stop
echo "docker stop"
${SSH_CMD} -C 'sudo docker stop instagram'

# docker pull
echo "docker pull"
${SSH_CMD} -C 'sudo docker pull devsuji/wps-instagram instagram'

# 로컬의 aws profile을 전달
${SSH_CMD} -C "sudo rm -rf /home/ubuntu/.aws"
scp -q -i "${IDENTITY_FILE}" -r "$HOME/.aws" ${HOST}:/home/ubuntu/

echo "screen settings"
# 실행중이던 screen 종료
${SSH_CMD} -C 'screen -X -S docker quit'

# screen 실행
${SSH_CMD} -C 'screen -S docker -d -m'

# 실행중인 세션에 명령어 전달
${SSH_CMD} -C "screen -r docker -X stuff 'sudo docker run --rm -it -p 80:8000 --name=instagram devsuji'"

echo "finish!"
