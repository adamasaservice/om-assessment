

#variable "files" {
#  default = 5
#}

#resource "local_file" "foo" {
# count    = var.files
#  content  = "# Some content for file ${count.index}"
#  filename = "file${count.index}.txt"
#}


resource "example" "example" {
  for_each = toset(["db1", "db2", "db3", "db4", "db5"])

  # ...
}

moved {
  from = example.example[0]
  to   = example.example["db1"]
}

moved {
  from = example.example[1]
  to   = example.example["db2"]
}

moved {
  from = example.example[3]
  to   = example.example["db3"]
}

moved {
  from = example.example[4]
  to   = example.example["db4"]
}

moved {
  from = example.example[5]
  to   = example.example["db5"]
}
