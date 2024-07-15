# AI answerBOT API based on LLMs
The aim of this project is to create a Python API using the well-known FastAPI framework, primarily based on Pydantic. The API will be designed to allow users to make queries through an AI-based bot, which will respond to the questions entered via a user interface.


## Index
A user query is taken and responded to based on information taken from Wikipedia. For this purpose, the code is structured into the following classes:

- **Keywords()**: Extracts keywords from the user's query.
- **Info_Retriever()**: Retrieves relevant information based on the keywords extracted in the previous step by searching Wikipedia entries containing the keywords.
- **Info_Ranker()**: Classifies the retrieved documents based on their relevance to the query. In this case, the top 10 classified documents are selected.
- **RoBERTaAnswerGenerator()**: Uses the RoBERTa model to generate responses from the classified documents.


## How to use
This project provides an API for answering questions based on information obtained from Wikipedia. To use the API, follow these steps:

1. **Clone the Repository:**
   Clone this repository to your local machine using the following command:
    - *git clone https://github.com/fbayomartinez/fastapi.git*

2. **Install Dependencies:**
Make sure you have all the necessary dependencies installed. You can install them by means of *pip install* command in the project's root director.

3. **Run the API:**
Once all dependencies are installed, you can run the API by executing the following command in the terminal:

         uvicorn main:app --reload

   In this case, we have also introduced this lines to automate the process:
       
       if __name__ == "__main__":
            uvicorn.run("main:app", host="0.0.0.0", port=8010, log_level="debug", reload=True)
   
   This will start the FastAPI development server, and you can access the API from your browser or through tools like cURL or Postman.

4. **Make Queries:**
   You can make queries to the API by accessing the following URL in your browser:
   - *http://localhost:8010*
   
   Additionally, FastAPI provides us with an interface where we can find the endpoints we have created, allowing us to test the correct functionality of the application. To do this, we use the following URL:
   - *http://localhost:8000/docs*

The following are some examples of use:

![Captura de pantalla 2024-07-15 140455](https://github.com/user-attachments/assets/3a24a43f-979f-437f-b778-6cb48f38e0a1)

![Captura de pantalla 2024-07-15 141458](https://github.com/user-attachments/assets/628bdc52-6b19-4408-b654-18937e944a4f)


