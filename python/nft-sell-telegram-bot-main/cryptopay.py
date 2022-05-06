import requests


class CryptoPay(object):
    def __init__(self, user_id, parameters) -> None:
        self.token = parameters['token']
        self.api_url = parameters['api_url']
        self.user_id = user_id
        self.headers = {
            "Crypto-Pay-API-Token": self.token
        }
        pass

    def get_me(self):
        getMe_url = f"{self.api_url}api/getMe"
        try:
            app_info = requests.get(getMe_url, headers=self.headers).json()
            return app_info
        except:
            return False

    def create_invoice(self, amount, paid_btn_name, paid_btn_url, asset='TON', description=None,
                       hidden_message='Оплата прошла успешно!',
                       expires_in=86400):
        payload = self.user_id
        invoice_url = f"{self.api_url}api/createInvoice"
        params = {
            "asset": asset,
            "amount": amount,
            "payload": payload,
            "hidden_message": hidden_message,
            "expires_in": expires_in,
            "paid_btn_name": paid_btn_name,
            "paid_btn_url": paid_btn_url
        }
        if description:
            params["description"] = description
        try:
            invoice_info = requests.get(invoice_url, headers=self.headers, params=params).json()
            return invoice_info
        except:
            return False

    def get_all_invoices(self):
        invoices_url = f"{self.api_url}api/getInvoices"
        invoice_info = requests.get(invoices_url, headers=self.headers).json()
        return invoice_info
        return False

    def get_invoice(self, invoice_id):
        invoices_list = self.get_all_invoices()
        if invoices_list:
            return [invoice for invoice in invoices_list["result"]["items"] if invoice["invoice_id"] == invoice_id]
        else:
            return False
