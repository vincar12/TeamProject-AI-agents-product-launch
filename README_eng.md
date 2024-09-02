# **Intellagent**

![Logo Intellagent](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-018-hck-group-002/blob/main/images/logo-1.png)<br>
<p align="center" width="100%">
    <i>
    The intelligence behind every great decision.</i><br>
</p>

## Introduction
"Intellagent" is an AI-based platform that simplifies and optimizes your product launch process. It uses a team of specialized AI agents to analyze user input and provide data-driven strategies for a successful launch. With actionable insights and personalized recommendations, Intellagent ensures your product launch runs smoothly and makes an impact.

This project is powered by the **CrewAI** framework, which automates the creation of detailed reports and product launch plans. CrewAI coordinates autonomous AI agents, enabling efficient collaboration and execution of complex tasks.

## Framework
The project is powered by a team of AI agents, coordinated through CrewAI. Each agent is assigned a background, tasks, tools, and expected outcomes to perform its role. The project consists of five agents, each focused on different aspects of a product launch. They use the **Exa Search Tool**, which allows them to gather and analyze online information. Together, they collaborate to deliver a comprehensive report on the best strategies for launching a product based on the given input.

![How Intellagent Works](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-018-hck-group-002/blob/main/images/Crew_general.png)<br>
<p align="center" width="100%">
    <i>
    General overview of how Intellagent works.</i><br>
</p>

Intellagent operates by receiving input from the user, after which a team of AI agents processes the input according to their individual roles to conduct the necessary research and analysis. Once each agent completes its research and analysis, the final agent summarizes all the results and creates a comprehensive report based on the user's input.

![How Intellagent Works Specifically](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-018-hck-group-002/blob/main/images/Crew_specific.png)<br>
<p align="center" width="100%">
    <i>
    Specific workings of Intellagent.</i><br>
</p>

There are 5 agents, each with a specific task aligned with their role. Each agent is assigned a specific goal and backstory to optimize their research and analysis. Every task comes with a description and expected output, allowing the agents to complete their tasks according to the desired guidelines and results. The four agents responsible for research and analysis have tools such as *search*, *find similar*, and *get contents* to browse the web, find similar pages, and retrieve content from those pages for further analysis. The final agent is responsible for compiling a comprehensive report based on the research and analysis of the previous agents.

## Running the Script
- **Environment Configuration**: Set the environment variables in `env.txt` to `.env` for OpenAI, Exa, and Langchain.
- **Dependency Installation**: Run `pip install -r requirements.txt`.
- **Run the Script**: Run `streamlit run files/app.py` and enter your idea.

## Details & Explanation
- **Running the Script**: Run `streamlit run files/app.py` and enter the required information when prompted. This script will leverage the CrewAI framework to generate a product launch report for you.
- **Key Components**:
  - `./files/app.py`: The main script file.
  - `./files/tasks.py`: Main file containing task prompts.
  - `./files/agents.py`: Main file containing agent creation.
  - `./files/tools.py`: Main file containing tools for agents.

## References
Arenas-Olvera, A. (n.d.). Crew AI crash course step-by-step. Alejandro AO. https://alejandro-ao.com/crew-ai-crash-course-step-by-step/

## Contributors
- [**Heru**](https://github.com/herurmdn7)
- [**Vincar**](https://github.com/vincar12)
- [**Devon**](https://github.com/RichieDevon53)
