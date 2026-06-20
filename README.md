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

![Project Structure](screenshots/01-project-structure.png)

### Terminal Output

![Terminal Output](screenshots/02-terminal-output.png)

### IAM User Created

![IAM User](screenshots/03-iam-user-created.png)

### S3 Bucket Created

![S3 Bucket](screenshots/04-s3-bucket-created.png)

### EC2 Instance Running

![EC2 Instance](screenshots/05-ec2-instance-created.png)

### Architecture Diagram

![Architecture](screenshots/06-architecture-diagram.png)

---

## ✅ Key Features

* Infrastructure provisioning using code
* Automated AWS resource creation
* Modular Python scripts
* Reusable architecture
* GitHub portfolio project

---

## 👨‍💻 Author
**Rahul Sadafule**


