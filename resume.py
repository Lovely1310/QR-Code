# resume.py

def create_resume():
    name = "Monika"
    email = "monika9899803392@gmail.com"
    phone = "9319559215"
    education = "Bachelors of Computer Application, Gurugram University, 2024"
   
    skills = ["Python", "C", "Java", "C#, HTML, CSS, Visual Basic, knowledge of operating system"]

    with open("resume.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n\n")
        file.write("Education:\n")
        file.write(f"{education}\n\n")
        file.write("Experience:\n")
        
        file.write("\nSkills:\n")
        file.write(", ".join(skills) + "\n")

if __name__ == "__main__":
    create_resume()