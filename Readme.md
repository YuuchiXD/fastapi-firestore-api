# FastAPI Firestore API

## 📌 Deskripsi
REST API sederhana menggunakan **FastAPI** dan **Firebase Firestore** untuk melakukan operasi CRUD pada data pengguna.

## ⚙️ Fitur
- ✅ CRUD User (Create, Read, Update, Delete)
- ✅ Validasi data dengan **Pydantic**
- ✅ Dokumentasi otomatis dengan **Swagger UI** (`/docs`)
- ✅ Menggunakan **Firebase Firestore** sebagai database

## 🛠 Teknologi yang Digunakan
- **FastAPI**: Framework web Python yang ringan dan cepat
- **Firebase Firestore**: Database NoSQL dari Google
- **Pydantic**: Validasi data berbasis model
- **Uvicorn**: Server ASGI untuk menjalankan FastAPI

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/YuuchiXD/fastapi-firestore-api.git
cd fastapi-firestore-api
```

### 2. Buat Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 3. Konfigurasi Firestore
- Download **serviceAccountKey.json** dari Firebase Console
- Simpan di root folder proyek (pastikan file ini tidak diupload ke GitHub)

### 4. Jalankan Server
```bash
uvicorn main:app --reload
```
API akan berjalan di **http://127.0.0.1:8000**

## 🔥 Dokumentasi API
Swagger UI tersedia di:
```
http://127.0.0.1:8000/docs
```

## 📌 Contoh Request
### **1. Tambah User**
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "age": 25}'
```

### **2. Ambil Data User**
```bash
curl -X GET "http://127.0.0.1:8000/users/{user_id}"
```

Gantilah `{user_id}` dengan ID user yang valid dari Firestore.

## 📜 Lisensi
Proyek ini menggunakan lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan!

---
✨ Dibuat dengan ❤️ oleh [YuuchiXD] ✨