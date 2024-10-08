from pymongo import MongoClient, InsertOne
from faker import Faker
from random import randint, uniform, choice, sample
from tqdm import tqdm
import json

# Initialize Faker
fake = Faker()

# MongoDB Atlas connection string (replace with your actual connection string)
MONGODB_URI = "mongodb+srv://admin:admin@instabase.svzbc.mongodb.net/?retryWrites=true&w=majority&appName=Instabase"

# Initialize MongoDB client
client = MongoClient(MONGODB_URI)

# Configuration
TOTAL_ENTRIES = 10000
BATCH_SIZE = 500  # Number of documents to insert per batch

# Define databases and their respective collections
databases = {
    "ecommerce_db": {
        "products": "Product information including name, category, price, and stock.",
        "customers": "Customer profiles with personal and contact information.",
        "orders": "Order records linking customers to products with order details."
    },
    "social_db": {
        "users": "User profiles with authentication and personal information.",
        "posts": "User-generated posts containing content and metadata.",
        "comments": "Comments made by users on posts."
    },
    "healthcare_db": {
        "patients": "Patient records with medical and personal information.",
        "appointments": "Appointment schedules linking patients to healthcare providers.",
        "medical_records": "Detailed medical history and records of patients."
    },
    "library_db": {
        "books": "Book details including title, author, genre, and availability.",
        "authors": "Author profiles with biographical information.",
        "loans": "Book loan records linking books to borrowers with loan dates."
    },
    "education_db": {
        "students": "Student profiles with academic and personal information.",
        "courses": "Courses offered including syllabus and instructor details.",
        "enrollments": "Enrollment records linking students to courses."
    }
}

# Function to generate a product document
def generate_product():
    categories = ["Electronics", "Books", "Clothing", "Home & Kitchen", "Sports", "Toys", "Beauty", "Automotive"]
    product = {
        "product_name": fake.catch_phrase(),
        "category": choice(categories),
        "price": round(uniform(5.0, 500.0), 2),
        "stock": randint(0, 1000),
        "description": fake.text(max_nb_chars=200),
        "sku": fake.unique.ean(length=13)
    }
    return product

# Function to generate a customer document
def generate_customer():
    customer = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "phone_number": fake.phone_number(),
        "address": {
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip_code": fake.zipcode(),
            "country": fake.country()
        },
        "registration_date": fake.date_between(start_date='-5y', end_date='today').isoformat()
    }
    return customer

# Function to generate an order document
def generate_order(customer_ids, product_ids):
    order = {
        "customer_id": choice(customer_ids),
        "product_id": choice(product_ids),
        "quantity": randint(1, 5),
        "total_price": 0,  # To be updated after fetching product price
        "order_date": fake.date_between(start_date='-2y', end_date='today').isoformat(),
        "status": choice(["Pending", "Shipped", "Delivered", "Cancelled"])
    }
    return order

# Function to generate a user document
def generate_user():
    user = {
        "username": fake.unique.user_name(),
        "email": fake.unique.email(),
        "password_hash": fake.password(length=12),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "signup_date": fake.date_between(start_date='-3y', end_date='today').isoformat()
    }
    return user

# Function to generate a post document
def generate_post(user_ids):
    post = {
        "user_id": choice(user_ids),
        "content": fake.text(max_nb_chars=280),
        "created_at": fake.date_time_between(start_date='-1y', end_date='now').isoformat(),
        "likes": randint(0, 1000),
        "shares": randint(0, 500)
    }
    return post

# Function to generate a comment document
def generate_comment(post_ids, user_ids):
    comment = {
        "post_id": choice(post_ids),
        "user_id": choice(user_ids),
        "content": fake.text(max_nb_chars=200),
        "created_at": fake.date_time_between(start_date='-1y', end_date='now').isoformat(),
        "likes": randint(0, 500)
    }
    return comment

# Function to generate a patient document
def generate_patient():
    patient = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "date_of_birth": fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=100).isoformat(),
        "gender": choice(["Male", "Female", "Other"]),
        "email": fake.unique.email(),
        "phone_number": fake.phone_number(),
        "address": {
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip_code": fake.zipcode(),
            "country": fake.country()
        },
        "registration_date": fake.date_between(start_date='-5y', end_date='today').isoformat()
    }
    return patient

# Function to generate an appointment document
def generate_appointment(patient_ids, provider_ids):
    appointment = {
        "patient_id": choice(patient_ids),
        "provider_id": choice(provider_ids),
        "appointment_date": fake.date_time_between(start_date='-1y', end_date='+1y').isoformat(),
        "reason": fake.sentence(nb_words=6),
        "status": choice(["Scheduled", "Completed", "Cancelled", "No-show"])
    }
    return appointment

# Function to generate a medical record document
def generate_medical_record(patient_ids, doctor_ids):
    medical_record = {
        "patient_id": choice(patient_ids),
        "doctor_id": choice(doctor_ids),
        "diagnosis": fake.word(ext_word_list=["Diabetes", "Hypertension", "Asthma", "Flu", "Covid-19", "Migraine"]),
        "treatment": fake.sentence(nb_words=10),
        "prescriptions": [fake.word() for _ in range(randint(1, 3))],
        "record_date": fake.date_between(start_date='-3y', end_date='today').isoformat()
    }
    return medical_record

# Function to generate a book document
def generate_book(author_ids):
    genres = ["Fiction", "Non-Fiction", "Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", "Biography"]
    book = {
        "title": fake.sentence(nb_words=4).rstrip('.'),
        "author_id": choice(author_ids),
        "genre": choice(genres),
        "published_year": randint(1950, 2023),
        "isbn": fake.unique.isbn13(),
        "pages": randint(100, 1000),
        "available_copies": randint(0, 20)
    }
    return book

# Function to generate an author document
def generate_author():
    author = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "date_of_birth": fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=100).isoformat(),
        "nationality": fake.country(),
        "biography": fake.text(max_nb_chars=500)
    }
    return author

# Function to generate a loan document
def generate_loan(book_ids, borrower_ids):
    loan = {
        "book_id": choice(book_ids),
        "borrower_id": choice(borrower_ids),
        "loan_date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
        "return_date": fake.date_between(start_date='today', end_date='+1y').isoformat(),
        "status": choice(["On Loan", "Returned", "Overdue"])
    }
    return loan

# Function to generate a student document
def generate_student():
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "student_id": fake.unique.bothify(text='???-#####'),
        "email": fake.unique.email(),
        "phone_number": fake.phone_number(),
        "enrollment_date": fake.date_between(start_date='-5y', end_date='today').isoformat(),
        "major": choice(["Computer Science", "Business", "Engineering", "Arts", "Biology", "Mathematics"])
    }
    return student

# Function to generate a course document
def generate_course():
    departments = ["Computer Science", "Business", "Engineering", "Arts", "Biology", "Mathematics"]
    course = {
        "course_name": fake.sentence(nb_words=3).rstrip('.'),
        "course_code": fake.unique.bothify(text='???-###'),
        "department": choice(departments),
        "credits": randint(1, 5),
        "instructor": fake.name(),
        "description": fake.text(max_nb_chars=300)
    }
    return course

# Function to generate an enrollment document
def generate_enrollment(student_ids, course_ids):
    enrollment = {
        "student_id": choice(student_ids),
        "course_id": choice(course_ids),
        "enrollment_date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
        "grade": choice(["A", "B", "C", "D", "F", "Incomplete"]),
        "status": choice(["Enrolled", "Completed", "Dropped"])
    }
    return enrollment

# Mapping of generation functions per collection
generation_functions = {
    "ecommerce_db": {
        "products": generate_product,
        "customers": generate_customer,
        "orders": None  # Special handling due to dependencies
    },
    "social_db": {
        "users": generate_user,
        "posts": None,     # Special handling due to dependencies
        "comments": None   # Special handling due to dependencies
    },
    "healthcare_db": {
        "patients": generate_patient,
        "appointments": None,      # Special handling due to dependencies
        "medical_records": None    # Special handling due to dependencies
    },
    "library_db": {
        "books": None,    # Special handling due to dependencies
        "authors": generate_author,
        "loans": None      # Special handling due to dependencies
    },
    "education_db": {
        "students": generate_student,
        "courses": generate_course,
        "enrollments": None  # Special handling due to dependencies
    }
}

# Pre-insert some collections to establish dependencies
def pre_insert_dependencies():
    # Ecommerce: Insert products and customers first to reference in orders
    ecommerce_db = client["ecommerce_db"]
    products = ecommerce_db["products"]
    customers = ecommerce_db["customers"]
    # Insert 100 products
    product_docs = [generate_product() for _ in range(100)]
    products.insert_many(product_docs)
    # Insert 100 customers
    customer_docs = [generate_customer() for _ in range(100)]
    customers.insert_many(customer_docs)
    
    # Social: Insert users first to reference in posts and comments
    social_db = client["social_db"]
    users = social_db["users"]
    # Insert 200 users
    user_docs = [generate_user() for _ in range(200)]
    users.insert_many(user_docs)
    
    # Healthcare: Insert patients and providers (doctors) first
    healthcare_db = client["healthcare_db"]
    patients = healthcare_db["patients"]
    # Assuming providers are doctors, we'll create a separate collection or use a placeholder
    # For simplicity, let's treat providers as doctors and insert them into patients as a separate collection
    providers = healthcare_db["providers"]
    # Insert 50 providers (doctors)
    provider_docs = [{
        "name": fake.name(),
        "specialization": choice(["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "General Medicine"]),
        "license_number": fake.unique.bothify(text='DOC-#####'),
        "email": fake.unique.email(),
        "phone_number": fake.phone_number()
    } for _ in range(50)]
    providers.insert_many(provider_docs)
    
    # Insert 200 patients
    patient_docs = [generate_patient() for _ in range(200)]
    patients.insert_many(patient_docs)
    
    # Library: Insert authors first to reference in books
    library_db = client["library_db"]
    authors = library_db["authors"]
    # Insert 100 authors
    author_docs = [generate_author() for _ in range(100)]
    authors.insert_many(author_docs)
    
    # Insert 500 books
    books = library_db["books"]
    author_ids = list(authors.find({}, {"_id": 1}))
    author_ids = [str(a["_id"]) for a in author_ids]
    book_docs = [{
        "title": fake.sentence(nb_words=4).rstrip('.'),
        "author_id": choice(author_ids),
        "genre": choice(["Fiction", "Non-Fiction", "Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", "Biography"]),
        "published_year": randint(1950, 2023),
        "isbn": fake.unique.isbn13(),
        "pages": randint(100, 1000),
        "available_copies": randint(0, 20)
    } for _ in range(500)]
    books.insert_many(book_docs)
    
    # Education: Insert students and courses first to reference in enrollments
    education_db = client["education_db"]
    students = education_db["students"]
    courses = education_db["courses"]
    # Insert 300 students
    student_docs = [generate_student() for _ in range(300)]
    students.insert_many(student_docs)
    # Insert 50 courses
    course_docs = [generate_course() for _ in range(50)]
    courses.insert_many(course_docs)

# Main function to generate and insert documents
def generate_and_insert_documents():
    # Pre-insert dependencies
    pre_insert_dependencies()
    
    # Fetch IDs for dependencies
    # Ecommerce
    ecommerce_db = client["ecommerce_db"]
    products = ecommerce_db["products"]
    customers = ecommerce_db["customers"]
    product_ids = list(products.find({}, {"_id": 1}))
    product_ids = [str(p["_id"]) for p in product_ids]
    customer_ids = list(customers.find({}, {"_id": 1}))
    customer_ids = [str(c["_id"]) for c in customer_ids]
    
    # Social
    social_db = client["social_db"]
    users = social_db["users"]
    user_ids = list(users.find({}, {"_id": 1}))
    user_ids = [str(u["_id"]) for u in user_ids]
    posts = social_db["posts"]
    # Insert 1000 posts
    post_docs = [generate_post(user_ids) for _ in range(1000)]
    posts.insert_many(post_docs)
    post_ids = list(posts.find({}, {"_id": 1}))
    post_ids = [str(p["_id"]) for p in post_ids]
    
    # Healthcare
    healthcare_db = client["healthcare_db"]
    patients = healthcare_db["patients"]
    providers = healthcare_db["providers"]
    patient_ids = list(patients.find({}, {"_id": 1}))
    patient_ids = [str(p["_id"]) for p in patient_ids]
    provider_ids = list(providers.find({}, {"_id": 1}))
    provider_ids = [str(p["_id"]) for p in provider_ids]
    appointments = healthcare_db["appointments"]
    # Insert 500 appointments
    appointment_docs = [generate_appointment(patient_ids, provider_ids) for _ in range(500)]
    appointments.insert_many(appointment_docs)
    appointment_ids = list(appointments.find({}, {"_id": 1}))
    appointment_ids = [str(a["_id"]) for a in appointment_ids]
    
    # Medical Records
    medical_records = healthcare_db["medical_records"]
    doctor_ids = provider_ids  # Assuming providers are doctors
    # Insert 800 medical records
    medical_record_docs = [generate_medical_record(patient_ids, doctor_ids) for _ in range(800)]
    medical_records.insert_many(medical_record_docs)
    
    # Library
    library_db = client["library_db"]
    books = library_db["books"]
    authors = library_db["authors"]
    book_ids = list(books.find({}, {"_id": 1}))
    book_ids = [str(b["_id"]) for b in book_ids]
    borrowers = library_db["loans"]  # Assuming borrowers are part of loans
    # Insert 1000 loans
    borrower_ids = [fake.unique.bothify(text='BORR-#####') for _ in range(1000)]  # Simulated borrower IDs
    loan_docs = [{
        "book_id": choice(book_ids),
        "borrower_id": borrower_ids[i],
        "loan_date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
        "return_date": fake.date_between(start_date='today', end_date='+1y').isoformat(),
        "status": choice(["On Loan", "Returned", "Overdue"])
    } for i in range(1000)]
    loans = library_db["loans"]
    loans.insert_many(loan_docs)
    
    # Education
    education_db = client["education_db"]
    students = education_db["students"]
    courses = education_db["courses"]
    enrollments = education_db["enrollments"]
    student_ids = list(students.find({}, {"_id": 1}))
    student_ids = [str(s["_id"]) for s in student_ids]
    course_ids = list(courses.find({}, {"_id": 1}))
    course_ids = [str(c["_id"]) for c in course_ids]
    # Insert 2000 enrollments
    enrollment_docs = [generate_enrollment(student_ids, course_ids) for _ in range(2000)]
    enrollments.insert_many(enrollment_docs)
    
    # Orders (E-commerce)
    orders = ecommerce_db["orders"]
    # Insert 1000 orders
    order_docs = [generate_order(customer_ids, product_ids) for _ in range(1000)]
    # Update total_price based on product price
    for order in order_docs:
        product = products.find_one({"_id": order["product_id"]})
        if product:
            order["total_price"] = round(product.get("price", 0) * order["quantity"], 2)
    orders.insert_many(order_docs)
    
    # Posts and Comments (Social)
    comments = social_db["comments"]
    # Insert 3000 comments
    comment_docs = [generate_comment(post_ids, user_ids) for _ in range(3000)]
    comments.insert_many(comment_docs)
    
    # Final Counts
    print("Data generation and insertion completed successfully.")

if __name__ == "__main__":
    generate_and_insert_documents()
