from agent_core import EnterpriseAgent
from utils import load_email_data, load_tasks

def main():
    print("\n🚀 Enterprise Automation Agent Started...\n")

    agent = EnterpriseAgent()

    # Load sample tasks
    emails = load_email_data("data/sample_emails.csv")
    tasks = load_tasks("data/tasks.json")

    print("📩 Processing Emails...")
    for email in emails:
        reply = agent.handle_email(email)
        print("\n--- Reply Generated ---")
        print(reply)

    print("\n📝 Processing Task List...")
    for task in tasks:
        output = agent.execute_task(task)
        print("\n--- Task Output ---")
        print(output)

    print("\n🎉 Workflow Completed!")

if __name__ == "__main__":
    main()
