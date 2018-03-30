# Custom_AWS_Panel
This code is used to create your own AWS Customized Panel. 

# How to create your AWS Panel in Ubuntu:

apt-get update -y

apt-get install docker.io -y

git clone git@github.com:chandraprakash1392/Custom_AWS_Panel.git

cd Custom_AWS_Panel

// open the code frontend.py
// Edit the self.path in frontend.py as per your regions in AWS

docker build -t <docker_image_tag> .

docker run -it --name aws_custom_panel -p 3000:3000 <docker_image_tag>
