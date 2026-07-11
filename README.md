# 🏫 AI School Inspection Form

A simple, easy-to-use web application for conducting comprehensive school inspections using Python Flask and HTML.

## Features

✅ **6 Inspection Categories**
- Infrastructure & Facilities
- Cleanliness & Hygiene
- Safety & Security
- Academic Standards
- Staff & Management
- Student Welfare

✅ **Easy-to-Use Interface**
- Clean, modern design
- 1-5 rating scale for each item
- Notes section for observations
- Real-time score calculation

✅ **Download Options**
- Download inspection data as PDF
- Download as JSON for further analysis

✅ **Real-Time Reports**
- Overall percentage score
- Status indicators (Good/Fair/Poor)
- Category-wise breakdown

## Requirements

- Python 3.7+
- Flask
- ReportLab

## Installation & Setup

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 3: Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

## How to Use

1. **Enter School Details**
   - School Name (required)
   - Inspection Date (required)
   - Inspector Name
   - District/Region

2. **Complete the Inspection**
   - Click on each category to expand
   - Rate each item (1-5 scale)
   - Add notes/observations if needed

3. **View Summary**
   - Overall score updates automatically
   - See category-wise breakdown
   - Review current status

4. **Download Report**
   - Click "Download PDF" to get a professional report
   - Or "Reset" to start a new inspection

## File Structure

```
school-inspection/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML interface
└── README.md             # This file
```

## Rating Scale

- **1** - Poor (Major improvements needed)
- **2** - Fair (Some improvements needed)
- **3** - Satisfactory (Adequate, with minor improvements)
- **4** - Good (Well-maintained)
- **5** - Excellent (Outstanding)

## Status Indicators

- **✓ Good** - Score 75% and above
- **⚠ Fair** - Score 50-74%
- **✗ Poor** - Score below 50%

## Tips

- Set today's date automatically appears in the date field
- Expand categories by clicking on them
- Add specific observations in the notes section
- Download PDF for official records

## Troubleshooting

**Port Already in Use?**
```bash
python app.py --port 5001
```

**Module Not Found?**
```bash
pip install -r requirements.txt
```

**Flask Not Found?**
```bash
pip install Flask==2.3.3
```

## Data Storage

- Inspection data is saved locally as JSON files
- PDFs are generated on-the-fly when downloaded
- No data is sent to external servers

## Contact & Support

For issues or suggestions, please refer to the documentation.

---

**Version:** 1.0  
**Last Updated:** 2024  
**License:** Free to use and modify
