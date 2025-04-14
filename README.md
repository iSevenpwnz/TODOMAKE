
A modern task management application built with Django and Bootstrap 5.

## Features

- Create, update, and delete tasks
- Mark tasks as complete/incomplete
- Set deadlines for tasks
- Tag system for task categorization
- Clean and responsive UI with Bootstrap 5
- Modern icons with Font Awesome

## Tech Stack

- Python 3.12
- Django 5.2
- Bootstrap 5
- Crispy Forms with Bootstrap 5 template pack
- Font Awesome 6
- SQLite database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TODOMAKE.git
cd TODOMAKE
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install django crispy-forms crispy-bootstrap5 django-extensions
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
TODOMAKE/
├── manage.py
├── todo_project/        # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tasks/              # Main app
│   ├── models.py       # Task and Tag models
│   ├── views.py        # Class-based views
│   ├── forms.py        # ModelForms for Task and Tag
│   └── urls.py         # URL routing
└── templates/          # HTML templates
    └── tasks/
        ├── base.html
        ├── task_list.html
        └── ...
```

## Features in Detail

### Tasks
- Content field for task description
- Automatic creation timestamp
- Optional deadline
- Completion status tracking
- Multiple tags support

### Tags
- Reusable tag system
- Tag management (CRUD operations)
- Task filtering by tags

### UI Features
- Responsive sidebar navigation
- Card-based task display
- Color-coded task status
- Intuitive task management buttons
- Form validation and feedback
- Modern iconography

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
