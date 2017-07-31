from twilio.rest import Client

account_sid = "Your Account Sid"
auth_token = "Your Auth Token"
my_cell = "+Your Cell Number"
my_twilio = "+Your Twilio Number"

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

#my_msg = "This text is from python"

my_msg = input("Enter Your Message!!\n")
print("Message Sent to Mobile is - " + my_msg + "!")

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)