#!/bin/bash
docker build -t pytester . ; docker run -p 8888:5000 pytester
