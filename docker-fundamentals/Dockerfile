FROM python:3.12
RUN pip install uv
COPY pyproject.toml uv.lock /src/
WORKDIR /src
RUN uv sync
COPY src/ /src
EXPOSE 8501
ENTRYPOINT ["uv", "run", "streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["app.py"]