from setuptools import setup, find_packages

setup(
    name="agenticflow-ai",
    version="1.0.0",
    description="Enterprise Multi-Agent Workflows, LangGraph Architectures & Autonomous AI Systems",
    author="Nachiket Gadilohar",
    author_email="nachiketlohar0306@gmail.com",
    url="https://github.com/nachiket0987/agenticflow-ai",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "langgraph>=0.2.0",
        "langchain>=0.3.0",
        "langchain-openai>=0.2.0",
        "langchain-anthropic>=0.2.0",
        "langchain-community>=0.3.0",
        "langchain-core>=0.3.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "tavily-python>=0.5.0",
        "pypdf>=4.0.0",
        "requests>=2.31.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
