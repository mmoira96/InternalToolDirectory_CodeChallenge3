# InternalToolDirectory_CodeChallenge3
Internal Tool Directory built with Django (MVT). Includes a CompanyTool model stored in SQLite, data managed via Django Admin, and a card-style UI that conditionally renders cloud vs. local tools using templates and template inheritance. It demonstrates: 

- Django project configuration in PyCharm  
- Database persistence with SQLite  
- Use of Django Admin  
- Conditional rendering in templates  
- Template inheritance (`base.html`)  
- Routing with `urls.py`  

## Features  

The application allows an IT department to:  

- Store software tools in a database  
- Indicate which department uses each tool  
- Mark whether a tool is cloud-based or locally installed  
- Display tools in a clean card-style interface  
- Show cloud tools in blue with a ☁️ icon and local tools in green with a 🖥️ icon  

---

## Data Model  

The project uses a `CompanyTool` model with the following fields:  

| Field | Type | Description |
|------|------|-------------|
| `tool_name` | CharField | Name of the software tool |
| `department` | CharField | Department using the tool |
| `is_cloud_based` | BooleanField | Whether the tool is cloud-based |

---

##  How to Run the Project  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/mmoira96/InternalToolDirectory_CodeChallenge3.git
cd InternalToolDirectory


