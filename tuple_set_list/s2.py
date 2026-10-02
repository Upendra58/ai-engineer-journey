skills = {"Python", "Java", "SQL", "AWS"}
skills_lower = {skill.lower() for skill in skills}
print(skills_lower)
print("Python" in skills)
print("docker" in skills)
print("aws" in skills_lower)