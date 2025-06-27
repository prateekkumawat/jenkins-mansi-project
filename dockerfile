FROM nginx:latest

# copy sorce code 
COPY src /usr/share/nginx/html/

# EXPOSE PORT
EXPOSE 80 