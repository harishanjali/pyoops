class Email:
    def send(self):
        return 'Sending an Email'
    
class Sms:
    def send(self):
        return 'Sending an SMS'
class Whatsapp:
    def send(self):
        return 'Sending whatsapp msg'
class Youtube:
    def send(self):
        return 'sending the youtube notification'
def notification_factory(choice):
    choices = {
        'mail':Email,
        'sms':Sms,
        'whatsapp':Whatsapp,
        'youtube':Youtube
    }
    target_class = choices.get(choice.lower())
    return target_class

my_tool = notification_factory('whatsapp')
obj = my_tool()
res = obj.send()
print(res)