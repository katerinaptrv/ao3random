# ao3random
AO3 Random is a simple flask web application that enhances your AO3 (Archive of Our Own) experience by helping indecisive readers or those looking to discover new works without having to scroll through long lists.

Given a URL from AO3 that shows a list of fanfics (such as user bookmarks, a search result, or reading history), this web app will randomly select a fanfic from the list and open it in a new tab. 

## Features

- **Random Fanfic Selection:** Input any valid AO3 search results or bookmarks URL and let the app choose a random story for you.
- **Easy to Use:**  Just paste the URL and click "Go"!
- **Dockerized:**  Easily deploy and run the app using Docker.

## How it Works

The application fetches the provided AO3 URL and analyzes the pagination to determine the total number of pages. Then, it randomly selects a page and retrieves the HTML content.  Finally, it serves this content to the user, effectively opening a random fanfic from the list.

## Getting Started

### Pre-requisites

- **Python 3:**  Make sure you have Python 3 installed on your system. [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **(Optional) Docker:** If you prefer using Docker, have it installed on your system.  [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

### Running without Docker

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ao3random.git
   cd ao3random
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv env 
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask run 
   ```

5. **Access the application:** Open your web browser and navigate to `http://127.0.0.1:5000/`.

### Running with Docker

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ao3random.git
   cd ao3random
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t ao3random .
   ```

3. **Run the Docker container:**
   ```bash
   docker run -p 80:80 ao3random 
   ```

4. **Access the application:** Open your web browser and navigate to `http://localhost`.

## Usage

1. **Paste AO3 URL:** In the input field, paste the URL of the AO3 search results or bookmarks page you want to explore randomly. 
2. **Click "Go":**  The app will process the URL, select a random fanfic, and open it in a new tab.

## Example AO3 URLs

- **Search Results:** `https://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search[query]=your+search+terms`
- **Bookmarks:** `https://archiveofourown.org/users/your-username/bookmarks`

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. 

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details. 

