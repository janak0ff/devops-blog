  * **Rule 4: Custom TCP (Port 8000/8001):** We'll use this temporarily for testing the Django development server or Docker.
      * Type: `Custom TCP`
      * Port range: `8000` (for virtual env testing) and `8001` (for Docker testing).
      * Source type: `Anywhere`




### 2\. Prepare Your Local Project for Deployment

Before installing dependencies on EC2, ensure your local project has a `requirements.txt` file.

1.  **Generate `requirements.txt` (on your LOCAL machine):**
      * Navigate to your project's root on your local machine.
      * If you have a local virtual environment, activate it.
      * Run:
        ```bash
        pip freeze > requirements.txt
        ```
      * **Add `gunicorn` to `requirements.txt`:** Open the file and add `gunicorn` on a new line. Save it.
      * **Commit and Push:** Make sure `requirements.txt` (with `gunicorn`) is committed and pushed to your GitHub repository.
        ```bash
        git add requirements.txt
        git commit -m "Add requirements.txt including gunicorn"
        git push origin main # or 'develop' if that's your branch
        ```
2.  **Pull Changes on EC2:**
    Back on your **EC2 instance's terminal** (in `~/django-todo`):
    ```bash
    git pull origin main # or 'develop'
    ```
    This ensures your EC2 instance has the updated `requirements.txt`.
