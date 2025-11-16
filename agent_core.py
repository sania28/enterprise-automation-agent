import json

class EnterpriseAgent:

    def __init__(self):
        print("Agent Initialized ✓")

    # ---------------------
    # EMAIL HANDLER
    # ---------------------
    def handle_email(self, email):
        subject = email.get("subject", "")
        body = email.get("body", "")

        if "invoice" in subject.lower():
            return self._generate_invoice_reply(email)

        elif "meeting" in subject.lower():
            return self._generate_meeting_reply(email)

        else:
            return self._generate_generic_reply(email)

    def _generate_invoice_reply(self, email):
        return f"""
        Subject: Invoice Request Received

        Hello,

        We have received your invoice request regarding:
        "{email.get('subject')}"

        Our system is generating your invoice and you will receive it shortly.

        Regards,
        Enterprise Automation Agent
        """

    def _generate_meeting_reply(self, email):
        return f"""
        Subject: Meeting Scheduled

        Hello,

        Your meeting request has been scheduled. We will send you a calendar invite soon.

        Regards,
        Automation Agent
        """

    def _generate_generic_reply(self, email):
        return f"""
        Subject: Response to your message

        Hello,

        Thank you for your email. Our system is reviewing your message:
        "{email.get('body')}"

        We will get back to you shortly.

        Regards,
        AI Agent
        """

    # ---------------------
    # TASK EXECUTION
    # ---------------------
    def execute_task(self, task):
        task_type = task.get("type", "")

        if task_type == "summary":
            return self._generate_summary(task)

        if task_type == "report":
            return self._generate_report(task)

        return "Unknown task type!"

    def _generate_summary(self, task):
        text = task.get("text", "")
        return f"📌 Summary Generated:\n{text[:120]}..."

    def _generate_report(self, task):
        data = task.get("data", {})
        report = json.dumps(data, indent=4)
        return f"📊 Report:\n{report}"
