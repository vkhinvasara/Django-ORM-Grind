# Assignment: Library Management System API

Your task is to design and implement a RESTful API for a simple library management system using Django and Django REST Framework. The system should have the following features:

## Features

### Book Management
The API should allow the library to manage their books. This includes operations like adding a new book, updating a book's details, deleting a book, and viewing details of a book. Each book should have the following details:

- Title
- Author
- Published Date
- ISBN number
- Pages
- Cover image (URL)

### User Management
The API should allow the library to manage their users. This includes operations like adding a new user, updating a user's details, deleting a user, and viewing details of a user. Each user should have the following details:

- Name
- Email
- Date of Birth
- Membership Status (Active/Inactive)

### Borrowing and Returning Books
The API should allow a user to borrow a book from the library. When a book is borrowed, the system should keep track of which user has borrowed the book and when it is due to be returned. The system should also handle the returning of books.

### Overdue Books
The API should provide a way to view all books that are currently overdue.

### Search
The API should provide a way to search for a book by its title or author.

### Unit Tests
Write unit tests for your models and views to ensure that they are working as expected.

Remember to use Django's ORM for database operations. You can use SQLite for the database as it's easy to set up and use.