# aws-resource-provisioning-boto3
# 🚀 Automated AWS Resource Provisioning using Python boto3

## 📌 Project Overview

This project demonstrates Infrastructure as Code (IaC) using Python and AWS boto3. The automation script provisions AWS resources without manual configuration through the AWS Console.

The script automatically creates:

* AWS IAM User
* Amazon S3 Bucket
* Amazon EC2 Instance

---

## 🎯 Objective

Automate AWS infrastructure provisioning using Python scripts and boto3 SDK.

---

## 🛠️ Technologies Used

* Python 3
* AWS boto3
* AWS IAM
* Amazon S3
* Amazon EC2
* AWS CLI
* Git & GitHub

---

## 📂 Project Structure

```text
aws-resource-provisioning-boto3
│
├── main.py
├── iam.py
├── s3.py
├── ec2.py
├── requirements.txt
├── README.md
└── screenshots
```

---

## 🏗️ Architecture

```text
Developer
    │
    ▼
Python Script (main.py)
    │
    ▼
boto3 SDK
    │
 ┌──┴───────┬───────┐
 ▼          ▼       ▼

IAM        S3      EC2
User      Bucket  Instance

    │
    ▼
AWS Infrastructure Created
```

---

## ⚙️ Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Rahulsada-518/aws-resource-provisioning-boto3.git
cd aws-resource-provisioning-boto3
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install boto3
```

### Configure AWS

```bash
aws configure
```

Provide:

* AWS Access Key
* AWS Secret Key
* Region: ap-south-1
* Output: json

---

## ▶️ Run Project

```bash
python main.py
```

Expected Output:

```text
🚀 AWS Automation Started
✅ IAM User Created
✅ S3 Bucket Created
✅ EC2 Instance Created
🎉 AWS Automation Completed
```

---

## 📸 Project Screenshots

### Project Structure

<img width="236" height="344" alt="01-project-structure" src="https://github.com/user-attachments/assets/f2ec37ba-6af0-4a09-b587-b84d375cf8e0" />


### Terminal Output

<img width="496" height="96" alt="02-terminal-output" src="https://github.com/user-attachments/assets/cf9e0664-f0a5-4cdf-8bf0-fc475f990a91" />


### IAM User Created

<img width="956" height="277" alt="03-iam-user-created" src="https://github.com/user-attachments/assets/60aa5405-3dc2-4ade-be91-fade6c8a4bbc" />


### S3 Bucket Created

<img width="637" height="356" alt="04-s3-bucket-created" src="https://github.com/user-attachments/assets/e41d47cd-c76a-4a8b-be10-c19aa0608e63" />


### EC2 Instance Running

<img width="959" height="178" alt="05-ec2-instance-created" src="https://github.com/user-attachments/assets/edaa2643-1352-4648-9c67-91f6b56bafff" />

<img width="773" height="317" alt="boto_3 installation" src="https://github.com/user-attachments/assets/ee5cc8c8-af65-444a-bfc5-429cdca47d99" />




