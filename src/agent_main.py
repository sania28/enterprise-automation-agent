from email_handler import process_email
from invoice_generator import create_invoice
from scheduler_agent import schedule_meeting
from summary_report import generate_daily_summary

def run_agent():
    print("Enterprise Automation Agent Running...")

    # Example actions
    process_email("data/sample_customers.csv")
    create_invoice("data/sample_invoices.csv")
    schedule_meeting("Tomorrow 3 PM")
    generate_daily_summary()

if __name__ == "__main__":
    run_agent()
