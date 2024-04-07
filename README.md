# answerBOT based on AI + FastAPI 
The aim of this project is to create a Python API using the well-known FastAPI framework, primarily based on Pydantic. The API will be designed to allow users to make queries through an AI-based bot, which will respond to the questions entered via a user interface.


## Index
A user query is taken and responded to based on information taken from Wikipedia. For this purpose, the code is structured into the following classes:

- **Keywords()**: Extracts keywords from the user's query.
- **Info_Retriever()**: Retrieves relevant information based on the keywords extracted in the previous step by searching Wikipedia entries containing the keywords.
- **Info_Ranker()**: Classifies the retrieved documents based on their relevance to the query. In this case, the top 10 classified documents are selected.
- **RoBERTaAnswerGenerator()**: Uses the RoBERTa model to generate responses from the classified documents.


<!-- ## Instalación

Proporciona instrucciones sobre cómo instalar o configurar tu proyecto. Incluye requisitos previos si es necesario.

## Uso

Explica cómo utilizar tu proyecto. Proporciona ejemplos de código o capturas de pantalla si es necesario.
 -->

