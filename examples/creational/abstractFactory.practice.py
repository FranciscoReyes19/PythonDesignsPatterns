

class PaypalGateway():
    def process_payment(self, amount):
        print(f"Processing payment of {amount} with Paypal")
        return True
    
class PaypalTransactionLogger():
    def log_transaction(self, message):
        print(f"Processing transaction in Paypal: {message}")


class StripeGateway():
    def process_payment(self, amount):
        print(f"Processing payment of {amount} with Stripe")
        return False

class StripeTransactionLogger():
    def log_transaction(self, message):
        print(f"Processing transaction in Stripe: {message}")
    

class PaypalGatewayFactory():
    def create_payment_gateway(self):
        return PaypalGateway()
    
    def create_transaction_logger(self):
        return PaypalTransactionLogger()
    

class StripeGatewayFactory():
    def create_payment_gateway(self):
        return StripeGateway()
    
    def create_transaction_logger(self):
        return StripeTransactionLogger()
    

class PaymentService:
    def __init__(self, payment_gateway_factory):
        self._payment_gateway = payment_gateway_factory.create_payment_gateway()
        self._transaction_logger = payment_gateway_factory.create_transaction_logger()

    def process_payment(self, amount):
        if self._payment_gateway.process_payment(amount):
            self._transaction_logger.log_transaction(f"Payment of {amount} successful")
        else:
            self._transaction_logger.log_transaction(f"Payment of {amount} fail")    
                                        
                                                     
paypal_gateway_factory = PaypalGatewayFactory()
payment_service = PaymentService(paypal_gateway_factory)

amount =  100.00
payment_service.process_payment(amount)

another_payment_gateway_factory = StripeGatewayFactory()
another_payment_service = PaymentService(another_payment_gateway_factory)

another_payment_service.process_payment(amount)



 
