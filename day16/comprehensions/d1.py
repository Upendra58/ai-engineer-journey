#dictionary comprehension

names = ["alice", "bob", "charlie"]
name_length ={name: len(name) for name in names} #for dict use {}
print(name_length)