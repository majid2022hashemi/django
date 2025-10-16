<!-- /home/majid/django/django/docs/docker-staticfiles-fix.md -->
# 🧩 Troubleshooting Static Files in Dockerized Django (Nginx + Gunicorn)

## 📘 Problem
When running a Django project with Docker, CSS and JS files were not loading from  
`http://localhost/static/...`  
and a **404 Not Found** error appeared in the browser.  
In fact, Nginx could not locate the `/app/staticfiles` directory.

---

## 🧠 Technical Analysis

1. **Static path not shared between web and Nginx**  
   The `staticfiles/` folder was created inside the Django container, but it was not available to Nginx.

2. **collectstatic in Dockerfile ran only inside web**  
   This meant the files existed only inside the web container, so Nginx could not access them.

3. **Incorrect Nginx configuration**  
   The `alias` path must point exactly to `/app/staticfiles/`.

---

## 🧩 Step-by-Step Solution

### 1️⃣ Dockerfile

```dockerfile
RUN python manage.py collectstatic --noinput

