# Calyrex Chatbot

Calyrex is a Python-based chatbot web app developed with Chainlit, Langchain, and Ollama framework. This chatbot is designed to offer conversational interactions and is powered by locally
run CPU inference-only LLMs (Language Models).

## Features
- Conversational chatbot interface.
- Local CPU inference-only LLMs for better Data privacy, lower resource requirements and more flexibility.

## Installation and Usage

To build the Docker images and run the Docker containers for Calyrex, use the following command:

```bash
docker-compose up -d --build
```

This command will build the Docker images and launch the containers in detached mode.

## Accessing the Application

Once the containers are up and running, you can access the Calyrex chatbot app at:

```
http://localhost:3008
```


## App Configuration

### .env file

User can configure the following:

- Networking config.
- LLM models.

### Choice of Models

Default models are (can be changed from the .env file):

| Model                                              | Use                                | Parameters | Quantization |
|----------------------------------------------------|------------------------------------|------------|--------------|
| [gemma-instruct](https://ai.google.dev/gemma/docs) | Performs well for text generation. | 2B         | Q6\_k        |
| [deepseek-coder](https://deepseekcoder.github.io/) | Excels in coding-related tasks.    | 1.3B       | Q6\_k        |


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Status

The development of Calyrex is currently in progress. Stay tuned for updates and new features!

---

Thank you for exploring Calyrex!
