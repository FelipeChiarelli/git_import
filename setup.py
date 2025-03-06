from setuptools import setup, find_packages

setup(
    name="git_import",  # Nome do pacote no PyPI
    version="0.1.0",  # Versão inicial
    packages=find_packages(),  # Descobre automaticamente os pacotes
    install_requires=[
        "requests"  # Dependências necessárias
    ],
    author="Felipe Chiarelli",
    author_email="felipechia8@gmail.com",
    description="Importa arquivos Python de repositórios GitHub (públicos ou privados).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FelipeChiarelli/git_import",  # URL do repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
