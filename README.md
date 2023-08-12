# ArtadoBot - Artado Search Crawler

![Artado Search Logo](https://www.artadosearch.com/images/android-chrome-192x192.png)

ArtadoBot is the web crawling component of Artado Search, an open-source search engine project. It is designed to fetch and index web pages for the Artado Search engine. This README provides an overview of ArtadoBot's Development branch, how to set up and run it in both Windows and Linux environments, and how to contribute to its development.

## Features

- **Web Crawling:** ArtadoBot is capable of crawling web pages, fetching their content, and processing metadata.
- **Robots.txt Compliance:** The crawler adheres to the rules set in a website's `robots.txt` file to respect website permissions.
- **Politeness:** ArtadoBot maintains a delay between requests to avoid overloading websites and being respectful to their servers.
- **Configurability:** The crawler can be configured with user-defined settings such as crawl depth and maximum number of pages to crawl.

## Prerequisites

- Python 3.7 or higher

## Setup and Running on Windows

1. **Install Ubuntu WSL:** Follow the [official guide](https://ubuntu.com/wsl/install) to install Ubuntu WSL on your Windows machine.

2. **Clone the Development Branch:** Open the Ubuntu WSL terminal and clone the ArtadoBot repository's Development branch:

   ```bash
   git clone -b Development https://github.com/Artado-Project/artadobot.git
   ```

3. **Run the Crawler:** In the Ubuntu WSL terminal, start the crawler:

   ```bash
   cd artadobot
   python main.py
   ```

## Setup and Running on Linux

1. **Clone the Development Branch:** Open a terminal and clone the ArtadoBot repository's Development branch:

   ```bash
   git clone -b Development https://github.com/Artado-Project/artadobot.git
   ```

2. **Run the Crawler:** In the terminal, start the crawler:

   ```bash
   cd artadobot
   python crawler.py
   ```

## Contributing

ArtadoBot's Development branch is where active development takes place. Contributions are welcome and encouraged. If you'd like to contribute, follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository and create a new branch for your feature or bug fix:

   ```bash
   git clone https://github.com/YourUsername/artadobot.git
   cd artadobot
   git checkout -b feature/your-feature-name
   ```

3. Make your changes, commit them, and push to your forked repository.

4. Create a pull request on the original repository's Development branch, describing your changes and improvements.

## License

ArtadoBot is released under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or need assistance, feel free to reach out to us at [support@artadosearch.com](mailto:support@artadosearch.com).

---

Thank you for your interest in ArtadoBot's Development branch! Your contributions and feedback are invaluable to the ongoing development of our web crawling component for the Artado Search project. Happy crawling and coding!
