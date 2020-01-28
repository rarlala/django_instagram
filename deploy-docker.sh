#!/usr/bin/env sh
IDENTIFY_FILE="$HOME/.ssh/wps12th.pem"
HOST="ubuntu@54.180.97.157"
ORIGIN_SOURCE="$HOME/projects/wps12th/instagram"
DEST_SOURCE="/srv/"
SSH_CMD="ssh -i ${IDENTIFY_FILE} ${HOST}"

echo "== Docker 배포=="

# 서버 초기설정
echo "apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt update && sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y && apt -y autoremove'
echo "apt install python3-pip"
${SSH_CMD} -C 'sudo apt -y install python3-pip'

# pip freeze
echo "pip freeze"
"$HOME"/.pyenv/versions/3.7.5/envs/wps-instagram-env/bin/pip freeze > "$HOME"/projects/wps12th/instagram/requirements.txt

echo "finish!"
