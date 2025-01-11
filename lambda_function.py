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
