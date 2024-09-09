# Task 1: Customer Service Ticket Tracker:
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
#Open a new service ticket
def open_ticket(ticket_id, customer_name, issue_description):
    """Open a new service ticket."""
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        print(f"New ticket opened: {ticket_id}")

# Update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    """Update the status of an existing ticket."""
    if ticket_id in service_tickets:
        if new_status in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = new_status
            print(f"Ticket ID {ticket_id} status updated to {new_status}.")
        else:
            print("Invalid status. Use 'open' or 'closed'.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

# Display all tickets or filter by status.
def display_tickets(status=None):
    """Display tickets. Filter by status if provided."""
    print("\nTickets:")
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

# Sample usage
if __name__ == "__main__":
    open_ticket("Ticket003", "Charlie", "Network issue")
    update_ticket_status("Ticket001", "closed")
    display_tickets()
    display_tickets("open")
