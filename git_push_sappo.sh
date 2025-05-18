#!/bin/bash

# === SETUP ===
REPO_NAME="sappo-ai-moral"
GITHUB_USER="ichal89"
TOKEN="ghp_xxxxxxxxxxxxxxxxx"  # GANTI dengan token kamu
COMMIT_MSG="Auto-update Sappo Moral Code"

# === DIRECTORY ===
cd /data/data/com.termux/files/home/sappo_ai || exit

# === GIT PUSH ===
git add .
git commit -m "$COMMIT_MSG"
git push https://$GITHUB_USER:$TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git
