from client import AutomatedCaseStudyRoiEvidenceSynthesizerClient

def main():
    client = AutomatedCaseStudyRoiEvidenceSynthesizerClient()
    res = client.synthesize_enterprise_case_study('HEALTHCARE_TELEMEDICINE', 'Patient intake bottleneck', {'intake_speedup_x': 4.5, 'cost_savings_pct': 40.0})
    print('Case Study Synthesizer: ' + res['case_study_id'] + ' (' + res['customer_vertical'] + ')')
    print('Framework: ' + res['storytelling_framework'] + ' | ROI Validated: ' + str(res['quantified_roi_validated']))
    print('Quotes: ' + str(res['executive_quotes_synthesized_count']) + ' | PDF: ' + res['case_study_pdf_url'])

if __name__ == '__main__':
    main()
