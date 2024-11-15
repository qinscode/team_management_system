# Team Member Management Application

This is a Django-based web application for managing team members. It serves as the example application for the CI/CD pipeline lab.

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   # On Unix/macOS
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application:
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

- `team_site/`: Main project directory
  - `settings.py`: Project settings
  - `urls.py`: Main URL configuration

- `members/`: Main application directory
  - `models.py`: Contains TeamMember model
  - `views.py`: Contains view logic
  - `urls.py`: URL configurations
  - `admin.py`: Admin interface setup
  - `tests.py`: Unit tests
  - `forms.py`: Form definitions

- `templates/`: HTML templates
  - `base.html`: Base template
  - `members/`: Member-specific templates
    - `member_list.html`: Homepage with member list
    - `member_detail.html`: Member details page
    - `member_form.html`: Create/Edit member form
    - `about.html`: About page

- `static/`: Static files
  - `css/`: CSS files
  - `js/`: JavaScript files

## Features

- List all team members
- View detailed information about each member
- Add new team members
- Edit existing team member information
- About page with version information
- Responsive design using Bootstrap 5
- Admin interface for data management

## Running Tests

Run the tests using:

## Database Setup

1. Set up PostgreSQL on EC2:
   - Follow instructions in `docs/postgres_setup.md`

2. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update database credentials in `.env`

3. Reset migrations if needed:
   ```bash
   # Remove old migrations (keep __init__.py)
   rm members/migrations/0*.py
   
   # Remove database tables
   psql -h your_ec2_instance_ip -U your_db_user -d team_management
   DROP TABLE IF EXISTS members_teammember CASCADE;
   DROP TABLE IF EXISTS django_migrations CASCADE;
   \q
   
   # Create new migration
   python manage.py makemigrations
   
   # Apply migration
   python manage.py migrate
   ```