resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block
  tags = {
    Name = "vpc-terraform-jenkins"
  }
}

resource "aws_subnet" "subnet1" {
  cidr_block = var.subnet_block[0]
  availability_zone = var.subnet.az[0]
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "terraform-jenkins-subnet1"
  }
}

resource "aws_subnet" "subnet2" {
  cidr_block = var.subnet_block[1]
  availability_zone = var.subnet.az[1]
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "terraform-jenkins-subnet2"
  }
}

resource "aws_subnet" "subnet3" {
  cidr_block = var.subnet_block[2]
  availability_zone = var.subnet.az[0]
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "terraform-jenkins-subnet3"
  }
}

resource "aws_subnet" "subnet4" {
  cidr_block = var.subnet_block[3]
  availability_zone = var.subnet.az[1]
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "terraform-jenkins-subnet4"
  }
}