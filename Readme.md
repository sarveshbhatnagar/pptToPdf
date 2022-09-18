# How to use docker

1. write a basic python code (main.py in this case)
2. write the Dockerfile
3. build the image using docker build -t testproj:1.0 .
   > Note that in this case, testproj is project name and 1.0 is tag.
4. created docker-compose.yml
5. used docker-compose command as follows: docker-compose -f docker-compose.yml up

> When Rerunning, just use step 5.
> When you want to build and use, run step 3 and 5.

TODO check changing ENV HOME=/tmp and remove that config from lambda configurations.
