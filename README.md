# **Code to use polisen.se API**

Get significant events (500 lastest) from polisen.se
No need for a API key!

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## **Table of Contents**

1. [About the Project](#about-the-project)
2. [Getting Started](#getting-started)
3. [Usage](#usage)


---

## **About the Project**
Get all events from polisen.se 
The last 500 events are available. Older can can be requested from poli

Following endpoints are available:
- Time of event 
- Location of the event
- Type of event
Full API description available at: https://polisen.se/om-polisen/om-webbplatsen/oppna-data/api-over-polisens-handelser/

---

## **Getting Started**

Follow these instructions to get a copy of the project up and running.

### **Prerequisites**

You will need:
- Python 3.10 or later
- `pip` to manage Python packages

### **Installation**

To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/alphagreen84/Polisens_api.git

# Navigate to the project directory
cd Polisens_api-main

# Install dependencies
pip install -r requirements.txt

### **Usage**
```


## Usage
Adjust endpoint details in the polisen_api.py depending on what data you want.

To run:
python polisen_api.py

Result:
Returns a list of events with key/values.
