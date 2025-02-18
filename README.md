# My Web App 🚀

This is a **full-stack web application** that consists of:
- **Backend:** Django (REST API)
- **Frontend:** React (Node.js)
- **Database:** PostgreSQL
- **Dockerized Setup:** Uses Docker Compose for easy deployment

---

## **🚀 Getting Started**
Follow these steps to set up and run the application on your local machine.

### **1️⃣ Clone the Repository**
```bash
git clone <REPO_URL>
cd Basic-Web-App/my-web-app
```

---

## **2️⃣ Prerequisites**
Ensure you have the following installed:
- **Docker & Docker Compose** → [Install Docker](https://docs.docker.com/get-docker/)
- **Git** → [Install Git](https://git-scm.com/)

---

## **3️⃣ Run the Application**
To build and start all services (backend, frontend, and database), run:
```bash
docker-compose up --build
```

This will:
- Set up the **PostgreSQL database**
- Run the **Django backend**
- Start the **React frontend**

---

## **4️⃣ Load Sample Data**
After the containers are running, load initial data into the database:
```bash
docker-compose exec backend python load_data.py
```

---

## **5️⃣ Access the Application**
Once everything is up and running, access the application at:
- **Frontend UI:** [http://localhost:3000](http://localhost:3000)
- **Backend API:** [http://localhost:8000/api/items/](http://localhost:8000/api/items/)
- **Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)  
  (Default credentials can be set using `createsuperuser`)

---

## **6️⃣ Stopping the Application**
To stop all running containers, use:
```bash
docker-compose down
```

To stop and remove everything including volumes (⚠️ This will delete database data):
```bash
docker-compose down -v
```

---

## **🔧 Optional Commands**
### **Check Running Containers**
```bash
docker ps
```

### **Restart a Specific Service**
```bash
docker-compose restart backend
```

### **Apply Database Migrations**
If needed, apply migrations manually:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

---

## **📌 Notes**
- If the backend gives **CORS errors**, ensure `django-cors-headers` is installed and properly configured.
- If `docker-compose up` fails, try **rebuilding** the images:
  ```bash
  docker-compose down
  docker-compose up --build
  ```
- If you need an admin account, create one using:
  ```bash
  docker-compose exec backend python manage.py createsuperuser
  ```

---

## **🛠️ Troubleshooting**
### **Frontend Not Fetching Data?**
- Open browser **Developer Tools (F12) → Console**
- Check if there are **CORS issues** or **network failures**
- Try restarting the backend:
  ```bash
  docker-compose restart backend
  ```

### **Database Issues?**
- Make sure migrations are applied:
  ```bash
  docker-compose exec backend python manage.py migrate
  ```
- Check if the database is running:
  ```bash
  docker-compose logs db
  ```

---

## **📜 License**
This project is open-source. Feel free to modify and contribute!

---

**🚀 Happy Coding! 🚀**
