FROM public.ecr.aws/sam/build-python3.9:1.66.0-20221129154443
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
