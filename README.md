
# End-to-End Student Performance Predictor ML App with MLflow & DVC

Welcome to one of my most challenging and rewarding projects—a complete End-to-End Machine Learning Solution! This project goes beyond mere coding; it’s about building a robust, production-ready ML system leveraging cutting-edge tools like MLflow and DVC.




## Project Overview

This project focuses on predicting student performance in math using Linear Regression. With an accuracy of 89%, the system is designed to provide real-time predictions while ensuring scalability, version control, and reproducibility.
##  What’s Inside?
#### **Data Pipelines**
- **Data Ingestion:** Automated collection and preparation of raw data.
- **Data Transformation:** Data cleaning and scaling for accurate predictions.
- **Model Training:** Experimented with multiple algorithms to achieve an 89% accuracy using Linear Regression.
- Cross platform

#### **Prediction Pipeline**
- Built a system to handle real-time predictions based on user inputs like study time, attendance, and previous scores.

#### **MLflow Integration**
- **Track Experiments:** Compare model performances and log metrics effortlessly.
- **Monitor Progress:** Simplified monitoring for continuous improvement.

#### **DVC for Version Control**
- **Efficient Tracking:** Manage large datasets and model files with ease.
- **Collaboration Ready:** Seamlessly work in teams with reproducible workflows.

#### **Deployment**
- **Containerization:** Packaged the app using Docker for portability.
- **CI/CD Pipeline:** Automated deployments for consistent, error-free releases.

## Installation

#### Clone the Repository
```bash
  git clone https://github.com/chetanp2002/Python.git  
  cd your-repo-folder
```
#### Setup Environment
```bash
  pip install -r requirements.txt 
```

#### Run the App Locally
```bash
  python app.py   
```
#### Experiment with MLflow     
- Launch the MLflow UI:  
```bash
    mlflow ui         
```                                    

-  Visit http://localhost:5000 to compare models and view logs.

#### Leverage DVC for Version Control
- Pull Data & Models:
```bash
  dvc pull  
```
- Track Changes:
```bash
  dvc add your-data-file  
  git commit -m "Track new data with DVC"   
```
##  live Demo

![My Image](https://github.com/chetanp2002/Student_Performance/blob/main/static/Screenshot%20(48).png)
Deployed App Link: [Coming Soon]

## Project Structure

```bash
  📂 Project Root  
├── 📁 data                # Dataset files managed by DVC  
├── 📁 models              # Trained model files  
├── 📁 src                 # Source code  
│   ├── data_pipeline.py   # Data ingestion and transformation  
│   ├── train.py           # Model training scripts  
│   ├── predict.py         # Prediction pipeline  
├── 📄 app.py              # Main app script  
├── 📄 requirements.txt    # Python dependencies  
└── 📄 README.md           # Project documentation  

```



## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a PR.


## Connect with Me

[LinkedIn](https://www.linkedin.com/in/data-scientist-chetan/)

