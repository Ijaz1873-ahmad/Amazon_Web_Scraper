# Amazon Product Scraper

This project scrapes product data from Amazon based on given search queries and displays the results in a React frontend.

---

## Backend (Python)

- Scrapes product title, price, reviews, image, and timestamp.
- Uses Selenium + BeautifulSoup.
- Scrapes first 20 pages for each of 10 queries.
- Results saved as separate JSON files per query.

### Run Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

```
## Frontend
``` bash
cd frontend
npm install
npm start
```
