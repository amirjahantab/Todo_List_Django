# ToDo App using Django

This is a simple ToDo application built using Django, allowing users to create lists and add items to those lists.

## Features

- **TodoList**: Model representing a list.
- **TodoItem**: Model representing items within a list.
- **CRUD Operations**: Users can Create, Read, Update, and Delete both lists and items.
- **User Authentication**: Utilizes Django's built-in authentication for user management.

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your_username/todo-django-app.git
    cd todo-django-app
    ```

2. **Install Dependencies:**

    Ensure you have Python and Django installed. Create a virtual environment and install the dependencies:

    ```bash
    pip install django
    ```

3. **Database Setup:**

    Run the migrations to create the database and apply the models:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the Development Server:**

    Start the Django server:

    ```bash
    python manage.py runserver
    ```

    The app should be accessible at `http://127.0.0.1:8000/`.

## Usage

- **Lists View**: Accessible at `/lists/`, displays all the created lists.
- **List Detail View**: Accessible at `/lists/<list_id>`, shows the items within a specific list.
- **Add List**: Users can add new lists.
- **Add Item**: Within each list, users can add new items.
- **Delete List**: Option available to delete a list.

## File Structure

- **models.py**: Contains the database models for TodoList and TodoItem.
- **forms.py**: Defines forms for creating and updating lists and items.
- **views.py**: Handles the logic and rendering for different views in the app.

## Contributing

Feel free to contribute by forking the repository, making changes, and creating pull requests. For major changes, please open an issue first to discuss the changes you would like to make.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
