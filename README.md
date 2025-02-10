open bash
run: docker build -t my-web-server .
run: docker run -p 8000:8000 my-web-server
open browser: https://localhost/8000
