### **Real-Time Language Translation Chatbot**  

This project implements a real-time language translation chatbot using **Amazon Lex V2**, **AWS Lambda**, and **Amazon Translate**. The chatbot allows users to input text in one language and receive a translated response in the desired target language.

---

### **Features**
- **Multi-language Support:** Translate text between multiple languages using Amazon Translate.  
- **Interactive Conversations:** Built using Amazon Lex V2 to understand user intents and slots for translation.  
- **Serverless Architecture:** Fulfillment logic handled using AWS Lambda.  
- **Secure Integration:** Configured IAM roles for secure communication between AWS services.  

---

### **Technologies Used**
- **Amazon Lex V2**: For creating the chatbot, defining intents, and processing user inputs.  
- **AWS Lambda**: To handle the backend logic for translation.  
- **Amazon Translate**: For accurate and fast language translation.  
- **IAM Roles**: To securely connect and authorize services.  

---

### **Setup Instructions**

1. **Create the Chatbot**  
   - Go to the **Amazon Lex V2** console.  
   - Create a bot, define intents (`TranslateIntent`), and add slots for `TextToTranslate` and `TargetLanguage`.  
   - Add fulfillment messages for successful and failed responses.  

2. **Set Up AWS Lambda**  
   - Create a Lambda function with a Python 3.9+ runtime.  
   - Use the following code for the fulfillment logic:  
     ```python
     import boto3
     def lambda_handler(event, context):
         translate = boto3.client('translate')
         text = event['sessionState']['intent']['slots']['TextToTranslate']['value']['originalValue']
         target_language = event['sessionState']['intent']['slots']['TargetLanguage']['value']['originalValue']
         
         response = translate.translate_text(
             Text=text,
             SourceLanguageCode='auto',
             TargetLanguageCode=target_language
         )
         
         translated_text = response['TranslatedText']
         return {
             'sessionState': {
                 'dialogAction': {
                     'type': 'Close'
                 },
                 'intent': {
                     'name': event['sessionState']['intent']['name'],
                     'state': 'Fulfilled'
                 }
             },
             'messages': [
                 {
                     'contentType': 'PlainText',
                     'content': translated_text
                 }
             ]
         }
     ```
   - Deploy the function and note the ARN.  

3. **Integrate Lambda with Lex**  
   - In the Lex V2 console, associate the Lambda function with the bot alias.  
   - Set up the Lambda function as the fulfillment code hook.  

4. **Test the Bot**  
   - Build the bot in Lex V2.  
   - Test with sample utterances like `Translate "Hello" to Spanish`.  
   - Verify the translated response.  

---

### **Usage**  
- Interact with the bot through the Lex V2 test console or integrate it into an application.  
- Provide input text and target language, and the bot will return the translated text.  

---

### Example Usage
![image](https://github.com/user-attachments/assets/aa9dca0d-9799-4ed8-8a9e-e33f888ae774)
