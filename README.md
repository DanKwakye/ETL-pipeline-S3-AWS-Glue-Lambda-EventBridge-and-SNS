#  AWS Data Pipeline Migration Project

Last week, I wrapped up a project that had me deep in the AWS ecosystem  and it was a game changer.

An organization had been running everything on local servers (you know the story: maintenance headaches, storage limits, and that one server that decides to crash at 2 AM).  
My task? **Migrate their data processing to the cloud and make it lean, automated, and scalable.**

---

##  What I Built

### 1. **ETL Pipeline on AWS**
- Raw data lands in **Amazon S3** (raw zone).  
- Data gets processed in **AWS Glue**.  
- Transformed data flows into a curated **S3 bucket** ready for analytics.  

### 2. **Automation with AWS Lambda**
- Lambda triggers the ETL flow automatically.  
- No more manual kicks — everything runs on schedule or event triggers.  

### 3. **Event-Driven Monitoring**
- **Amazon EventBridge** + **SNS** handle alerts.  
- Automatic retries every minute to reduce false alarms.  

### 4. **Security Baked In**
- **IAM roles** designed with the principle of least privilege.  
- No over-permissioned access floating around.  

### 5. **CloudWatch Dashboards**
- Real-time monitoring of logs and metrics.  
- Simplified production monitoring and troubleshooting.  

---

##  Impact

- The pipeline processes **hundreds of thousands of records each week** without breaking a sweat.  
- Migrating from **on-prem to AWS** freed up local servers, reduced maintenance costs, and unlocked **elastic scaling** — paying only for what we use.  

💡 **In plain English:** fewer headaches, faster data, smarter decisions.

---

## 🛠️ Tech Stack

- **Amazon S3** – Data lake storage  
- **AWS Glue** – ETL processing  
- **AWS Lambda** – Automation  
- **Amazon EventBridge** – Event-driven workflows  
- **Amazon SNS** – Notifications  
- **Amazon CloudWatch** – Monitoring and logging  
- **AWS IAM** – Security and permissions  

---

##  Architecture Diagram

```mermaid
flowchart LR
    A[On-Prem Data] -->|Upload| B[S3 - Raw Zone]
    B -->|ETL Job| C[AWS Glue]
    C --> D[S3 - Curated Zone]
    D --> E[Analytics / BI Tools]

    subgraph Automation & Monitoring
        F[AWS Lambda] --> B
        G[Amazon EventBridge] --> F
        G --> H[SNS Alerts]
        H --> I[Team Notifications]
    end

    subgraph Security
        J[IAM Roles & Policies]
    end
