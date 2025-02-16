# Telegram Gifts Catalogue

> In addition to this README, there are also README files available in other languages:
>
> - [Russian](RU.README.md)
> - [Ukrainian](UK.README.md)
> - [Uzbek](UZ.README.md)
>
> These files contain the same information as this README but translated into their respective languages.

This project consists of two main parts:
1. A catalogue of gifts that Telegram bots can send to users, generated and updated regularly using a Python script and deployed to GitHub Pages.
2. A script to download all available gifts in Telegram using aiogram.

---

## Features

- Displays a list of gifts with their IDs, prices, and other details.
- Supports multiple languages: English, Russian, Ukrainian, and Uzbek.
- Automatically updates the catalogue with the latest data.
- Responsive design for better user experience on different devices.
- Downloads all available gifts from Telegram.
- Saves gift data and images locally.

---

## Project Structure

```plaintext
telegram-gifts-catalogue/ 
├── .github/ 
│ └── workflows/ 
│ │ └── generate.yml # GitHub Actions workflow for generating and deploying the catalogue 
├── src/ 
│ └── collector.py # Python script for downloading the gifts
├── web/ 
│ ├── index.html # English version of the catalogue 
│ ├── ru.index.html # Russian version of the catalogue 
│ ├── uk.index.html # Ukrainian version of the catalogue 
│ ├── uz.index.html # Uzbek version of the catalogue 
│ └── style.css # Stylesheet for the catalogue 
├── .gitignore # Git ignore file
├── pyproject.toml # Project configuration file
└── README.md # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Git
- GitHub account with a repository for deploying the catalogue

### Installation

#### Local Setup for Downloading All Gifts

1. Clone the repository:
    ```sh
    git clone https://github.com/MasterGroosha/telegram-gifts-catalogue.git
    cd telegram-gifts-catalogue
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create `.env` file in the root directory and add your configuration:
    ```sh
    BOT_TOKEN=your_bot_token_here
    OUTPUT_DIR=/path/to/output/directory
    ```

5. Run the script to download all available gifts:
    ```sh
    python src/collector.py
    ```

#### Setup for Self-Deployment on GitHub Pages

1. Fork the repository to your GitHub account.

2. Go to the repository settings and add a secret named `BOT_TOKEN`.

3. Enable GitHub Actions in your repository.

4. You will see a workflow named "Generate and Deploy" (disabled). Click on it and activate it.

5. Manually trigger the workflow to generate the catalogue.

6. Go to the repository settings, navigate to Pages, and enable it for the `web` branch. Use `/root` as the path (default).

7. Visit your site or configured domain to view the catalogue.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.