variable "aws_region" {}
variable "vpc_cidr_block" {}
variable "subnet_block" {
   type = list  
}
variable "subnet_az"{
    type = list
}