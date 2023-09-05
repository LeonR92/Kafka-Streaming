# Kafka Streaming Project

**Introduction:**

Welcome to the GitHub repository for our Apache Kafka Data Pipeline Project! This project is designed to demonstrate the end-to-end process of generating fictional data, transmitting it through Apache Kafka, and finally storing it in AWS S3. This is a simple project that does not include advance Kafka concepts such as logging and producer acks settings and it has only one broker.

Below is the project's worfklow. Settings in Docker Compose file and Python code have to be tweaked if this project is to be run in the cloud or a VM.

Data Generator -> Kafka Producer -> Kafka Consumer -> AWS S3 -> CSV-Loader -> PowerBI/Tableau


**Description:**

**Project Overview:**
Data pipelines play a crucial role in modern data-driven organizations, enabling the seamless flow of data from various sources to downstream systems. Our Apache Kafka Data Pipeline Project showcases how to set up a simple yet robust data pipeline using Apache Kafka, Docker Compose, and AWS S3.

**Key Features:**

1. **Fictional Data Generation:** We've created a data generator that produces a fictional order table, simulating the kind of data you might encounter in a real-world scenario.

2. **Kafka Producer-Consumer:** Apache Kafka is used as the messaging backbone for data transmission. We have a Kafka producer that publishes data to Kafka topics, and a consumer that consumes and processes this data.

3. **Docker Compose for Scalability:** Docker Compose is leveraged for easy containerization and orchestration of the Kafka components, allowing you to scale your data pipeline as needed.

4. **AWS S3 Integration:** The data is eventually pushed to AWS S3 for storage and further analysis. We demonstrate how to interact with AWS S3 using the Boto3 library in Python.

5. **Data Transformation:** We've included data transformation steps, such as splitting names into first and last names, and extracting year and quarters from date strings.

6. **CSV Conversion:** You'll find code snippets for converting the processed data into CSV format, making it suitable for visualization in popular tools like Power BI or Tableau.

**Getting Started:**
To get started with this project, follow the comprehensive README documentation in this repository. It will guide you through setting up the entire data pipeline, from data generation to S3 storage and CSV conversion.

**Contributions:**
We welcome contributions and suggestions from the open-source community. If you have ideas for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request. Together, we can make this project even more valuable for data enthusiasts and practitioners.

**License:**
This project is licensed under the MIT License, ensuring that it's open and free to use for a wide range of purposes.

Thank you for exploring our Apache Kafka Data Pipeline Project! We hope you find it helpful and insightful for your data engineering endeavors. Happy coding and data streaming!
