# Real-Time-Data-Pipeline-for-X-Twitter-Analytics-Using-Apache-Airflow-

The main agenda behind the project is about building an end-to-end data engineering pipeline.
The project focuses on extracting data from X(Twitter) using Python, transforming it with Pandas, and storing the processed data in an Amazon S3 bucket, all orchestrated through Apache Airflow.

**Technologies used** :
- AWS EC2: AMI(ubuntu o/s) , t2.small(instance type)
- AWS S3 
- Apache Airflow: orchestration tool used to monitor data pipelines and other workflows.
- Python libraries: pandas, tweepy, s3fs (sudo pip install pandas tweepy s3fs)
- X(twitter) APIs

**Commands used(terminal)**:
C:\Users\Admin>
     step1.└── C:\Users\Admin>cd C:\Users\Admin\Downloads
                              └──(command) └──(path of sahith key(key pair))
         step2.└── C:\Users\Admin\Downloads>"ssh -i paste SSH client "
                                              └── aws connect 2 instance (ssh client)
             step3.└── ubuntu@ip-address:~$   (we get this finally, connection b/w EC2 --> Ubuntu successfull )   

sudo apt-get update
 └──sudo apt install python3-venv
  └── python3 -m venv airflow_env
    └── source airflow_env/bin/activate
      └── pip install --upgrade pip
        └── pip install apache-airflow
          └── pip install pandas s3fs tweepy

**Project Overview** : 
- Data Extraction: Utilizes the Twitter API to fetch tweets and related metadata.
- Data Transformation: Processes and cleans the extracted data using Python's Pandas library to ensure it's structured appropriately for analysis.
- Data Storage: Stores the transformed data in Amazon S3, a scalable object storage service.
- Workflow Orchestration: Employs Apache Airflow to automate and manage the entire workflow, ensuring tasks are executed in the correct sequence and can be monitored effectively.

**Real-World Applications** :
This project serves as a foundational example for several real-world scenarios:                                                                                                                                      
- Social Media Analytics: Organizations can monitor brand mentions, sentiment, and trending topics by analyzing Twitter data.
- Market Research: Companies can gain insights into consumer opinions and industry trends by examining tweet patterns and content.
- Event Monitoring: Real-time tracking of events, news, or product launches becomes feasible by processing live Twitter streams.
- Data Engineering Proficiency: The project offers hands-on experience with tools like Apache Airflow, enhancing skills in building and managing data pipelines.
