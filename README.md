# Telegram Gifts Catalogue

Hello! This project is designed to create a catalogue of Telegram gifts. Below, you'll find all the necessary information to get started.

---

## Project Structure

Let's first understand the structure of the project:

```plaintext
telegram-gifts-catalogue/ 
├── .github/ 
│   └── workflows/ 
│       └── generate.yml # GitHub Actions workflow for generating and deploying the catalogue
├── src/ 
│   └── collector.py # Python script for downloading the gifts
├── web/ 
│   ├── index.html # Catalogue webpage
│   └── style.css # Stylesheet for the catalogue
├── .gitignore # Git ignore file
├── pyproject.toml # Project configuration file
└── README.md # Project documentation
```

---

## Getting Started

### Prerequisites
To start working with this project, ensure you have the following:
- Python 3.12 or higher
- Git
- A GitHub account (for deploying the catalogue)

---

### Local Setup for Downloading All Gifts

If you want to download all available gifts locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/MasterGroosha/telegram-gifts-catalogue.git
   cd telegram-gifts-catalogue
   ```

2. **Create and activate a virtual environment**:
   This isolates the project dependencies from your system.
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**:
   Create a `.env` file in the root directory and add your configuration. You can use any text editor for this step:

   - **On Linux/macOS**: Use `nano`:
     ```sh
     nano .env
     BOT_TOKEN=your_bot_token_here
     OUTPUT_DIR=/path/to/output/directory
     ```
     *(To save changes in nano: press `CTRL + X`, then `Y`, and `Enter`)*

   - **On Windows**: Use `Notepad` or `VS Code`:
     1. Open File Explorer and navigate to the project folder.
     2. Create a new text file named `.env`.
     3. Add the following lines:
        ```
        BOT_TOKEN=your_bot_token_here
        OUTPUT_DIR=C:\path\to\output\directory
        ```
     4. Save the file.

5. **Apply the environment variables**:
   - **On Linux/macOS**:
     ```sh
     export $(grep -v '^#' .env | xargs)
     ```

   - **On Windows**:
     Run the following command in Command Prompt to load the variables from `.env`:
     ```cmd
     for /f "tokens=*" %i in (.env) do set %i
     ```

6. **Run the script**:
   Start the gift downloader:
   ```sh
   python src/collector.py
   ```

Now, all available gifts will be downloaded to the specified directory!

---

### Self-Deployment on GitHub Pages

If you want to deploy the catalogue to GitHub Pages, follow these steps:

1. **Fork the repository**:
   Go to the project page and click "Fork" to copy it to your GitHub account.

2. **Add secrets to your repository**:
   In your fork's settings, add a secret named `BOT_TOKEN` with your bot token.

3. **Enable GitHub Actions**:
   Navigate to the "Actions" section of your repository and activate the "Generate and Deploy" workflow.

4. **Manually trigger the workflow**:
   Once activated, you can manually run the workflow to generate the catalogue.

5. **Set up GitHub Pages**:
   Go to the repository settings, navigate to "Pages," and enable it for the `web` branch. Use `/root` as the path (default).

6. **View your site**:
   Visit your site or configured domain to see the catalogue.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
