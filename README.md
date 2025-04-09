# 📂 ResourceManager
ResourceManager is a Django REST Framework (DRF) based backend system for managing user accounts and educational materials.
This project is structured for scalability, clean API design, and Docker-based deployment. It's ideal for use in educational platforms or resource-sharing systems.

## 🚀 Features
> - 🧑‍💼 User registration, login, and profile management
> - 📚 Create and manage categorized  materials
> - 🔐 Token-based authentication via Django REST Framework
> - ⚙️ Fully Dockerized for quick local setup
> - 🛠 Modular code structure for future API expansion

## 🧰 Tech Stack
> - Backend:
>   - Python 3.11
>   - Django
>   - Django Rest Framework
>
> - Database: 
>   - PostgreSQL
>
> - Containerization:
>    - Docker & Docker Compose

## 📁 Project Structure
```bash
ResourceManager/
├── config/                    # Project configuration 
├── materials/                 # App for managing  materials
│   ├── models.py              # Material model
│   ├── serializers.py         # API serializers
│   └── views.py               # Material views
├── users/                     # Custom user management app
│   ├── models.py              # User model
│   └── views.py               # Auth-related views
├── docker-compose.yaml        # Docker service definitions
├── Dockerfile                 # Docker image setup
├── requirements.txt           # Dependencies
└── manage.py                  # Django project runner
```

## ⚙️ Installation
### 💻 Local Development

#### Clone the Repository:
```bash
git clone https://github.com/xinis002/ResourceManager.git
```

#### Navigate to the Project Directory:
```bash
cd ResourceManager
```

#### Run with Docker
```bash
docker-compose up --build
```
##### App will be available 
```bash
http://localhost:8000/
```
##### To enter the container shell:
```bash
docker-compose exec web bash
```

## 🔐 Authentication
ResourceManager uses token-based authentication.
To authenticate, send a ```POST``` request to ```/api/token/``` with credentials.
Use the received token in headers:
```bash
Authorization: Token your_token_here
```

## 🧪 Testing
To run tests inside the container:
```bash
docker-compose exec web python manage.py test
```

## 🤝 Contributing
> Contributions are welcome! 
> Please fork the repository and submit a pull request with your changes.
> 1. Fork the repository
> 2. Create a new branch ```git checkout -b feature-name```
> 3. Commit your changes
> 4. Push to your fork
> 5. Open a pull request


## 📝 License
This project is open-source and available under the MIT License.






