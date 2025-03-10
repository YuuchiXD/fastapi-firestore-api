from google.cloud import firestore

# Pastikan file serviceAccountKey.json ada di direktori yang benar
db = firestore.Client.from_service_account_json("serviceAccountKey.json")

try:
    # Tes menulis ke Firestore
    test_ref = db.collection("test").document("ping")
    test_ref.set({"status": "connected"})
    
    # Tes membaca dari Firestore
    doc = test_ref.get()
    if doc.exists:
        print("Firestore Connected! Data:", doc.to_dict())
    else:
        print("Firestore connection failed!")
except Exception as e:
    print("Firestore Connection Error:", e)
