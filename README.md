This project implements a web application using a prediction model of valve condition based on presure and volume data. The application consists of two main parts: a backend that handles prediction logic and a frontend to display the results. The backend is developed with **Flask**, and the frontend is built with **Streamlit**.

The prediction model is located in the file `mmodel_rf.pkl`, and from this model, an SQLite database (`Predictions`) is generated to store the predictions. The entire project is containerized using **Docker** to simplify deployment and execution.
