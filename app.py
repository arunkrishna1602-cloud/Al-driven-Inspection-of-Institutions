from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import json
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from io import BytesIO

app = Flask(__name__)

# Store inspection data
inspections_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/save-inspection', methods=['POST'])
def save_inspection():
    try:
        data = request.json
        inspection_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        inspections_data[inspection_id] = data
        
        # Save to JSON file as backup
        with open(f'inspections_{inspection_id}.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        return jsonify({'success': True, 'inspection_id': inspection_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/download-pdf', methods=['POST'])
def download_pdf():
    try:
        data = request.json
        
        # Create PDF
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
        
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        title_style = styles['Heading1']
        title_style.fontSize = 16
        title_style.alignment = TA_CENTER
        
        story.append(Paragraph("SCHOOL INSPECTION REPORT", title_style))
        story.append(Spacer(1, 0.2*inch))
        
        # School Info
        school_info = f"""
        <b>School Name:</b> {data.get('schoolName', 'N/A')}<br/>
        <b>Inspection Date:</b> {data.get('inspectionDate', 'N/A')}<br/>
        <b>Inspector:</b> {data.get('inspector', 'N/A')}<br/>
        <b>Report Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>
        """
        story.append(Paragraph(school_info, styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Results table
        results = data.get('results', {})
        table_data = [['Category', 'Item', 'Rating', 'Notes']]
        
        for category, items in results.items():
            for item_name, item_data in items.items():
                rating = item_data.get('rating', 'N/A')
                notes = item_data.get('notes', '')
                table_data.append([category, item_name, str(rating), notes[:30]])
        
        results_table = Table(table_data, colWidths=[1.5*inch, 2*inch, 1*inch, 1.5*inch])
        results_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
        ]))
        story.append(results_table)
        story.append(Spacer(1, 0.2*inch))
        
        # Overall Score
        overall_score = data.get('overallScore', 0)
        story.append(Paragraph(f"<b>Overall Score:</b> {overall_score}%", styles['Normal']))
        
        doc.build(story)
        pdf_buffer.seek(0)
        
        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"School_Inspection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/download-json', methods=['POST'])
def download_json():
    try:
        data = request.json
        json_buffer = BytesIO()
        json_buffer.write(json.dumps(data, indent=2).encode())
        json_buffer.seek(0)
        
        return send_file(
            json_buffer,
            mimetype='application/json',
            as_attachment=True,
            download_name=f"School_Inspection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
