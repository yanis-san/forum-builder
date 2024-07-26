# Forum Builder

Forum Builder is a system designed to create and manage online forums similar to phpBB. The project allows users to create accounts, set up forums, and manage user permissions and interactions within those forums. The frontend of the project has not been implemented yet.

## Features

- **User Management**
  - Registration and login for users.
  - Customizable profiles (profile picture, description, etc.).
  - User rights management (members, moderators, administrators).

- **Topic Management**
  - Create topics within various categories.
  - Search and filter topics by date, popularity, category.
  - Moderation system for topics and messages (delete, edit).

- **Community Interactions**
  - Post messages and respond to topics.
  - Message rating system (like, dislike).

## Prerequisites

- pipenv for dependency management

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yanis-san/forum-builder.git
    cd forum-builder
    ```

2. Create and activate a virtual environment and install dependencies using pipenv:

    ```bash
    pipenv install
    pipenv shell
    ```

## Usage

1. Run the Application:

    Start the application to manage forums, users, and topics. The frontend of the project has not been completed, so you may interact with the system via the command line or through the minimal web interface.

    ```bash
    python manage.py runserver
    ```

2. Access the Application:

    Navigate to [http://localhost:8000](http://localhost:8000) to interact with the application.

## Notes

- The project currently uses SQLite for database management. For production use, consider upgrading to a more robust database system like PostgreSQL or MySQL.


