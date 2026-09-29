from flask import Flask, abort
from flask_login import current_user, login_required

app = Flask(__name__)


@app.get("/invoices/<int:invoice_id>")
@login_required
def get_invoice(invoice_id):
    invoice = db.session.get(Invoice, invoice_id)
    if invoice is None:
        abort(404)
    return {"id": invoice.id, "owner_id": invoice.owner_id, "total": invoice.total}
